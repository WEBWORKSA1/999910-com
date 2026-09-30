"""Home + interactive tool pages."""
from tpl import page, page_hero, ad, faq_html, faq_ld, app_ld, newsletter_form, INTEREST

SERVICES = [
    ("number", "Lucky phone / plate / house number"),
    ("business", "Business or brand number & name"),
    ("dates", "Auspicious date (wedding, move, opening)"),
    ("domain", "Numeric domain — buy, sell or value"),
    ("fengshui", "Feng shui Kua & home layout"),
    ("other", "Something else"),
]


def quick_lead(root, title="Get your personal lucky-number report", cta="Send my request →"):
    opts = "".join(f'<option value="{k}" data-prefill-opt>{v}</option>' for k, v in SERVICES)
    return f"""<div class="lead-band">
 <div>
  <span class="eyebrow" style="background:rgba(255,255,255,.15);color:#FFE8A8">Personal consultation · 专属咨询</span>
  <h2>{title}</h2>
  <p>A human-checked analysis of the numbers and dates that matter most to you — with better alternatives you can actually use.</p>
  <ul><li>Phone, plate, house or business numbers scored & improved</li><li>Wedding, move-in and opening dates matched to your zodiac</li><li>Numeric domain valuations, buyer outreach & brokering</li><li>Free quick check reply within 48 hours</li></ul>
 </div>
 <div class="card">
  <form data-lead="Quick Consultation Request" data-ok="Received! Your free quick check will arrive within 48 hours.">
   <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
   <div class="field"><label for="ql-s">I need help with</label><select id="ql-s" name="service" data-prefill="service">{opts}</select></div>
   <div class="field"><label for="ql-n">Number, date or domain</label><input id="ql-n" name="number" data-prefill="number" placeholder="e.g. 416 888 1688 or 2027-05-20"></div>
   <div class="row2">
    <div class="field"><label for="ql-name">Name</label><input id="ql-name" name="name" required autocomplete="name"></div>
    <div class="field"><label for="ql-e">Email</label><input id="ql-e" name="email" type="email" required autocomplete="email"></div>
   </div>
   <button class="btn btn-red btn-block" type="submit">{cta}</button>
   <p class="form-note">No spam. Your details go only to our consultants. <a href="{root}legal.html#privacy">Privacy</a></p>
  </form>
 </div>
</div>"""


POPULAR = [("8", "Prosperity"), ("9", "Forever"), ("6", "Smooth"), ("4", "Avoid"), ("168", "Prosper all the way"),
           ("520", "I love you"), ("1314", "Lifetime"), ("518", "I will prosper"), ("888", "Triple wealth"),
           ("999", "Eternal"), ("9999", "Forever & ever"), ("999910", "Forever perfect"), ("666", "Awesome"),
           ("88", "Double fortune"), ("250", "Fool (avoid)"), ("5201314", "Love for life")]

HOME_FAQ = [
    ("What does 999910 mean in Chinese?", "Read as 9999 + 10: 九 (jiǔ) sounds like 久 ‘long-lasting’, so 9999 = 久久久久 ‘forever and ever’, and 10 (十) evokes the idiom 十全十美 ‘perfect in every way’. Together: ‘forever perfect’. This is a cultural reading of the digits, not an established set phrase."),
    ("Which numbers are luckiest in Chinese culture?", "8 (发 prosperity), 9 (久 longevity) and 6 (顺 smooth) are the most sought after; 2 (pairs) and 168/518/888 combinations are popular in business. 4 sounds like 死 ‘death’ and is widely avoided."),
    ("Are the tools free?", "Yes. Every calculator on 999910.com is free and runs in your browser. We are funded by advertising, sponsors, optional personal reports and supporter donations."),
    ("How accurate is the lucky number score?", "It is a transparent cultural score based on homophones, famous combinations, digit position and patterns — see our Methodology page. It is for education and entertainment, not a guarantee."),
    ("Can I get a personal reading?", "Yes — request a personal report for your phone, plate, house or business number, auspicious dates, feng shui directions or a numeric domain. The first quick check is free."),
]


