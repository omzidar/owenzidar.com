#!/usr/bin/env python3
"""Build owenzidar.com.

Each page's body lives in src/<page>.html. This script wraps every body in the
shared header, nav, and footer and writes the finished page to the site root.
It also writes 404.html, sitemap.xml, robots.txt, and small forwarding pages
for addresses from the old Princeton site (see OLD_PATHS).

    python3 build.py

Edit the NAV list below to add, rename, or reorder pages.
A page can set its title, description, and share image with comments at the
top of its src file, e.g. <!-- image: assets/img/og-book.jpg -->.
"""
import datetime
import html as htmllib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
SITE = "https://owenzidar.com"

NAV = [
    ("index", "Home"),
    ("bio", "Bio / CV"),
    ("research", "Research"),
    ("book", "Book"),
    ("teaching", "Teaching"),
    ("press", "Press"),
    ("commentary", "Commentary"),
    ("contact", "Contact"),
]

# Old zidar.princeton.edu paths -> new pages. If Princeton forwards
# zidar.princeton.edu/<path> to owenzidar.com/<path>, these catch it.
OLD_PATHS = {
    "publications": "research.html",
    "bio": "bio.html",
    "cv": "bio.html",
    "classes": "teaching.html",
    "discussions": "commentary.html",
    "other-writing": "commentary.html",
    "press": "press.html",
    "research-assistants": "index.html",
    "ra": "index.html",
    "zidar": "index.html",
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{base}<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="google-site-verification" content="aJECxOGeNziHfho_JyKpM7fgRYQVgAt_GMGWjnVnqmk">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Owen Zidar">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@omzidar">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
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

REDIRECT = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Owen Zidar</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<meta name="robots" content="noindex">
</head><body><p>This page has moved to <a href="{url}">{url}</a>.</p></body></html>
"""

META = re.compile(r"<!--\s*(title|description|image):\s*(.*?)\s*-->")
DEFAULT_DESC = "Owen Zidar, Professor of Economics and Public Affairs, Princeton University."


def render(slug, raw, current_slug, base=""):
    meta = dict(META.findall(raw))
    body = META.sub("", raw).strip("\n")
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'      <li><a href="{s}.html"{cur if s == current_slug else ""}>{l}</a></li>'
        for s, l in NAV
    )
    label = dict(NAV).get(slug, "")
    title = meta.get("title", label)
    page_title = "Owen Zidar" if slug == "index" else f"{title} | Owen Zidar"
    url = f"{SITE}/" if slug == "index" else f"{SITE}/{slug}.html"
    image = f"{SITE}/{meta.get('image', 'assets/img/og-default.jpg')}"
    return TEMPLATE.format(
        base=base,
        title=htmllib.escape(page_title, quote=True),
        description=htmllib.escape(meta.get("description", DEFAULT_DESC), quote=True),
        url=url,
        image=image,
        nav=nav,
        body=body,
        year=datetime.date.today().year,
    )


def build():
    for slug, _ in NAV:
        raw = (SRC / f"{slug}.html").read_text()
        (ROOT / f"{slug}.html").write_text(render(slug, raw, slug))
        print(f"built {slug}.html")

    # 404 page: <base href="/"> so links and styles work at any missing path.
    raw = (SRC / "404.html").read_text()
    (ROOT / "404.html").write_text(render("404", raw, None, base='<base href="/">\n'))
    print("built 404.html")

    for old, new in OLD_PATHS.items():
        d = ROOT / old
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(REDIRECT.format(url=f"{SITE}/{new}"))
    print(f"built {len(OLD_PATHS)} forwarding pages")

    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{SITE}/{'' if s == 'index' else s + '.html'}</loc><lastmod>{today}</lastmod></url>"
        for s, _ in NAV
    )
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nDisallow: /src/\nSitemap: {SITE}/sitemap.xml\n")
    print("built sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
