"""Run the real migrations in a transaction; leave the CI database unchanged."""
import os
from pathlib import Path

import psycopg
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def db():
    with psycopg.connect(os.environ['DATABASE_URL']) as conn:
        try:
            conn.execute((ROOT / 'database/migrations/001_init.sql').read_text(), prepare=False)
            migration = (ROOT / 'database/migrations/002_geometry_nonempty.sql').read_text()
            conn.execute(migration.replace('BEGIN;', '').replace('COMMIT;', ''), prepare=False)
            conn.execute((ROOT / 'database/seed/001_seed.sql').read_text(encoding='utf-8'), prepare=False)
            yield conn
        finally:
            conn.rollback()


@pytest.mark.parametrize('table,wkt', [
    ('zones', 'MULTIPOLYGON EMPTY'), ('assets', 'MULTIPOLYGON EMPTY'),
    ('facilities', 'POINT EMPTY'),
])
def test_empty_geometry_rejected_by_database(db, table, wkt):
    with pytest.raises(psycopg.errors.CheckViolation) as error:
        with db.transaction():
            db.execute(f'UPDATE {table} SET geom = ST_GeomFromText(%s, 4326)', (wkt,))
    assert error.value.diag.constraint_name == f'{table}_geom_nonempty'


@pytest.mark.parametrize('table', ['zones', 'assets', 'facilities'])
def test_null_geometry_rejected(db, table):
    with pytest.raises(psycopg.errors.NotNullViolation):
        with db.transaction():
            db.execute(f'UPDATE {table} SET geom = NULL')


def test_invalid_geometry_rejected(db):
    with pytest.raises(psycopg.errors.CheckViolation):
        with db.transaction():
            db.execute("UPDATE assets SET geom = ST_GeomFromText("
                         "'MULTIPOLYGON(((0 0,1 1,1 0,0 1,0 0)))',4326)")


def test_successful_write_increments_once_and_stale_write_changes_nothing(db):
    query = """UPDATE assets SET name=%s, version=version+1, updated_at=now()
               WHERE external_id=%s AND version=%s RETURNING version, name"""
    assert db.execute(query, ('accepted', 'A-001', 1)).fetchone() == (2, 'accepted')
    assert db.execute(query, ('stale', 'A-001', 1)).fetchone() is None
    assert db.execute("SELECT version,name FROM assets WHERE external_id='A-001'").fetchone() == (2, 'accepted')


def test_version_trigger_does_not_increment_version(db):
    assert db.execute("UPDATE assets SET name='administrative test' WHERE external_id='A-001' RETURNING version").fetchone() == (1,)


def test_upgrade_rejects_preexisting_empty_geometry():
    with psycopg.connect(os.environ['DATABASE_URL']) as conn:
        try:
            conn.execute((ROOT / 'database/migrations/001_init.sql').read_text(), prepare=False)
            conn.execute("INSERT INTO zones VALUES ('empty','empty',ST_GeomFromText('MULTIPOLYGON EMPTY',4326))")
            migration = (ROOT / 'database/migrations/002_geometry_nonempty.sql').read_text()
            with pytest.raises(psycopg.errors.CheckViolation):
                with conn.transaction():
                    conn.execute(migration.replace('BEGIN;', '').replace('COMMIT;', ''), prepare=False)
        finally:
            conn.rollback()