def home():
    root = ""
    pop = "".join(f'<a href="numbers/{n}.html">{n}<small>{m}</small></a>' for n, m in POPULAR)
    tools = [
        ("8", "Number Meaning", "Decode any number from 0 to 99,999,999 — homophones, combos and a 0–99 luck score.", "meaning.html"),
        ("☎", "Lucky Phone Checker", "Score your mobile number and get luckier endings before you pick one.", "checker.html#phone"),
        ("車", "Licence Plate Checker", "Check a plate the way Hong Kong, Singapore & Malaysia buyers do.", "checker.html#plate"),
        ("宅", "House Number", "Is your address, unit or floor auspicious? Avoid the hidden 4s.", "checker.html#house"),
        ("吉", "Auspicious Dates", "Wedding, move-in, opening and signing dates from the Chinese almanac.", "dates.html"),
        ("龙", "Zodiac & Compatibility", "Lunar-accurate zodiac, element, lucky numbers and best matches.", "zodiac.html"),
        ("卦", "Kua & Feng Shui", "Your Kua number and four lucky directions for desk, bed and door.", "fengshui.html"),
        (".com", "Numeric Domain Value", "Indicative value bands for NN, NNN, 4N, 5N and 6N domains.", "domains.html"),
    ]
    tgrid = "".join(f'<a class="card" href="{h}"><div class="tool-ico">{i}</div><h3>{t}</h3><p>{d}</p><span class="tag">Free tool</span></a>' for i, t, d, h in tools)
    body = f"""
<section class="hero"><div class="container hero-grid">
 <div>
  <span class="eyebrow">久久久久 · 十全十美 — Forever & Perfect</span>
  <h1>Find the numbers that bring you <span style="color:var(--red)">luck</span>, love & prosperity</h1>
  <p class="lead">Free Chinese lucky-number tools, a living number dictionary and almanac-based date finder — trusted guidance for phone numbers, plates, addresses, weddings, business launches and numeric domains.</p>
  <form class="searchbar" data-numsearch action="meaning.html" role="search">
   <label for="hero-n" class="sr">Enter any number</label>
   <input id="hero-n" inputmode="numeric" placeholder="Type any number… e.g. 168, 520, 13888888" aria-label="Enter any number">
   <button class="btn btn-red" type="submit">Decode</button>
  </form>
  <div class="flex">{''.join(f'<a class="pill" href="meaning.html?n={n}">{n}</a>' for n in ["8","168","520","1314","888","9999","999910"])}</div>
  <div class="trust"><span><b>9</b> free tools</span><span><b>40+</b> number combos explained</span><span><b>Almanac</b>-based dates</span><span><b>0</b> sign-up needed</span></div>
 </div>
 <div class="hero-card">
  <div class="muted" style="font-weight:700;letter-spacing:.12em;font-size:.8rem">THE NUMBER BEHIND THIS SITE</div>
  <div class="bignum">9999&nbsp;10</div>
  <div class="hanzi" style="font-size:1.6rem;font-weight:800">久久久久 · 十全十美</div>
  <p class="muted" style="margin-top:8px">Four nines for <b>forever</b> — the imperial number, the purity of “four-nines” gold — and a ten for <b>perfection</b>.</p>
  <div class="row"><span class="pill">九 jiǔ = 久 lasting</span><span class="pill">十 shí = complete</span><span class="pill">Score 99/99</span></div>
  <a class="btn btn-gold mt2" href="culture.html">Decode 999910 →</a>
 </div>
</div></section>

<section style="padding-top:10px"><div class="container">
 <div class="section-head"><div><h2>Today’s luck at a glance</h2><p>Generated from the traditional Chinese almanac (黄历) for today’s date.</p></div><a class="btn btn-ghost btn-sm" href="dates.html">Find a lucky date →</a></div>
 <div class="daily" data-daily></div>
</div></section>
{ad("top")}
<section class="section-alt"><div class="container">
 <div class="section-head"><div><h2>Free lucky-number tools</h2><p>Everything runs instantly in your browser — no sign-up, no data stored.</p></div></div>
 <div class="grid g4">{tgrid}</div>
</div></section>

<section><div class="container grid g2" style="align-items:start">
 <div class="card">
  <span class="tag red">Most popular</span>
  <h2 style="margin-top:8px">Is your phone number lucky?</h2>
  <p class="muted">Paste any mobile, landline or WhatsApp number. We score every digit, famous combinations and the all-important ending.</p>
  <form data-tool="phone" data-out="home-phone-out" class="searchbar" style="margin:0">
   <label for="home-phone" class="sr">Phone number</label>
   <input id="home-phone" inputmode="tel" placeholder="+1 514 888 1688" required>
   <button class="btn btn-red" type="submit">Check</button>
  </form>
 </div>
 <div>
  <h2>Why numbers are worth millions</h2>
  <div class="grid g2">
   <div class="card"><div class="kpi">HK$26M</div><p>Paid for the single-letter plate “W” at a 2021 Hong Kong auction — its record.</p></div>
   <div class="card"><div class="kpi">¥2.33M</div><p>Paid by Sichuan Airlines in 2003 for the phone number 8888-8888.</p></div>
   <div class="card"><div class="kpi">6,106</div><p>Couples married in Guangzhou on 9/9/2009 — a one-day record since 1949.</p></div>
   <div class="card"><div class="kpi">1,003 t</div><p>China’s gold demand in 2025, much of it “999” and “9999” fine gold.</p></div>
  </div>
  <p class="form-note">Sources on our <a href="culture.html#sources">culture guide</a>.</p>
 </div>
</div>
<div class="container"><div class="result" id="home-phone-out"></div></div></section>

<section><div class="container">{quick_lead(root)}</div></section>
{ad("inContent")}
<section class="section-alt"><div class="container">
 <div class="section-head"><div><h2>Number dictionary</h2><p>Tap a number to see its meaning, score and where it is used.</p></div><a class="btn btn-ghost btn-sm" href="numbers/index.html">All numbers →</a></div>
 <div class="num-grid">{pop}</div>
</div></section>

<section><div class="container">
 <div class="section-head"><div><h2>Watch & learn</h2><p>Short videos on lucky numbers, zodiac and feng shui.</p></div><a class="btn btn-ghost btn-sm" href="videos.html">Video hub →</a></div>
 <div class="grid g3" data-videos>
  <a class="card vcard" href="https://www.youtube.com/results?search_query=chinese+lucky+numbers+meaning" target="_blank" rel="noopener"><div class="vthumb">8 · 9 · 6</div><h3>Chinese lucky numbers explained</h3></a>
  <a class="card vcard" href="https://www.youtube.com/results?search_query=double+ninth+festival+chongyang" target="_blank" rel="noopener"><div class="vthumb">重阳</div><h3>Double Ninth Festival</h3></a>
  <a class="card vcard" href="https://www.youtube.com/results?search_query=hong+kong+number+plate+auction" target="_blank" rel="noopener"><div class="vthumb">HK$</div><h3>Hong Kong number-plate auctions</h3></a>
 </div>
</div></section>

<section class="section-alt"><div class="container">
 <div class="section-head"><div><h2>Join the 999910 community</h2><p>Win prizes, support free tools, sponsor the site or work with us.</p></div></div>
 <div class="grid g4">
  <a class="card" href="contest.html"><span class="tag gold">Win</span><h3 style="margin-top:8px">Monthly contest</h3><p><span data-contest="title">Luckiest Number of the Month</span> — prize: <span data-contest="prize">prize pool</span>.</p></a>
  <a class="card" href="support.html"><span class="tag red">Support</span><h3 style="margin-top:8px">Keep the tools free</h3><p>Become a “Lucky Nine” supporter from $9. Funds operations, marketing, talent and prizes.</p></a>
  <a class="card" href="advertise.html"><span class="tag">Sponsor</span><h3 style="margin-top:8px">Advertise with us</h3><p>Sponsored tools, homepage placements, newsletter and contest sponsorship.</p></a>
  <a class="card" href="careers.html"><span class="tag">Hiring</span><h3 style="margin-top:8px">Careers</h3><p>Writers, consultants, video editors and growth talent — remote and flexible.</p></a>
 </div>
</div></section>

<section><div class="container grid g2" style="align-items:start">
 <div><h2>Questions, answered</h2>{faq_html(HOME_FAQ)}</div>
 <div class="card"><span class="eyebrow">Daily email · 每日好运</span><h2>Your lucky number, every morning</h2><p class="muted">Lucky number, colour and direction for your zodiac, plus the day’s almanac. Takes 10 seconds to join.</p>{newsletter_form(root)}</div>
</div></section>
<section style="padding-top:0"><div class="container"><div class="callout"><b>Own a business, domain portfolio or media brand?</b> This website and the domain <b>999910.com</b> are open to sponsorship, advertising, partnership or acquisition. <a href="{INTEREST}" target="_blank" rel="noopener">Contact us →</a></div></div></section>
"""
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "999910.com", "url": "https://999910.com/",
           "potentialAction": {"@type": "SearchAction", "target": "https://999910.com/meaning.html?n={number}", "query-input": "required name=number"}},
          {"@context": "https://schema.org", "@type": "Organization", "name": "999910.com", "url": "https://999910.com/", "logo": "https://999910.com/assets/img/favicon.svg"},
          faq_ld(HOME_FAQ)]
    return page("index.html", "999910.com — Chinese Lucky Numbers, Meanings, Dates & Tools | Forever Perfect",
                "Free Chinese lucky number tools: number meanings, lucky phone & licence plate checker, auspicious wedding dates, zodiac, Kua feng shui and numeric domain values.",
                body, jsonld=ld)


