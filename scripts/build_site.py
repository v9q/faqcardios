#!/usr/bin/env python3
"""Injects site/data.json into each site/*.template.html to produce its *.html.

Every template shares the same __DATA__ placeholder mechanism (a JSON payload
dropped into a <script type="application/json"> block), so any new template
added to PAGES automatically gets the current FAQ content on every rebuild —
no separate sync step needed between index.html and bot.html.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site" / "data.json"
SITE = ROOT / "site"

# (template filename, output filename)
PAGES = [
    ("index.template.html", "index.html"),
    ("bot.template.html", "bot.html"),
]


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    # Safe for embedding inside a <script type="application/json"> block.
    payload = json.dumps(data, ensure_ascii=False).replace("</script", "<\\/script")
    for template_name, out_name in PAGES:
        template_path = SITE / template_name
        if not template_path.exists():
            continue
        template = template_path.read_text(encoding="utf-8")
        out = template.replace("__DATA__", payload)
        out_path = SITE / out_name
        out_path.write_text(out, encoding="utf-8")
        print(f"Wrote {out_path} ({len(out)} bytes)")


if __name__ == "__main__":
    main()
