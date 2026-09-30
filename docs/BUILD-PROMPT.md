# 999910.com — Phase-wise Build Prompt

Reusable, copy-paste prompts to (re)build or extend 999910.com with an AI coding agent. Each phase is self-contained. Run them in order. Phases 1–7 are already implemented in this repo; phases 8–10 are the expansion roadmap.

> **Global constraints (paste at the top of every phase)**
> - Domain: **999910.com** (read "9999 10" → 久久久久 · 十全十美 → "Forever Perfect").
> - Stack: static HTML/CSS/vanilla JS only. It must run on the **GitHub Pages free plan**, so no server, no build step required at runtime, and relative links only (it is served from `/999910-com/` until the custom domain is live).
> - The **top of every page** shows: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to `https://web.works/contact`.
> - **One inbox only** for every form, stored obfuscated in `assets/js/config.js` (`_k`) and assembled at runtime. The address must **never** appear in HTML, visible text, `href`s, docs or the README. Use FormSubmit AJAX (or its random alias once activated) and a `data-mail` click-to-email link as fallback.
> - Monetization hooks: AdSense slots (config-driven), YouTube lite embeds (config-driven), donations, sponsorships, contest, lead-gen.
> - Never use "999", "9999" or any third-party mark as a brand. Use digits only as numerals, and keep the trademark/copyright disclosure on every page footer plus `/legal.html#trademark`.
> - Accessibility: WCAG AA contrast, keyboard nav, labels on every input, `prefers-reduced-motion`. Mobile-first with no horizontal scroll at 360 px. Light and dark themes.

---

## Phase 1 — Research & positioning
"Research the cultural meaning of 9, 99, 999, 9999 and 10 in Chinese culture (homophones, imperial symbolism, Double Ninth, gold purity grades, number slang) and the economics of lucky numbers (HK plate auctions, phone numbers, numeric domains, gold demand, diaspora size). Collect verifiable figures with URLs. Scan trademark risks for 999 / 9999 / 999910. Score 4+ site concepts on traffic, RPM, lead value, domain fit and build cost; choose one and justify it. Output `docs/RESEARCH.md`."

## Phase 2 — Competitive teardown (25+ sites)
"Fetch at least 25 leading sites in Chinese astrology, numerology, feng shui, China culture/travel and domain marketplaces. For each, record tools, lead forms (fields, CTA copy, placement), monetization, navigation, design and trust elements. Synthesize: top 30 features, best lead-form patterns, AdSense placement rules, IA, design direction and SEO clusters. Append the results to `docs/RESEARCH.md`."

## Phase 3 — Design system & layout shell
"Create `assets/css/style.css` with tokens:

- Colours: cinnabar #C8102E, imperial gold #C9971C, ink #1A1414, rice-paper #FAF6EE, jade #2E7D6B.
- Type: Noto Serif SC headings, Inter UI.
- Components: sticky header with mega-menu and mobile drawer, top interest bar, buttons, cards, tabs, forms (multi-step, choice pills, honeypot), score gauge (conic-gradient), seal stamps, digit chips, tables, FAQ `<details>`, lead band, ad slots, donation tiers and progress bar, video lite cards, sticky CTA, cookie consent, exit-intent modal, footer.
- Dark mode via `prefers-color-scheme` plus a `[data-theme]` toggle.

Write `tools/tpl.py` (Python) that renders `head` (SEO meta, OG, canonical, JSON-LD), `header`, `footer` and `page()`."

## Phase 4 — Engine (no dependencies)
"Write `assets/js/engine.js` exposing `window.Luck`:

- **`analyzeNumber`**: digit weights, ending multiplier, combo dictionary with nested-combo suppression, pattern bonuses, Five Elements, 0–99 score with verdicts 大吉 / 吉 / 中平 / 小凶 / 凶.
- **`suggest`**
- **Lunar conversion**: use `Intl.DateTimeFormat('en-u-ca-chinese')`.
- **Day pillar**: anchor 1949-10-01 = 甲子; verify 2000-01-01 = 戊午.
- **Twelve Day Officers** from solar-term month branches.
- **Zodiac**: Lunar New Year boundary, stem element.
- **Compatibility**: 六合 / 三合 / 六冲 / 六害.
- **Kua**: Eight Mansions with the 立春 boundary.
- **`daily()`**: lucky number, colour, 喜神 direction, clash.
- **`dateFinder(year, month, occasion, birthYear)`**
- **`domainValue`**: length bands, TLD factor, 0/4 penalties, pattern and all-lucky multipliers.