def meaning():
    root = ""
    body = page_hero('<span id="meaning-title">What does this number mean in Chinese?</span>',
                     "Type any number to see each digit’s homophone, the famous combinations inside it, its pattern, Five-Element mix and a 0–99 cultural luck score.",
                     "Number Meanings", root, "Number meaning lookup · 数字含义")
    body += f"""<section style="padding-top:10px"><div class="container layout-side">
 <div>
  <form class="searchbar" data-numsearch action="meaning.html" role="search" style="max-width:none">
   <label for="meaning-input" class="sr">Number</label><input id="meaning-input" inputmode="numeric" placeholder="Any number, e.g. 5201314">
   <button class="btn btn-red" type="submit">Decode</button></form>
  <div class="result" id="meaning-out"></div>
  {ad("inContent")}
  <h2>The ten digits at a glance</h2>
  <div class="table-wrap"><table><tr><th>Digit</th><th>Chinese</th><th>Sounds like</th><th>Reputation</th></tr>
  <tr><td>0</td><td>零 líng</td><td>—</td><td>Neutral · wholeness</td></tr>
  <tr><td>1</td><td>一 yī</td><td>要 “will”</td><td>Mildly positive</td></tr>
  <tr><td>2</td><td>二 èr</td><td>易 “easy” (Cantonese)</td><td>Positive · pairs</td></tr>
  <tr><td>3</td><td>三 sān</td><td>生 “life” (Cantonese)</td><td>Mixed-positive</td></tr>
  <tr><td>4</td><td>四 sì</td><td>死 “death”</td><td><b style="color:var(--red)">Avoided</b></td></tr>
  <tr><td>5</td><td>五 wǔ</td><td>我 “me” / 无 “none”</td><td>Neutral</td></tr>
  <tr><td>6</td><td>六 liù</td><td>溜 “smooth”</td><td>Lucky</td></tr>
  <tr><td>7</td><td>七 qī</td><td>起 “arise” / 气 “anger”</td><td>Mixed</td></tr>
  <tr><td>8</td><td>八 bā</td><td>发 “prosper”</td><td><b style="color:var(--jade)">Luckiest for wealth</b></td></tr>
  <tr><td>9</td><td>九 jiǔ</td><td>久 “long-lasting”</td><td><b style="color:var(--jade)">Imperial · eternal</b></td></tr></table></div>
  <p class="mt2"><a href="numbers/index.html">Browse the full number dictionary →</a></p>
 </div>
 <aside><div class="side-sticky">
  <div class="card"><h3>Need a luckier number?</h3><p class="muted">We’ll suggest better phone numbers, plates or business numbers — and where to get them.</p><a class="btn btn-red btn-block" href="consult.html?service=number">Get my report</a></div>
  {ad("sidebar")}
 </div></aside>
</div></section>"""
    return page("meaning.html", "Chinese Number Meaning Lookup — Decode Any Number | 999910.com",
                "Decode any number in Chinese: digit homophones, lucky combinations like 168, 520, 1314 and 888, patterns, Five Elements and a 0–99 luck score.",
                body, active="meaning.html", jsonld=[app_ld("Chinese Number Meaning Lookup", "Decode any number in Chinese culture", "meaning.html")])


