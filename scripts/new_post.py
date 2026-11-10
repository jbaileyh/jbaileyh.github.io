#!/usr/bin/env python3
"""Create a new post skeleton.

    python scripts/new_post.py <section> "Post title" [--r]

section: ai | data | art | leadership | other
--r      start the post with an R chunk instead of Python
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

SECTIONS = {
    "ai": ("AI", "chip"),
    "data": ("Data", "browser"),
    "art": ("Art", "palette"),
    "leadership": ("Leadership", "megaphone"),
    "other": ("Other", "mug"),
}

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("section", choices=SECTIONS)
parser.add_argument("title")
parser.add_argument("--r", action="store_true", help="use an R setup chunk")
args = parser.parse_args()

today = dt.date.today().isoformat()
slug = re.sub(r"[^a-z0-9]+", "-", args.title.lower()).strip("-")[:60]
root = pathlib.Path(__file__).resolve().parent.parent
folder = root / "posts" / args.section / f"{today}-{slug}"
if folder.exists():
    sys.exit(f"Already exists: {folder}")
folder.mkdir(parents=True)

label, art = SECTIONS[args.section]
if args.r:
    engine = ""
    setup = '```{r}\n#| include: false\nsource("../../../assets/theme_StellarGrok.R")\nlibrary(ggplot2)\n```'
else:
    engine = "jupyter: python3\n"
    setup = '```{python}\n#| include: false\nimport sys; sys.path.insert(0, "../../../assets")\nimport StellarGrok; StellarGrok.use()\n```'

(folder / "index.qmd").write_text(f'''---
title: "{args.title}"
description: "One or two sentences that show on the listing card."
date: {today}
categories: [{label}]
# image: thumbnail.png   # optional: add a picture to this folder for link previews
draft: true          # remove when you're ready to publish
{engine}---

{setup}

Start writing here.
''', encoding="utf-8")
print(f"Created {folder.relative_to(root)}/index.qmd")
