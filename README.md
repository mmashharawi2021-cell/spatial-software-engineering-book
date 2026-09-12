# Spatial Software Engineering
## هندسة البرمجيات المكانية

**Official companion repository** for the book **«هندسة البرمجيات المكانية: من البيانات الجغرافية إلى التطبيقات الذكية»**.

**Author & Maintainer:** Eng. Mohanad Anwar Khalil Al-Mashharawi — Full-Stack GIS Developer

**Repository:** https://github.com/mmashharawi2021-cell/spatial-software-engineering-book

**Reference implementation:** `GeoSmart Assets` — an educational spatial intelligence platform that connects field data, validation, PostGIS, API services, Web GIS, offline workflows, dashboards, automation, testing, security, and optional GeoAI.

> Book manuscript copyright is separate from the companion code license. Synthetic training data has its own license. Third-party software and standards retain their original ownership and licenses.

---

# GeoSmart Assets — Companion Package v0.3

الحزمة المرجعية المصاحبة لكتاب «هندسة البرمجيات المكانية: من البيانات الجغرافية إلى التطبيقات الذكية».

> البيانات التدريبية اصطناعية ولا تمثل سجلات أو معالم حقيقية. بعض الإحداثيات تقع ضمن فضاء جغرافي حقيقي لأغراض شرح الخرائط فقط.

## Book ↔ Repository Mapping
خريطة الربط الرسمية بين الفصول ومسارات الكود موجودة في:

- `docs/BOOK_REPOSITORY_MAPPING.md`
- `book/chapter-01/` حتى `book/chapter-21/`

هذه الخريطة تجعل كل فصل قابلًا للتتبع إلى الأمثلة والمكونات التنفيذية المرتبطة به. عند إصدار الطبعة الأولى سيُفضّل الربط إلى Release ثابت بدل الاعتماد على `main` المتغير.

## Skills + Agents + MCP-ready
أضيفت طبقة ذكية منظمة فوق النظام الجغرافي الأساسي دون ربط المشروع بمزود LLM واحد:

- `skills/`: مهارات مكانية deterministic وقابلة للاختبار بشكل مستقل.
- `agents/`: وكلاء ينسقون المهارات ولا يتجاوزون طبقة الصلاحيات أو قاعدة البيانات.
- `mcp/`: Tool registry وmanifest مستقلان عن مزود النموذج وجاهزان للتغليف لاحقًا داخل MCP server.
- `docs/agent-architecture.md`: معمارية الفصل بين GIS logic وagent orchestration وLLM adapters.

### المهارات الحالية
`validate-geojson`, `transform-crs`, `spatial-query`, `summarize-field-data`, `detect-data-quality-issues`, `generate-map-style`.

### الوكلاء الحاليون
`SpatialDataAgent`, `SpatialQueryAgent`, `FieldDataAgent`, `MapAssistantAgent`, `GeoAIAssistant`.

**قاعدة أمنية:** `SpatialQueryAgent` لا يقبل SQL حر؛ ينتج خطة استعلام structured ومحدودة وقابلة للـparameterization.

## ما تغير في v0.3
- إضافة Skills وAgents وMCP-ready registry.
- إبقاء GeoAI provider-agnostic مع planner adapter اختياري.
- توسيع الاختبارات والـCI لتشمل الطبقة الذكية.
- تحديث بيئة PostgreSQL/PostGIS المرجعية.
- إضافة health checks وAPI container.
- إصلاح bbox ليستخدم `ST_Intersects` بعد prefilter مكاني.
- إضافة CORS صريح وready check وpagination بسيطة.
- تقوية التحقق من GeoJSON وETL.
- فصل ترخيص الكود عن ترخيص Dataset.

## تشغيل كامل
1. انسخ `.env.example` إلى `.env` وغيّر كلمة المرور عند الحاجة.
2. شغّل: `docker compose up --build`.
3. تحقق من API: `http://localhost:8000/health` و`/ready` و`/docs`.
4. للويب: `cd web && npm install && npm run dev`.

## التحقق
- Python + Skills + Agents + MCP: `python -m compileall -q api python tests skills agents mcp && pytest -q`
- ETL: `python python/validate_features.py && python python/etl.py`
- Web: `cd web && npm install && npm run build`
- Database: راجع `database/tests/001_smoke.sql` وGitHub Actions.

## مراجع رسمية
راجع `docs/OFFICIAL_REFERENCES.md`.

## ملاحظة امتثال
الـAPI في هذه الحزمة **تعليمي ومتأثر بممارسات OGC API - Features** لكنه لا يُوصف بأنه OGC-compliant ما لم تنفذ نقاط conformance المطلوبة ويُشغّل اختبار امتثال مناسب.
