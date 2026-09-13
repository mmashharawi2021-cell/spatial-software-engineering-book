-- Apply after 001_init.sql on both existing and fresh databases.
-- Existing empty geometries fail validation; repair them explicitly before retrying.
BEGIN;
ALTER TABLE zones ADD CONSTRAINT zones_geom_nonempty CHECK (NOT ST_IsEmpty(geom));
ALTER TABLE assets ADD CONSTRAINT assets_geom_nonempty CHECK (NOT ST_IsEmpty(geom));
ALTER TABLE facilities ADD CONSTRAINT facilities_geom_nonempty CHECK (NOT ST_IsEmpty(geom));
COMMIT;
