CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE zones (
  id text PRIMARY KEY,
  name text NOT NULL,
  geom geometry(MultiPolygon, 4326) NOT NULL,
  CONSTRAINT zones_geom_valid CHECK (ST_IsValid(geom))
);
CREATE INDEX zones_geom_gix ON zones USING gist (geom);

CREATE TABLE assets (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  external_id text UNIQUE NOT NULL,
  name text NOT NULL,
  zone_id text REFERENCES zones(id) ON UPDATE CASCADE ON DELETE SET NULL,
  lifecycle_status text NOT NULL CHECK (lifecycle_status IN ('draft','active','archived')),
  review_status text NOT NULL CHECK (review_status IN ('pending','approved','rejected')),
  version integer NOT NULL DEFAULT 1 CHECK (version > 0),
  observed_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  geom geometry(MultiPolygon, 4326) NOT NULL,
  CONSTRAINT assets_geom_valid CHECK (ST_IsValid(geom))
);
CREATE INDEX assets_geom_gix ON assets USING gist (geom);
CREATE INDEX assets_zone_status_idx ON assets(zone_id, review_status);

CREATE TABLE facilities (
  id text PRIMARY KEY,
  name text NOT NULL,
  facility_type text NOT NULL,
  geom geometry(Point, 4326) NOT NULL,
  CONSTRAINT facilities_geom_valid CHECK (ST_IsValid(geom))
);
CREATE INDEX facilities_geom_gix ON facilities USING gist (geom);

CREATE TABLE survey_observations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  asset_id uuid NOT NULL REFERENCES assets(id) ON UPDATE CASCADE ON DELETE CASCADE,
  observed_at timestamptz NOT NULL,
  gps_accuracy_m numeric CHECK (gps_accuracy_m IS NULL OR gps_accuracy_m >= 0),
  has_photo boolean NOT NULL DEFAULT false,
  review_status text NOT NULL CHECK (review_status IN ('pending','approved','rejected')),
  notes text
);
CREATE INDEX survey_observations_asset_time_idx ON survey_observations(asset_id, observed_at DESC);

CREATE OR REPLACE FUNCTION set_updated_at() RETURNS trigger AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER assets_set_updated_at
BEFORE UPDATE ON assets
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
