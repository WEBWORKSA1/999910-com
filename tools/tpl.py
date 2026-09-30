"""Shared layout for 999910.com static pages (header, footer, head, widgets)."""
import json

SITE = "https://999910.com"
INTEREST = "https://web.works/contact"
VERSION = "20260930"

SEAL = ('<svg class="seal" viewBox="0 0 40 40" aria-hidden="true"><rect x="1" y="1" width="38" height="38" rx="9" fill="#C8102E"/>'
        '<rect x="4" y="4" width="32" height="32" rx="6" fill="none" stroke="#F3D27A" stroke-width="1.2"/>'
        '<text x="20" y="27.5" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="18" font-weight="700" fill="#fff">久</text></svg>')

NAV = [
    ("Meanings", "meaning.html", None),
    ("Checkers", None, [
        ("Phone Number Checker", "checker.html#phone"),
        ("Licence Plate Checker", "checker.html#plate"),
        ("House & Unit Number", "checker.html#house"),
        ("Auspicious Date Finder", "dates.html"),
        ("Numeric Domain Value", "domains.html"),
    ]),
    ("Zodiac", None, [
        ("Chinese Zodiac Finder", "zodiac.html"),
        ("Zodiac Compatibility", "zodiac.html#compat"),
        ("Kua Number & Directions", "fengshui.html"),
    ]),
    ("Culture", None, [
        ("999910 & Lucky Number Guide", "culture.html"),
        ("Number Dictionary A–Z", "numbers/index.html"),
        ("Videos", "videos.html"),
        ("How Our Tools Work", "methodology.html"),
    ]),
    ("Community", None, [
        ("Monthly Contest & Prizes", "contest.html"),
        ("Support Us / Donate", "support.html"),
        ("Careers — Join the Team", "careers.html"),
        ("Advertise & Sponsor", "advertise.html"),
        ("About", "about.html"),
    ]),
]


def head(title, desc, path, root, jsonld=None, ogtype="website"):
    url = SITE + "/" + path.replace("index.html", "")
    ld = ""
    for block in (jsonld or []):
        ld += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + "</script>\n"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#C8102E">
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="999910.com">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css?v={VERSION}">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{ld}</head>
"""


def header(root, active=""):
    items = []
    for label, href, sub in NAV:
        if sub:
            subs = "".join(f'<li><a href="{root}{h}">{l}</a></li>' for l, h in sub)
            items.append(f'<li><button class="dd" aria-haspopup="true">{label} ▾</button><ul class="sub">{subs}</ul></li>')
        else:
            cur = ' aria-current="page"' if active == href else ""
            items.append(f'<li><a href="{root}{href}"{cur}>{label}</a></li>')
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note"><a href="{INTEREST}" target="_blank" rel="noopener"><strong>Contact</strong>, if you are interested in this <strong>website / domain name / Sponsorship / Advertisement / Partnership</strong> →</a></div>
<header class="site-header">
 <div class="container nav">
  <a class="brand" href="{root}index.html" aria-label="999910.com home">{SEAL}<span>999910<span style="color:var(--red)">.com</span><small>Forever · Perfect</small></span></a>
  <ul class="menu" id="menu">
   <li><button class="icon-btn close" data-menu-close aria-label="Close menu">✕</button></li>
   {''.join(items)}
  </ul>
  <div class="nav-cta">
   <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 1 0 0 20V2z"/><circle cx="12" cy="12" r="9.2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>
   <a class="btn btn-red btn-sm" href="{root}consult.html">Get Reading</a>
   <button class="icon-btn burger" data-menu-open aria-controls="menu" aria-expanded="false" aria-label="Open menu">☰</button>
  </div>
 </div>
</header>
"""


def ad(slot="inContent", root=""):
    return (f'<div class="ad-slot" data-slot="{slot}"><span><span class="ad-label">Advertisement</span>'
            f'This premium space is available · <a href="{root}advertise.html">Advertise / sponsor here</a></span></div>')


def newsletter_form(root, compact=False):
    return f"""<form data-lead="Newsletter — Daily Lucky Number" data-ok="You’re in! Your first lucky number arrives tomorrow.">
 <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
 <div class="{'' if compact else 'row2'}">
  <div class="field"><label for="nl-name{int(compact)}">First name</label><input id="nl-name{int(compact)}" name="name" autocomplete="given-name" required></div>
  <div class="field"><label for="nl-email{int(compact)}">Email</label><input id="nl-email{int(compact)}" name="email" type="email" autocomplete="email" required></div>
 </div>
 <div class="field"><label for="nl-z{int(compact)}">Your zodiac (optional)</label><select id="nl-z{int(compact)}" name="zodiac"><option value="">Not sure</option><option>Rat</option><option>Ox</option><option>Tiger</option><option>Rabbit</option><option>Dragon</option><option>Snake</option><option>Horse</option><option>Goat</option><option>Monkey</option><option>Rooster</option><option>Dog</option><option>Pig</option></select></div>
 <button class="btn btn-red btn-block" type="submit">Get my free daily lucky number →</button>
 <p class="form-note">Free. Unsubscribe anytime. We never sell your data — see <a href="{root}legal.html#privacy">Privacy</a>.</p>
</form>"""