def checker():
    root = ""
    def panel(pid, label, ph, im, note, active=False):
        return f"""<div class="panel{' active' if active else ''}" id="p-{pid}" role="tabpanel">
  <form data-tool="{pid}" data-out="out-{pid}" class="searchbar" style="max-width:none">
   <label for="in-{pid}" class="sr">{label}</label><input id="in-{pid}" inputmode="{im}" placeholder="{ph}" required>
   <button class="btn btn-red" type="submit">Check</button></form>
  <p class="muted">{note}</p>
  <div class="result" id="out-{pid}"></div></div>"""
    body = page_hero("Lucky Phone, Licence Plate & House Number Checker",
                     "Score any phone number, car plate, house, unit or floor number the way Chinese buyers do — then get luckier alternatives.",
                     "Lucky Checkers", root, "Free checker · 号码吉凶")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><div>
 <div class="tabs" data-tabs role="tablist">
  <button role="tab" id="phone" aria-controls="p-phone" aria-selected="true">Phone number</button>
  <button role="tab" id="plate" aria-controls="p-plate" aria-selected="false">Licence plate</button>
  <button role="tab" id="house" aria-controls="p-house" aria-selected="false">House / unit / floor</button>
 </div>
 {panel("phone", "Phone number", "+1 514 888 1688", "tel", "Tip: the last 4 digits carry the most weight. Endings like 88, 68, 99, 168 and 518 are prized; 14, 24, 54 and 74 are avoided.", True)}
 {panel("plate", "Plate number", "e.g. 8TK 888 or 9999", "text", "Letters are ignored — only digits are scored. In Hong Kong, plates like 18, 28 and 9 have sold for HK$13M–18M.")}
 {panel("house", "House number", "e.g. 1688 or Unit 2808", "text", "Many buildings skip floors 4, 13, 14 and 24. A 4 inside the number lowers the score; 8 and 9 raise it.")}
 {ad("inContent")}
 <h2>How to choose a lucky number — 5 rules</h2>
 <ol><li><b>Protect the ending.</b> The final two to four digits are what people remember and repeat.</li>
 <li><b>Avoid 4 next to 1, 2, 5 or 7</b> — 14, 24, 54, 74 read as phrases about death or anger.</li>
 <li><b>Stack prosperity:</b> 8, 88, 168, 518, 1688, 6688 are the business favourites.</li>
 <li><b>Choose longevity for relationships:</b> 9, 99, 520, 1314 and 5201314 are the romantic set.</li>
 <li><b>Patterns sell:</b> AAAA, ABAB and AABB numbers are easier to remember and resell.</li></ol>
