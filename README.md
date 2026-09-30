# 999910.com — Forever Perfect · 久久久久 · 十全十美

A static website about Chinese lucky numbers. It has free tools (number meanings, phone/plate/house checker, almanac date finder, zodiac and compatibility, Kua feng shui, numeric-domain value), a culture guide, a 37-page number dictionary, lead generation, donations, a monthly contest, careers and advertising pages.

- **Hosting:** GitHub Pages (free plan). No build step is required at runtime.
- **Live (project URL):** https://webworksa1.github.io/999910-com/
- **Research & concept:** [`docs/RESEARCH.md`](docs/RESEARCH.md)
- **Phase-wise build prompt:** [`docs/BUILD-PROMPT.md`](docs/BUILD-PROMPT.md)

## Structure
```
index.html, meaning, checker, dates, zodiac, fengshui, domains   ← tools
culture, videos, methodology, numbers/*.html                     ← content (SEO)
consult, advertise, support, contest, careers, contact, about    ← revenue & community
legal (trademark/copyright, privacy, cookies, terms), 404
assets/css/style.css   design system (light/dark)
assets/js/config.js    ← EDIT ME: AdSense, GA4, donations, YouTube, contest, form alias
assets/js/engine.js    number/almanac/zodiac/Kua/domain engine
assets/js/core.js      nav, consent, ads, forms, modals, video, donations
assets/js/tools.js     tool UIs
tools/*.py             page generator (python3 tools/build.py)
```

## Editing
- Change settings in `assets/js/config.js`. No rebuild is needed.
- Change page content in `tools/pages_a.py` / `tools/pages_b.py`, then run `python3 tools/build.py`.
- For the custom domain 999910.com: run `python3 tools/build.py --base /`, add a `CNAME` file and configure DNS (see the checklist in `docs/BUILD-PROMPT.md`).

## Forms
All forms post through FormSubmit to the owner's private inbox. The address is stored obfuscated and never rendered. The first live submission triggers a one-time FormSubmit activation email.

## Legal
“999910” is used as a domain name and numeral only. There is no affiliation with any owner of “999”/“9999” marks. See `legal.html#trademark`.
