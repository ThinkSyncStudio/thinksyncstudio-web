"""Check static routes, anchors, policy/support coverage, and release status."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ("braglytics", "ateyet", "back-to-better", "yuan", "gossamer", "autojustice")
EMAIL = "support@thinksyncstudio.com"

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.h1, self.statuses = [], set(), 0, 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            assert a["id"] not in self.ids, "Duplicate id: " + a["id"]
            self.ids.add(a["id"])
        self.h1 += tag == "h1"
        self.statuses += a.get("class") == "app-status"
        for key in ("href", "src"):
            if key in a:
                self.links.append(a[key])

pages = {p: Page(p.read_text()) for p in ROOT.rglob("*.html")
         if not any(x in {"archive", ".git", "node_modules"} for x in p.relative_to(ROOT).parts)}
errors = []
for path, page in pages.items():
    rel = str(path.relative_to(ROOT))
    if page.h1 != 1:
        errors.append(f"{rel}: expected one H1, got {page.h1}")
    for slug in SLUGS:
        if f"/{slug}/" not in page.links:
            errors.append(f"{rel}: missing {slug} navigation")
    for required in ("/apps/", "/policies/", "/support/"):
        if required not in page.links:
            errors.append(f"{rel}: missing {required}")
    for link in page.links:
        u = urlsplit(link)
        if u.scheme == "mailto" and u.path != EMAIL:
            errors.append(f"{rel}: unexpected support email {u.path}")
        if u.scheme or u.netloc:
            continue
        dest = (ROOT / u.path.lstrip("/") if u.path.startswith("/") else path.parent / u.path) if u.path else path
        if dest.is_dir():
            dest /= "index.html"
        dest = dest.resolve()
        if not dest.exists():
            errors.append(f"{rel}: missing target {link}")
        elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:
            errors.append(f"{rel}: missing anchor {link}")
for name in ("index.html", "apps/index.html"):
    if pages[ROOT / name].statuses != 6:
        errors.append(f"{name}: expected six Coming soon labels")
for slug in SLUGS:
    path = ROOT / slug / "index.html"
    if pages[path].statuses != 1 or "Privacy, terms &amp; support" not in path.read_text():
        errors.append(f"{slug}: missing status or app resources")
assert not errors, "\n".join(errors)
print(f"PASS: {len(pages)} pages; links, assets, anchors, app status, navigation, and support email.")
