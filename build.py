#!/usr/bin/env python3
"""Build owenzidar.com.

Each page's body lives in src/<page>.html. This script wraps every body in the
shared header, nav, and footer and writes the finished page to the site root.

    python3 build.py

Edit the NAV list below to add, rename, or reorder pages.
"""
import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"

NAV = [
    ("index", "Home"),
    ("bio", "Bio"),
    ("cv", "CV"),
    ("research", "Research"),
    ("book", "Book"),
    ("teaching", "Teaching"),
    ("press", "Press"),
    ("commentary", "Commentary"),
    ("contact", "Contact"),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,600;0,700;1,400&family=Barlow+Condensed:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="index.html"><div class="brand-name">Owen Zidar</div></a>
  <nav class="site-nav" aria-label="Main">
    <ul>
{nav}
    </ul>
  </nav>
</header>
<main>
  <div class="wrap">
{body}
  </div>
</main>
<footer class="site-footer">
  <div class="wrap">
    <span>&copy; Copyright {year} Owen Zidar. All rights reserved.</span>
    <span><a href="mailto:ozidar@princeton.edu">ozidar@princeton.edu</a> &middot; <a href="https://www.everywheremillionaire.com">The Everywhere Millionaire</a></span>
  </div>
</footer>
</body>
</html>
"""

META = re.compile(r"<!--\s*(title|description):\s*(.*?)\s*-->")


def build():
    year = datetime.date.today().year
    for slug, label in NAV:
        raw = (SRC / f"{slug}.html").read_text()
        meta = dict(META.findall(raw))
        body = META.sub("", raw).strip("\n")
        current = ' aria-current="page"'
        nav = "\n".join(
            f'      <li><a href="{s}.html"{current if s == slug else ""}>{l}</a></li>'
            for s, l in NAV
        )
        title = meta.get("title", label)
        page_title = "Owen Zidar" if slug == "index" else f"{title} | Owen Zidar"
        html = TEMPLATE.format(
            title=page_title,
            description=meta.get("description", "Owen Zidar, Professor of Economics and Public Affairs, Princeton University."),
            nav=nav,
            body=body,
            year=year,
        )
        (ROOT / f"{slug}.html").write_text(html)
        print(f"built {slug}.html")


if __name__ == "__main__":
    build()
