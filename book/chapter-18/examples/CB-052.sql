-- مثال مبسط: دور القراءة لا يملك الكتابة
GRANT SELECT ON assets TO app_reader;
GRANT SELECT, INSERT, UPDATE ON assets TO app_editor;
REVOKE ALL ON assets FROM PUBLIC;