</div>
<aside><div class="side-sticky">
 <div class="card"><h3>Buy a luckier number</h3><p class="muted">We help you find, negotiate and transfer premium numbers and plates.</p><a class="btn btn-red btn-block" href="consult.html?service=number">Request help</a></div>
 {ad("sidebar")}
</div></aside></div></section>
<section><div class="container">{quick_lead(root, "Want a professionally chosen number?")}</div></section>"""
    faq = [("What is the luckiest phone number ending?", "Endings with 8 and 9 — 88, 68, 98, 168, 518, 888 and 999 — are the most prized. Avoid 14, 24, 54 and 74."),
           ("Does the country code matter?", "Traditionally only the digits people see and say count, so focus on the local number and especially the ending.")]
    return page("checker.html", "Lucky Phone Number, Licence Plate & House Number Checker | 999910.com",
                "Free Chinese lucky phone number checker and licence plate / house number scorer. See every digit’s meaning, lucky combos and better alternatives.",
                body + f'<section><div class="container article">{faq_html(faq)}</div></section>',
                jsonld=[app_ld("Lucky Phone Number Checker", "Chinese lucky phone, plate and house number scoring", "checker.html"), faq_ld(faq)])


def dates():
    root = ""
    body = page_hero("Auspicious Date Finder — Chinese Almanac 黄历",
                     "Pick an occasion and month. We rank every day using the Twelve Day Officers (建除十二神), the day’s stem-branch, Ghost Month, unlucky digits and your zodiac clash.",
                     "Auspicious Dates", root, "Wedding · Move-in · Opening · Signing · Travel")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><div>
 <form id="dates-form" class="card">
  <div class="row2">
   <div class="field"><label for="d-occ">Occasion</label><select id="d-occ" name="occasion">
    <option value="wedding">Wedding / marriage registration</option><option value="move">Moving house</option>
    <option value="opening">Business opening / launch</option><option value="signing">Signing a contract</option><option value="travel">Travel</option></select></div>
   <div class="field"><label for="d-m">Month</label><input id="d-m" name="month" type="month" required></div>
  </div>
  <div class="field"><label for="d-by">Your birth year (optional — avoids clash days)</label><input id="d-by" name="birthyear" type="number" min="1900" max="2030" placeholder="e.g. 1990"></div>
  <button class="btn btn-red" type="submit">Find lucky dates</button>
  <p class="form-note">Solar-term boundaries are approximated (±1 day). For weddings, confirm with a family elder or a professional almanac reading.</p>
 </form>
 <div class="result" id="dates-out"></div>
 {ad("inContent")}
 <h2>How we rank dates</h2>
 <p>Each day in the Chinese almanac has a “day officer”. <b>成 Success</b>, <b>定 Stable</b> and <b>开 Open</b> days are favoured for weddings and launches; <b>破 Destruction</b> and <b>闭 Close</b> days are avoided. We also down-rank the 7th lunar month (“Ghost Month”), dates containing 4, and any day whose earthly branch clashes with your zodiac sign.</p>
 <p><a href="methodology.html#dates">Read the full methodology →</a></p>
</div>
<aside><div class="side-sticky">
 <div class="card"><h3>Planning a wedding?</h3><p class="muted">Get a hand-picked shortlist of dates matched to both partners’ birth data.</p><a class="btn btn-red btn-block" href="consult.html?service=dates">Get my dates</a></div>
 {ad("sidebar")}
</div></aside></div></section>"""
    return page("dates.html", "Auspicious Date Finder — Lucky Wedding, Moving & Opening Dates | 999910.com",
                "Find auspicious wedding, moving, business opening and signing dates with the Chinese almanac: day officers, stem-branch, Ghost Month and zodiac clashes.",
                body, jsonld=[app_ld("Auspicious Date Finder", "Chinese almanac lucky date finder", "dates.html")])


