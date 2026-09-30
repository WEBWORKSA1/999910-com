#!/usr/bin/env python3
"""Build 999910.com static site.

Usage:
  python3 tools/build.py                 # for GitHub Pages project URL (/999910-com/)
  python3 tools/build.py --base /        # after pointing the custom domain 999910.com
"""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
import pages_a as A, pages_b as B
from tpl import SITE

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
base = "/999910-com/"
if "--base" in sys.argv:
    base = sys.argv[sys.argv.index("--base") + 1]


def write(rel, html):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    return rel


pages = {
    "index.html": A.home(), "meaning.html": A.meaning(), "checker.html": A.checker(), "dates.html": A.dates(),
    "zodiac.html": A.zodiac(), "fengshui.html": A.fengshui(), "domains.html": A.domains(),
    "culture.html": B.culture(), "videos.html": B.videos(), "consult.html": B.consult(), "advertise.html": B.advertise(),
    "support.html": B.support(), "contest.html": B.contest(), "careers.html": B.careers(), "contact.html": B.contact(),
    "about.html": B.about(), "methodology.html": B.methodology(), "legal.html": B.legal(),
    "numbers/index.html": B.numbers_index(), "404.html": B.notfound(base),
}
for n in B.NUMBERS:
    pages[f"numbers/{n}.html"] = B.number_page(n)
for rel, html in pages.items():
    write(rel, html)

today = datetime.date.today().isoformat()
prio = {"index.html": "1.0", "meaning.html": "0.9", "checker.html": "0.9", "dates.html": "0.9", "culture.html": "0.8", "consult.html": "0.8"}
urls = "".join(
    f"<url><loc>{SITE}/{'' if r == 'index.html' else r}</loc><lastmod>{today}</lastmod><priority>{prio.get(r, '0.6')}</priority></url>\n"
    for r in pages if r != "404.html")
write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
write("manifest.webmanifest", '{"name":"999910.com — Chinese Lucky Numbers","short_name":"999910","start_url":"./index.html","display":"standalone","background_color":"#FAF6EE","theme_color":"#C8102E","icons":[{"src":"assets/img/favicon.svg","sizes":"any","type":"image/svg+xml"}]}\n')
write(".nojekyll", "")
write("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect x="1" y="1" width="38" height="38" rx="9" fill="#C8102E"/><rect x="4" y="4" width="32" height="32" rx="6" fill="none" stroke="#F3D27A" stroke-width="1.2"/><text x="20" y="27.5" text-anchor="middle" font-family="serif" font-size="18" font-weight="700" fill="#fff">久</text></svg>\n')
print(f"Built {len(pages)} pages (base={base})")
