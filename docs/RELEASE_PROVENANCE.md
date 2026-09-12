# Release provenance

Prepared for the first companion release of **هندسة البرمجيات المكانية: من البيانات الجغرافية إلى التطبيقات الذكية**.

## Freeze procedure

1. Merge the finalization pull request only after all protected required checks are green.
2. Record the resulting `main` commit SHA.
3. Create tag/release `book-v1.0.0` pointing to that exact commit.
4. Put that commit SHA and the stable release URL into the production manuscript.
5. Generate the printed QR from the stable release URL, not from `main`.
6. Re-render the DOCX and preflight the final PDF after the publication metadata is inserted.

## Audit date

Final third-party notice and release-gate audit: **2026-09-12**.

## Release URL template

`https://github.com/mmashharawi2021-cell/spatial-software-engineering-book/releases/tag/book-v1.0.0`

The immutable commit SHA is intentionally filled into the publication artifact only after the finalization pull request has merged.
