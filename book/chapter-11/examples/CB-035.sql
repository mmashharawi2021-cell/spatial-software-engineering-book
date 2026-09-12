CREATE TABLE sync_queue (
  operation_id TEXT PRIMARY KEY,
  entity_id TEXT NOT NULL,
  action TEXT NOT NULL,
  payload TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'pending'
);
