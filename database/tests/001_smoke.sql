DO $$
DECLARE
  asset_count integer;
  invalid_count integer;
BEGIN
  SELECT count(*) INTO asset_count FROM assets;
  IF asset_count < 3 THEN
    RAISE EXCEPTION 'Expected seeded assets, got %', asset_count;
  END IF;

  SELECT count(*) INTO invalid_count FROM assets WHERE NOT ST_IsValid(geom);
  IF invalid_count <> 0 THEN
    RAISE EXCEPTION 'Invalid geometries found: %', invalid_count;
  END IF;
END $$;

SELECT external_id
FROM assets
WHERE geom && ST_MakeEnvelope(35.2,31.89,35.22,31.91,4326)
  AND ST_Intersects(geom, ST_MakeEnvelope(35.2,31.89,35.22,31.91,4326))
ORDER BY external_id;