def zodiac():
    root = ""
    body = page_hero("Chinese Zodiac Finder & Compatibility",
                     "Lunar-accurate: born in January or early February? We use the actual Lunar New Year date, not just the calendar year.",
                     "Zodiac", root, "生肖 · 2026 Year of the Fire Horse")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><div>
 <form id="zodiac-form" class="card"><div class="field"><label for="z-dob">Date of birth</label><input id="z-dob" name="dob" type="date" required min="1901-01-01" max="2099-12-31"></div>
  <button class="btn btn-red" type="submit">Find my zodiac</button></form>
 <div class="result" id="zodiac-out"></div>
 {ad("inContent")}
 <h2 id="compat">Zodiac compatibility</h2>
 <form id="compat-form" class="card"><div class="row2">
  <div class="field"><label for="c-a">Your sign</label><select id="c-a" name="a"></select></div>
  <div class="field"><label for="c-b">Their sign</label><select id="c-b" name="b"></select></div></div>
  <button class="btn btn-red" type="submit">Check compatibility</button></form>
 <div class="result" id="compat-out"></div>
 <h2 class="mt2">Lucky numbers by zodiac</h2>
 <div class="table-wrap"><table><tr><th>Sign</th><th>Recent years</th><th>Lucky numbers</th></tr>
 <tr><td>鼠 Rat</td><td>1984, 1996, 2008, 2020</td><td>2, 3</td></tr><tr><td>牛 Ox</td><td>1985, 1997, 2009, 2021</td><td>1, 4</td></tr>
 <tr><td>虎 Tiger</td><td>1986, 1998, 2010, 2022</td><td>1, 3, 4</td></tr><tr><td>兔 Rabbit</td><td>1987, 1999, 2011, 2023</td><td>3, 4, 6</td></tr>
 <tr><td>龙 Dragon</td><td>1988, 2000, 2012, 2024</td><td>1, 6, 7</td></tr><tr><td>蛇 Snake</td><td>1989, 2001, 2013, 2025</td><td>2, 8, 9</td></tr>
 <tr><td>马 Horse</td><td>1990, 2002, 2014, 2026</td><td>2, 3, 7</td></tr><tr><td>羊 Goat</td><td>1991, 2003, 2015, 2027</td><td>3, 4, 9</td></tr>
 <tr><td>猴 Monkey</td><td>1992, 2004, 2016</td><td>4, 9</td></tr><tr><td>鸡 Rooster</td><td>1993, 2005, 2017</td><td>5, 7, 8</td></tr>
 <tr><td>狗 Dog</td><td>1994, 2006, 2018</td><td>3, 4, 9</td></tr><tr><td>猪 Pig</td><td>1995, 2007, 2019</td><td>2, 5, 8</td></tr></table></div>
 <p class="form-note">Years start at Lunar New Year (e.g. 2026 Fire Horse begins 17 Feb 2026; 2027 Fire Goat begins 6 Feb 2027). Lucky-number sets follow popular almanac sources and vary between schools.</p>
