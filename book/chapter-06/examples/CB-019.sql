UPDATE features
SET status = :status,
    version = version + 1,
    updated_at = now()
WHERE id = :id
  AND version = :expected_version
RETURNING id, version, updated_at;
