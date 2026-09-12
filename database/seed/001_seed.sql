INSERT INTO zones(id,name,geom) VALUES
('Z-A','منطقة ألف',ST_Multi(ST_GeomFromText('POLYGON((35.2 31.89,35.22 31.89,35.22 31.91,35.2 31.91,35.2 31.89))',4326))),
('Z-B','منطقة باء',ST_Multi(ST_GeomFromText('POLYGON((35.22 31.89,35.24 31.89,35.24 31.91,35.22 31.91,35.22 31.89))',4326)));

INSERT INTO assets(external_id,name,zone_id,lifecycle_status,review_status,geom) VALUES
('A-001','أصل تدريبي 1','Z-A','active','pending',ST_Multi(ST_GeomFromText('POLYGON((35.2055 31.893,35.2067 31.893,35.2067 31.8942,35.2055 31.8942,35.2055 31.893))',4326))),
('A-002','أصل تدريبي 2','Z-A','active','rejected',ST_Multi(ST_GeomFromText('POLYGON((35.209 31.894,35.2102 31.894,35.2102 31.8952,35.209 31.8952,35.209 31.894))',4326))),
('A-003','أصل تدريبي 3','Z-A','active','approved',ST_Multi(ST_GeomFromText('POLYGON((35.2125 31.892,35.2137 31.892,35.2137 31.8932,35.2125 31.8932,35.2125 31.892))',4326)));

INSERT INTO facilities(id,name,facility_type,geom) VALUES
('F-01','مرفق تدريبي 1','service',ST_SetSRID(ST_MakePoint(35.208,31.896),4326)),
('F-02','مرفق تدريبي 2','service',ST_SetSRID(ST_MakePoint(35.231,31.903),4326));