</div>
<aside><div class="side-sticky"><div class="card"><h3>2027 personal forecast</h3><p class="muted">Get a personal year-ahead reading for your sign and element.</p><a class="btn btn-red btn-block" href="consult.html?service=other">Request forecast</a></div>{ad("sidebar")}</div></aside>
</div></section>"""
    return page("zodiac.html", "Chinese Zodiac Calculator, Compatibility & Lucky Numbers | 999910.com",
                "Lunar-accurate Chinese zodiac calculator with element, stem-branch, lucky numbers and compatibility (Six Harmony, Triple Harmony, Clash).",
                body, jsonld=[app_ld("Chinese Zodiac Calculator", "Lunar-accurate zodiac and compatibility", "zodiac.html")])


def fengshui():
    root = ""
    body = page_hero("Kua Number Calculator & Lucky Directions",
                     "Find your Kua (Gua) number and your four favourable directions for wealth, health, love and growth — then arrange your desk, bed and door.",
                     "Feng Shui", root, "Eight Mansions · 八宅风水")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><div>
 <form id="kua-form" class="card"><div class="row2">
  <div class="field"><label for="k-dob">Date of birth</label><input id="k-dob" name="dob" type="date" required></div>
  <div class="field"><label for="k-g">Gender (traditional formula)</label><select id="k-g" name="gender"><option value="f">Female</option><option value="m">Male</option></select></div></div>
  <button class="btn btn-red" type="submit">Calculate my Kua</button></form>
 <div class="result" id="kua-out"></div>
 {ad("inContent")}
 <h2>Feng shui and numbers</h2>
 <p>In the Lo Shu magic square each number 1–9 sits in a direction; every row, column and diagonal adds to 15. The Eight Mansions school turns your birth year into a Kua number that belongs to the East group (1, 3, 4, 9) or West group (2, 6, 7, 8).</p>
 <div class="grid g3" style="max-width:360px;text-align:center;font-family:var(--serif);font-size:1.6rem;font-weight:800;gap:6px">
  <div class="card">4</div><div class="card">9</div><div class="card">2</div><div class="card">3</div><div class="card">5</div><div class="card">7</div><div class="card">8</div><div class="card">1</div><div class="card">6</div></div>
 <p class="form-note">Lo Shu square (south at top, as in traditional charts).</p>
 <h2>Quick number tips for your home</h2>
 <ul><li>A 4 in your address can be “balanced” with an 8 or 9 elsewhere — many owners add a unit letter or ½ rather than change numbers.</li>
 <li>Floors 8, 9, 18, 28, 38 and 88 often sell at a premium in Chinese-majority markets; floors 4, 14 and 24 at a discount.</li>
 <li>Face your wealth (Sheng Qi) direction when you work or negotiate.</li></ul>
</div>
<aside><div class="side-sticky"><div class="card"><h3>Home or office audit</h3><p class="muted">Send a floor plan — get a numbers + directions action list.</p><a class="btn btn-red btn-block" href="consult.html?service=fengshui">Book an audit</a></div>{ad("sidebar")}</div></aside>
</div></section>"""
    return page("fengshui.html", "Kua Number Calculator & Feng Shui Lucky Directions | 999910.com",
                "Free Kua number calculator: find your East/West group and four lucky feng shui directions for wealth, health, love and personal growth.",
                body, jsonld=[app_ld("Kua Number Calculator", "Feng shui Kua number and lucky directions", "fengshui.html")])


