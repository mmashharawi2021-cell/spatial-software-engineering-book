ALTER TABLE assets ADD CONSTRAINT assets_geom_srid_chk
CHECK (ST_SRID(geom)=4326);

ALTER TABLE assets ADD CONSTRAINT assets_geom_valid_chk
CHECK (ST_IsValid(geom));

ALTER TABLE assets ADD CONSTRAINT assets_geom_nonempty_chk
CHECK (NOT ST_IsEmpty(geom));
