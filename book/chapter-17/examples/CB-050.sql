EXPLAIN (ANALYZE, BUFFERS)
SELECT id, status, geom
FROM assets
WHERE geom && ST_MakeEnvelope(35.20,31.88,35.25,31.93,4326);
