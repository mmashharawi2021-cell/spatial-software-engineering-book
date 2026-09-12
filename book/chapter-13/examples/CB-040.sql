CREATE MATERIALIZED VIEW dashboard_kpi AS
SELECT zone_id,
       count(*) FILTER (WHERE review_status='approved') AS approved,
       count(*) FILTER (WHERE review_status IN ('approved','rejected')) AS reviewed
FROM assets
GROUP BY zone_id;