def footer(root):
    return f"""
<footer class="site-footer">
 <div class="container">
  <div class="foot-grid">
   <div>
    <a class="brand" href="{root}index.html" style="color:#fff">{SEAL}<span>999910.com<small style="color:#B9AA95">久久久久 · 十全十美</small></span></a>
    <p style="margin-top:14px">Free Chinese lucky-number tools, almanac dates and culture guides — forever useful, perfect in every detail.</p>
    <p><a href="{INTEREST}" target="_blank" rel="noopener"><b>Interested in this website, domain, sponsorship, advertising or partnership? Contact →</b></a></p>
   </div>
   <div><h4>Tools</h4><ul>
    <li><a href="{root}meaning.html">Number Meaning</a></li><li><a href="{root}checker.html">Phone / Plate / House</a></li>
    <li><a href="{root}dates.html">Auspicious Dates</a></li><li><a href="{root}zodiac.html">Zodiac</a></li>
    <li><a href="{root}fengshui.html">Kua & Directions</a></li><li><a href="{root}domains.html">Numeric Domains</a></li></ul></div>
   <div><h4>Learn</h4><ul>
    <li><a href="{root}culture.html">Lucky Number Guide</a></li><li><a href="{root}numbers/index.html">Number Dictionary</a></li>
    <li><a href="{root}videos.html">Videos</a></li><li><a href="{root}methodology.html">Methodology</a></li><li><a href="{root}about.html">About</a></li></ul></div>
   <div><h4>Community</h4><ul>
    <li><a href="{root}consult.html">Get a Personal Reading</a></li><li><a href="{root}contest.html">Contest & Prizes</a></li>
    <li><a href="{root}support.html">Support / Donate</a></li><li><a href="{root}careers.html">Careers</a></li>
    <li><a href="{root}advertise.html">Advertise & Sponsor</a></li><li><a href="{root}contact.html">Contact</a></li></ul></div>
   <div><h4>Legal</h4><ul>
    <li><a href="{root}legal.html#trademark">Trademark & Copyright</a></li><li><a href="{root}legal.html#disclaimer">Disclaimer</a></li>
    <li><a href="{root}legal.html#privacy">Privacy</a></li><li><a href="{root}legal.html#cookies">Cookies</a></li>
    <li><a href="{root}legal.html#terms">Terms</a></li><li><a href="#" data-mail="Inquiry from 999910.com">Email us</a></li></ul></div>
  </div>
  <div class="legal-line">
   © <span data-year>2026</span> 999910.com. Original content and code © the site owner. “999910” is used as a domain name and numeral only; no trademark rights are claimed in the number.
   Not affiliated with, endorsed by or sponsored by China Resources Sanjiu (“999”), Nine West or any holder of “999”, “9999” or similar marks, the Palace Museum, Google, YouTube or FormSubmit.
   Cultural information is for education and entertainment — not financial, legal, medical or investment advice. <a href="{root}legal.html#trademark">Full disclosure</a>.
  </div>
 </div>
</footer>
<div class="sticky-cta">
 <button class="icon-btn to-top" aria-label="Back to top">↑</button>
 <a class="btn btn-red" href="{root}consult.html">Get my lucky report</a>
</div>
<div class="consent" role="dialog" aria-label="Cookie choices">
 <b>Cookies & ads</b> — We use cookies for ads (Google AdSense) and anonymous analytics to keep these tools free. <a href="{root}legal.html#cookies">Details</a>
 <div class="btns"><button class="btn btn-red btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div>
</div>
<div class="modal" id="exit-modal" role="dialog" aria-modal="true" aria-labelledby="exit-title">
 <div class="card">
  <button class="icon-btn x" data-close-modal aria-label="Close">✕</button>
  <span class="eyebrow">Before you go · 别走</span>
  <h3 id="exit-title">Get your lucky number every morning</h3>
  <p class="muted">Daily lucky number, colour and direction for your zodiac — free.</p>
  {newsletter_form(root, compact=True)}
 </div>
</div>
<script src="{root}assets/js/config.js?v={VERSION}"></script>
<script src="{root}assets/js/engine.js?v={VERSION}"></script>
<script src="{root}assets/js/core.js?v={VERSION}"></script>
<script src="{root}assets/js/tools.js?v={VERSION}"></script>
</body>
</html>
"""


def page(path, title, desc, body, active="", jsonld=None, root=None):
    if root is None:
        root = "../" * path.count("/")
    base = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": title.split(" | ")[0], "item": SITE + "/" + path}]}]
    return (head(title, desc, path, root, (jsonld or []) + (base if path != "index.html" else []))
            + f'<body data-root="{root}">' + header(root, active)
            + f'<main id="main">{body}</main>' + footer(root))


def page_hero(title, sub, crumb, root="", eyebrow=""):
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f"""<section class="page-hero"><div class="container">
<nav class="breadcrumb" aria-label="Breadcrumb"><a href="{root}index.html">Home</a> › {crumb}</nav>
{eb}<h1>{title}</h1><p class="lead">{sub}</p></div></section>"""


def faq_ld(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


def faq_html(pairs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs)


def app_ld(name, desc, path):
    return {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "description": desc,
            "url": SITE + "/" + path, "applicationCategory": "LifestyleApplication", "operatingSystem": "Any",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
