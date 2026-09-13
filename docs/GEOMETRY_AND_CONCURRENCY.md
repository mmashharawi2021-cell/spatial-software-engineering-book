# Geometry and optimistic concurrency policy

All persisted geometries in `zones`, `assets`, and `facilities` must be non-null,
non-empty, valid, and conform to the declared geometry type and SRID. These are
separate requirements: `ST_IsValid` does not prohibit empty geometries.
Apply migrations in numerical order, including `002_geometry_nonempty.sql`.
The latter deliberately fails if old rows contain empty geometries; inspect and
repair those rows before retrying. It does not delete or invent geometry data.
CB-017, CB-020 and CB-021 demonstrate the same storage policy.

The application owns the version increment, as demonstrated by CB-019. Each
accepted write uses one atomic statement with `WHERE id = ... AND version =
expected_version`, sets `version = version + 1`, and returns the new version.
Zero returned rows mean the requested write was not accepted. Never follow a
failed comparison with an unconditional overwrite. A separate read may classify
missing and conflicting records, subject to authorization.

The database trigger updates only `updated_at`; it must not increment `version`.
Every application write path must follow this policy. Direct administrative SQL
is outside the concurrency protocol and must not be used as an application write
path. Two clients submitting the same expected version can produce at most one
accepted write. A rejected write changes neither content nor version.

Use `expected_version` consistently in API and offline operation payloads. It is
the last server version observed by the client, not a client-generated next
version. Return `version_conflict` (HTTP 409 for the illustrated JSON contract)
when the comparison fails. Resolve against refreshed server state before retry.
HTTP `If-Match` is a distinct conditional request contract with HTTP 412 for a
failed precondition; do not silently interchange the two contracts.

The reference API currently exposes reads only. These write semantics are
demonstrated by CB-019 and database tests, not a claimed production sync endpoint.
The v0.6 manuscript mirrors this policy. Its source provenance is documented in the delivery report.
