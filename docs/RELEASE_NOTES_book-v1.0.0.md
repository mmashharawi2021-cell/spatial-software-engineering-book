# book-v1.0.0 — First Edition Companion Release

This file is the prepared release note for the first frozen companion-code release of the Arabic book **هندسة البرمجيات المكانية: من البيانات الجغرافية إلى التطبيقات الذكية**.

## Release scope

The release is intended to freeze the repository state used by the first publication edition. It includes:

- the GeoSmart Assets reference architecture;
- PostgreSQL/PostGIS migrations, seed data, and smoke tests;
- FastAPI reference API with live PostGIS integration tests;
- MapLibre/Vite/TypeScript web example with reproducible `npm ci` install and Playwright E2E tests;
- Python validation/ETL examples;
- Skills, Agents, and MCP-ready tool registry architecture;
- exact file-backed mapping for all 60 manuscript code blocks;
- synthetic training datasets and their data-license notice;
- final third-party dependency/license audit dated 2026-09-12;
- protected-branch release gate requiring `web`, `python-and-postgis`, and `dart-code-block` checks.

## Verification statement

Before the tag is created, the final `main` commit must pass all required GitHub Actions checks from a clean hosted runner. The tag `book-v1.0.0` must point to that exact green `main` commit.

## Licensing boundary

- Original companion code: `LICENSE-CODE` (MIT).
- Synthetic training data: `DATA_LICENSE.md` (CC0 1.0 unless a file states otherwise).
- Third-party dependencies/references: `THIRD_PARTY_LICENSES.md` and upstream terms.
- Manuscript text and book artwork: separate publication copyright; not granted under the code license.

## Stable release URL

After the tag/release is created, the publication should use:

`https://github.com/mmashharawi2021-cell/spatial-software-engineering-book/releases/tag/book-v1.0.0`

The mutable `main` branch should not be used as the QR target in the printed edition.
