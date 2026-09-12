CREATE TABLE assets (
  id uuid PRIMARY KEY,
  name text NOT NULL,
  status text NOT NULL CHECK (status IN ('draft','review','approved')),
  version integer NOT NULL DEFAULT 1,
  geom geometry(Geometry, 4326) NOT NULL
);
CREATE INDEX assets_geom_gix ON assets USING gist (geom);