def domains():
    root = ""
    body = page_hero("Numeric Domain Value Indicator",
                     "Chinese investors pay premiums for short numeric .com domains. Get an indicative value band for NN, NNN, 4N, 5N and 6N names — and talk to us about buying, selling or leasing.",
                     "Numeric Domains", root, "数字域名 · Numeric .com")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><div>
 <form id="domain-form" class="searchbar" style="max-width:none"><label for="dm" class="sr">Domain</label><input id="dm" name="domain" placeholder="e.g. 168168.com" required><button class="btn btn-red" type="submit">Estimate</button></form>
 <div class="result" id="domain-out"></div>
 {ad("inContent")}
 <h2>What drives numeric domain prices</h2>
 <div class="table-wrap"><table><tr><th>Class</th><th>Public comparable sales</th><th>Notes</th></tr>
 <tr><td>NN.com</td><td>55.com $2.3M (2011); 37.com $1.96M (2014)</td><td>Only 100 exist; Chinese owners held ~59</td></tr>
 <tr><td>NNN.com</td><td>114.com $2.1M (2013); 345.com $800K (2015)</td><td>1,000 exist; Chinese owners held ~480</td></tr>
 <tr><td>5N.com</td><td>88888.com $245K</td><td>Patterns and all-8/9 names dominate</td></tr>
 <tr><td>6N.com</td><td>2016: $160–180 random; $200–1,000+ patterned</td><td>Investors favour the 262,144 names with no 0 or 4</td></tr></table></div>
 <p class="form-note">Figures reported by Media Options and NamePros; see sources on the <a href="culture.html#sources">culture guide</a>. Values change — the tool gives indicative bands only, not an appraisal.</p>
</div>
<aside><div class="side-sticky"><div class="card"><h3>Own this domain?</h3><p class="muted">999910.com itself is open to partnership or acquisition.</p><a class="btn btn-gold btn-block" href="{INTEREST}" target="_blank" rel="noopener">Contact the owner</a></div>{ad("sidebar")}</div></aside>
</div></section>
<section id="domain-lead" class="section-alt"><div class="container grid g2" style="align-items:start">
 <div><h2>Buy, sell, lease or value a numeric domain</h2><p class="muted">Tell us what you have or want. We reply with comparable sales, realistic pricing and a plan — buyer outreach, brokerage or lease-to-own.</p>
 <ul><li>Portfolio reviews for 3N–6N numeric .com and .cn names</li><li>Chinese-market buyer outreach</li><li>Escrow-protected transactions via established platforms</li></ul></div>
 <div class="card"><form data-lead="Numeric Domain Inquiry" data-ok="Thanks — we’ll send comparables and next steps shortly.">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="field"><span class="sr">Intent</span><div class="choice"><label><input type="radio" name="intent" value="Sell" checked>Sell</label><label><input type="radio" name="intent" value="Buy">Buy</label><label><input type="radio" name="intent" value="Lease">Lease</label><label><input type="radio" name="intent" value="Valuation">Valuation</label></div></div>
  <div class="field"><label for="dl-d">Domain(s)</label><input id="dl-d" name="domain" placeholder="e.g. 168168.com" required></div>
  <div class="row2"><div class="field"><label for="dl-p">Target price / budget (USD)</label><input id="dl-p" name="price" inputmode="numeric"></div>
  <div class="field"><label for="dl-t">Timeline</label><select id="dl-t" name="timeline"><option>Flexible</option><option>Within 30 days</option><option>Within 90 days</option></select></div></div>
  <div class="row2"><div class="field"><label for="dl-n">Name</label><input id="dl-n" name="name" required></div><div class="field"><label for="dl-e">Email</label><input id="dl-e" name="email" type="email" required></div></div>
  <button class="btn btn-red btn-block" type="submit">Send inquiry →</button></form></div>
</div></section>"""
    return page("domains.html", "Numeric Domain Value Estimator — NNN, 4N, 5N, 6N .com | 999910.com",
                "Estimate numeric domain value bands for NN, NNN, 4N, 5N and 6N .com names, see why Chinese buyers pay premiums, and buy, sell or lease numeric domains.",
                body, jsonld=[app_ld("Numeric Domain Value Indicator", "Indicative numeric domain valuation", "domains.html")])
