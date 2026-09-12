ALTER TABLE assets ADD CONSTRAINT assets_geom_srid_chk
CHECK (ST_SRID(geom)=4326);

ALTER TABLE assets ADD CONSTRAINT assets_geom_valid_chk
CHECK (ST_IsValid(geom));
