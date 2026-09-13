CREATE TABLE assets (
  id uuid PRIMARY KEY,
  name text NOT NULL,
  status text NOT NULL CHECK (status IN ('draft','review','approved')),
  version integer NOT NULL DEFAULT 1 CHECK (version > 0),
  geom geometry(Geometry, 4326) NOT NULL
    CHECK (ST_IsValid(geom) AND NOT ST_IsEmpty(geom))
);
CREATE INDEX assets_geom_gix ON assets USING gist (geom);
