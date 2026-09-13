CREATE TABLE buildings (
  id uuid PRIMARY KEY,
  status text NOT NULL CHECK (status IN ('draft','verified','archived')),
  geom geometry(MultiPolygon, 4326) NOT NULL
    CHECK (ST_IsValid(geom) AND NOT ST_IsEmpty(geom)),
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX buildings_geom_gix
ON buildings USING GIST (geom);
