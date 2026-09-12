# spatial-query
Builds a structured, parameterizable spatial query plan from a collection, bbox, filters, and limit.

Implementation: `skills.core.build_spatial_query_plan`.

Safety rule: raw SQL is never accepted or emitted. Only whitelisted operators are allowed.