Unit-test the key dates and outputs in Node."

## Phase 5 — Core pages & tools
"Generate with `tools/build.py`:

- **Tool pages**: `index`, `meaning` (`?n=`), `checker` (phone/plate/house tabs), `dates`, `zodiac` (+ compatibility), `fengshui` (Kua), `domains` (estimator + buy/sell/lease lead form).
- **Content**: `culture` (long-form guide with TOC, FAQ schema, sources), `numbers/index` + 37 programmatic number pages, `videos`, `methodology`.
- **Community / commercial**: `consult`, `advertise`, `support`, `contest`, `careers`, `contact`, `about`, `legal`, `404`.
- **Site files**: `sitemap.xml`, `robots.txt`, `manifest`, favicon, OG image.

Every tool result shows the score UI, an ad slot directly under the result, a lead CTA pre-filled with the user's number, and share."

## Phase 6 — Lead generation, donations, contest, hiring
"Implement `assets/js/core.js`:

- **Lead forms (`[data-lead]`)**: FormSubmit AJAX with `_subject`, `_template=table`, `_replyto`, honeypot, success/error states and a mailto fallback.
- **Multi-step consult form** with validation per step and query-string prefill (`?service=&number=`).
- **Exit-intent newsletter modal**: desktop only, once per session.
- **Sticky 'Get my lucky report' CTA.**
- **Donation tiers** ($9 / $99 / $999) feeding a pledge form, a config-driven provider buttons area (Buy Me a Coffee / Ko-fi / PayPal / Stripe / GitHub Sponsors) and a goal bar.
- **Contest**: entry form with skill-testing question and official rules (18+, no purchase necessary, Canadian skill-testing requirement).
- **Careers**: role cards plus application form, with a scam warning.
- **Advertise**: formats, ideal sponsors and a media-kit request form."

## Phase 7 — Monetization wiring, compliance, QA & deploy
"Build a consent banner (Quebec Law 25 / GDPR-style) that loads AdSense (non-personalized if 'Essential only') and optional GA4 from `config.js`. Write the Privacy, Cookies and Terms policies (including Google partner-sites wording) and the trademark/copyright disclosure.

QA with Playwright at 1366 px and 390 px:

- no console errors
- no horizontal overflow
- top bar present on all pages
- the inbox address absent from every file and from the DOM

Push to `WEBWORKSA1/999910-com` on `main` and publish with GitHub Pages (`gh-pages` branch or the Pages settings)."

## Phase 8 — Growth (next)
"Add a Simplified/Traditional Chinese toggle with `hreflang` pages.

Expand programmatic pages:

- `/numbers/{n}` for all 0–999 plus the top 500 combos
- `/zodiac/{animal}/2027`
- `/dates/{occasion}/{yyyy-mm}` for 24 months

Add shareable OG result cards (canvas → PNG download). Add a festival countdown (CNY 6 Feb 2027, Double Ninth). Pre-render tool results for the top 1,000 numbers to capture long-tail search."

## Phase 9 — Revenue expansion
"Offer paid PDF reports via Stripe Payment Links, and a directory of feng shui consultants, jewellers and wedding planners (paid listings). Add affiliate modules (numeric-domain marketplaces, gold dealers, astrology apps) with disclosure. Sell sponsored-tool placements. Launch the YouTube Shorts series (one number per day) and embed it via `config.videos`."

## Phase 10 — Community & data
"Publish a public Hall of Fame for contest winners, Q&A pages generated from answered consultations (with permission), a supporter wall, and quarterly 'Lucky Number Index' reports (plate and domain auction results) for PR and backlinks."

---

### Operator checklist after deploy
1. Submit any form once on the live site, then open the FormSubmit activation email in the owner inbox and click **Activate**. Optionally paste the random alias into `config.js → formAlias`.
2. Apply for AdSense. Once approved, set `adsenseClient` and slot IDs in `config.js`, then add `ads.txt` at the root with `google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0`.
3. Add donation links, YouTube video IDs, the channel URL and GA4 in `config.js`.
4. Custom domain: add a `CNAME` file containing `999910.com` and point DNS to GitHub Pages (A records 185.199.108–111.153). Rebuild with `python3 tools/build.py --base /`, then enable HTTPS in Settings → Pages.
