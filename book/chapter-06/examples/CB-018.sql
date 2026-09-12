SELECT id, name
FROM facilities
ORDER BY geom <-> ST_SetSRID(ST_Point(:lon, :lat), 4326)
LIMIT 5;
