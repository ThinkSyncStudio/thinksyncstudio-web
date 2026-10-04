"""Refresh content-based asset versions. Run after editing CSS, JS, or OG art.

    python3 scripts/version-assets.py
    python3 scripts/version-assets.py --check

Archives are deliberately excluded. No dependencies or network access required.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ("styles.css", "script.js", "assets/og-studio.png")
versions = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()[:12]
            for name in ASSETS}
changed = []
for path in sorted(ROOT.rglob("*.html")):
    if any(part in {"archive", ".git", "node_modules"} for part in path.relative_to(ROOT).parts):
        continue
    before = path.read_text()
    after = before
    for name, version in versions.items():
        pattern = r'((?:href|src|content)="[^"?]*' + re.escape(name) + r')(?:\?[^"\s]*)?"'
        after = re.sub(pattern, lambda m: m[1] + "?v=" + version + '"', after)
    if after != before:
        changed.append(str(path.relative_to(ROOT)))
        if "--check" not in sys.argv:
            path.write_text(after)
if "--check" in sys.argv and changed:
    sys.exit("Stale asset versions: " + ", ".join(changed))
print("Asset versions current." if not changed else "Updated: " + ", ".join(changed))
