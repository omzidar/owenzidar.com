# owenzidar.com

Static personal website (9 pages: Home, Bio, CV, Research, Teaching, Book, Press, Other, Contact).
Style: Raj Chetty's site (centered name, text nav, featured work) and Henrik Kleven's site (condensed headings, rounded photo, CV button, icon row, press clippings grid).

## How to edit

1. Edit the page body in `src/<page>.html` (plain HTML; the top two comments set the page title and description).
2. Run `python3 build.py`. This wraps each body in the shared header, nav, and footer and writes `index.html`, `bio.html`, etc. to this folder.
3. Open `index.html` in a browser to check.

Never edit the root `*.html` files directly; `build.py` overwrites them. Nav items and order live in the `NAV` list in `build.py`. Styles are in `assets/css/style.css`.

To update the CV: replace `files/OwenZidarCV.pdf` (no rebuild needed).

## Publishing (live since Oct 6, 2026)

- Hosted on **GitHub Pages**: repo `github.com/omzidar/owenzidar.com` (public, branch `main`, root folder). `CNAME` file = `owenzidar.com`; HTTPS enforced.
- Domain registered at **GoDaddy** (account 51283181, omzidar@gmail.com; paid through Apr 2, 2027, auto-renew). DNS: four A records `@` -> 185.199.108/109/110/111.153; CNAME `www` -> `omzidar.github.io`. GoDaddy forwarding to scholar.princeton.edu was removed.
- GitHub CLI lives at `~/.local/bin/gh` (logged in as omzidar).
- `_archive_princeton/` is git-ignored and never uploaded.

`build.py` also writes `404.html`, `sitemap.xml`, `robots.txt`, share-preview tags (images: `assets/img/og-default.jpg`, `og-book.jpg`), and forwarding pages for old Princeton paths (`/publications`, `/bio`, `/cv`, `/classes`, `/discussions`, `/other-writing`, `/press`, ...).

To publish an edit: change `src/<page>.html`, run `python3 build.py`, then
`git add -A && git commit -m "update" && git push` (live about a minute later).

## Where things came from (Oct 6, 2026)

- Papers, appendices, data, replication zips, discussion slides, and all course materials were downloaded from zidar.princeton.edu into `files/` so links keep working after the Princeton site goes away.
- `_archive_princeton/` (not for upload) holds a full copy of the old site's pages plus files left off the new site: the old CV, the 2020-21 RA posting, and the RA task data (two CPS zips, 100 MB and 129 MB).
- Book coverage comes from the Sept 26 Substack "Media Round Up" and the Sept 17 press email. Press-card images are the articles' own preview images, saved in `assets/img/press/`.

## Status (Oct 7, 2026)

Pages: Home, Bio / CV, Research, Book, Teaching, Press, Other, Contact (nav order set in `build.py`).
Recent decisions: blue links, title-case nav; Henrik-style home (no CV/Book buttons; icons = NBER, Substack, X, LinkedIn, Email; Scholar/Wikipedia/Bluesky removed); book description = one sentence; praise trimmed to 9 short quotes; Book page coverage trimmed to a "Selected coverage" list with the NYT Oct 2 story first under News; Press page = clippings only (full coverage-by-paper list saved in `_archive_princeton/press_coverage_by_paper.html`); early working papers, Booth courses, student/RA lists, CV summary, keynotes removed.

Oct 7: added share previews, OZ favicon, 404 page, sitemap/robots, old-Princeton-path forwarding pages, bolder Featured Work charts; Bio/CV merged (headshot download = 300dpi); service roles moved to Bio; Search Console verified (URL-prefix https://owenzidar.com/, sitemap submitted).

Oct 7 (later): Book page now has a 'Book talks, fall 2026' list (19 events; linked so far: Labyrinth, Princeton 9/28, CAP, SPIA DC, AEI, Duke, Dartmouth, Yale Law, Harvard Stone, MIT, Berkeley, NTA) — add links for Hyde Park Labs, HKS/Furman, Chicago ETA, Wharton, Swarthmore, UCLA, Haas as hosts post them. TV/podcasts list: CNN Smerconish, Fox Kilmeade, Bloomberg Businessweek, Odd Lots, At the Money, Wall Street Week, Marketplace, Erin Talks Money, Rational Reminder. Press page research grid leads with one top story per paper (WaPo/NYT TCJA, Economist top wealth, Bloomberg Capitalists [text card], WaPo JPE, WSJ JEP/cap gains/health/TPE). Removed: Fortier PR contact, Chartbook/No Mercy/PAW/MarketWatch/Tax Foundation cards, NBER 2015 interview, Booth Review podcast, MIT panel.

## Open items

- [ ] JEP 2024 is 38(3): 61-88 per Crossref; the CV says 1-30 and "lead article". The site uses 61-88.
- [ ] Old press links that were dead now point to the Wayback Machine (only in the archived coverage-by-paper list).
- [ ] GoDaddy `www` CNAME still pointed at ghs.google.com as of Oct 6, 4:10pm; change to `omzidar.github.io` and save.
- [ ] Ask Princeton IT to redirect zidar.princeton.edu (all paths, path-preserving) to owenzidar.com.
