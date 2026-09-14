#!/usr/bin/env python3
"""Parses faq/**/*.md (frontmatter + body) into site/data.json for the demo help center."""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FAQ_DIR = ROOT / "faq"
OUT = ROOT / "site" / "data.json"

# Ordem de TODAS as categorias do projeto (mantida para quando as demais
# áreas forem reativadas). A ordem das 6 categorias de Suporte já segue o
# volume real de atendimentos do Suri em 3 meses: Holter 1.540 > MAPA 1.012 >
# CardioNet 823 > CardioSmart 209 > Pressão Central 140 > ECG 92.
CATEGORY_ORDER = [
    "Holter", "MAPA", "CardioNet", "CardioSmart", "Pressão Central",
    "ECG", "Comercial", "Financeiro", "Assistência Técnica",
]

# Nesta primeira versão de teste, o foco é só o Suporte Técnico (77,4% dos
# atendimentos do Suri) — Comercial, Financeiro e Assistência Técnica ficam
# "on hold" (conteúdo continua no repo, só não entra no site gerado) até o
# carro-chefe (suporte) estar validado e adotado pelos clientes.
ACTIVE_CATEGORIES = [
    "Holter", "MAPA", "CardioNet", "CardioSmart", "Pressão Central", "ECG",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_file(path: Path):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    meta = yaml.safe_load(m.group(1)) or {}
    body = m.group(2).strip()
    meta["body"] = body
    meta["is_skeleton"] = path.name.startswith("_")
    return meta


def main():
    categories = {name: [] for name in CATEGORY_ORDER}
    for md_file in sorted(FAQ_DIR.glob("*/*.md")):
        meta = parse_file(md_file)
        if not meta:
            continue
        cat = meta.get("categoria", "Outros")
        categories.setdefault(cat, []).append(meta)

    data = []
    for cat in ACTIVE_CATEGORIES:
        articles = categories.get(cat, [])
        real_articles = [a for a in articles if not a.get("is_skeleton")]
        skeleton = next((a for a in articles if a.get("is_skeleton")), None)
        data.append({
            "categoria": cat,
            "artigos": real_articles,
            "esqueleto": skeleton,
        })

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    on_hold = [c for c in CATEGORY_ORDER if c not in ACTIVE_CATEGORIES]
    print(f"Wrote {OUT} with {sum(len(c['artigos']) for c in data)} articles across {len(data)} categories")
    print(f"On hold (não incluídas neste build): {', '.join(on_hold)}")


if __name__ == "__main__":
    main()
