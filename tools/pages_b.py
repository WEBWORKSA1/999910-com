"""Content, community, lead-gen and legal pages."""
from tpl import page, page_hero, ad, faq_html, faq_ld, newsletter_form, INTEREST, SITE
from pages_a import quick_lead, SERVICES

SOURCES = [
    ("Wikipedia — 9 (number)", "https://en.wikipedia.org/wiki/9"),
    ("TravelChinaGuide — Lucky Number 9", "https://www.travelchinaguide.com/intro/lucky-number9.htm"),
    ("TravelChinaGuide — Rooms in the Forbidden City", "https://www.travelchinaguide.com/attraction/beijing/how-many-rooms-in-forbidden-city.htm"),
    ("Wikipedia — Double Ninth Festival", "https://en.wikipedia.org/wiki/Double_Ninth_Festival"),
    ("LTL Mandarin School — Lucky numbers in Chinese", "https://ltl-school.com/lucky-numbers-chinese/"),
    ("China Highlights — Lucky Number 8", "https://www.chinahighlights.com/travelguide/culture/lucky-number-8.htm"),
    ("ChinesePod — 十全十美", "https://www.chinesepod.com/dictionary/%E5%8D%81%E5%85%A8%E5%8D%81%E7%BE%8E"),
    ("China Daily (2009) — 9/9/2009 wedding rush", "https://www.chinadaily.com.cn/china/2009-09/09/content_8673413.htm"),
    ("China Daily (2003) — 8888-8888 phone number", "https://www.chinadaily.com.cn/en/doc/2003-08/19/content_256178.htm"),
    ("CNN — Hong Kong vanity plate auctions", "https://www.cnn.com/style/article/hong-kong-auctioned-vanity-car-plates-intl-hnk/index.html"),
    ("Kwiksure — Top-priced car plates in Hong Kong", "https://www.kwiksure.com/blog/top-priced-car-plate-number-hong-kong/"),
    ("Wikipedia — 2008 Olympics opening ceremony", "https://en.wikipedia.org/wiki/2008_Summer_Olympics_opening_ceremony"),
    ("Wikipedia — Tetraphobia", "https://en.wikipedia.org/wiki/Tetraphobia"),
    ("Media Options — Numeric domain value in Chinese culture", "https://mediaoptions.com/blog/understanding-numeric-domain-value-in-chinese-culture/"),
    ("NamePros — Chinese investors and numeric domains", "https://www.namepros.com/blog/domain-data-chinese-investors-and-numeric-domains.873715/"),
    ("NamePros — Should you buy 6N .coms?", "https://www.namepros.com/blog/should-you-buy-6n-coms-a-guide-to-this-rapidly-expanding-market.916489/"),
    ("China Daily (2026) — China gold demand 2025", "https://www.chinadaily.com.cn/a/202601/30/WS697c2506a310d6866eb369cc.html"),
    ("World Gold Council — Gold Demand Trends FY2025", "https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025"),
    ("Wikipedia — Overseas Chinese", "https://en.wikipedia.org/wiki/Overseas_Chinese"),
    ("Hong Kong Observatory — Gregorian–Lunar conversion", "https://www.hko.gov.hk/en/gts/time/conversion.htm"),
    ("Travel of China — Chinese number slang", "https://www.travelofchina.com/chinese-number-slang/"),
]

CULTURE_FAQ = [
    ("Is 999910 a traditional Chinese phrase?", "No. It is a modern reading of familiar symbols — 9999 (久久久久, forever) and 10 (十全十美, perfection). We present it as a cultural interpretation, not an established idiom."),
    ("Why is 9 linked to the emperor?", "Nine is the highest single-digit yang number. Imperial China used it everywhere — nine-dragon robes, nine grades of officials, 81 (9×9) golden doornails on palace gates — and the emperor was called 九五之尊, ‘the honoured one of nine and five’."),
    ("What is ‘four-nines’ gold?", "Gold of 99.99% purity, called 万足金 in Chinese and marked 9999. ‘Three-nines’ (999, 千足金) is the Hong Kong retail standard; 足金 means at least 99.0%."),
    ("Why do people avoid the number 4?", "四 (sì) sounds like 死 (sǐ, death). Many buildings in Chinese-majority cities skip floors 4, 14 and 24, and some skip the entire 40s."),
]


def culture():
    root = ""
    src = "".join(f'<li><a href="{u}" target="_blank" rel="noopener nofollow">{t}</a></li>' for t, u in SOURCES)
    body = page_hero("999910 Decoded: Nine, Ten & the Chinese Economy of Luck",
                     "Why four nines mean ‘forever’, why ten means ‘perfect’, and how lucky numbers move real money — from HK$26 million plates to million-dollar numeric domains.",
                     "Culture Guide", root, "Culture guide · 文化")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><article class="article">
<p class="byline">By the 999910.com editorial team · Updated 30 September 2026 · 12-minute read</p>
<div class="toc"><b>Contents</b><ol>
<li><a href="#decode">Reading 999910</a></li><li><a href="#nine">Nine: the imperial, eternal number</a></li><li><a href="#ten">Ten: 十全十美</a></li>
<li><a href="#gold">9999: “four-nines” gold</a></li><li><a href="#festivals">Double Ninth & 9/9 weddings</a></li><li><a href="#slang">Number slang: 520, 1314, 666, 88</a></li>
<li><a href="#money">The economics of lucky numbers</a></li><li><a href="#avoid">Unlucky numbers</a></li><li><a href="#sources">Sources</a></li></ol></div>

<h2 id="decode">Reading 999910</h2>
<p>Chinese number symbolism works mainly through <b>sound</b>. Split 999910 into <b>9999</b> and <b>10</b>:</p>
<ul><li><b>9999 → 久久久久</b> (jiǔ jiǔ jiǔ jiǔ): 九 “nine” is pronounced exactly like 久 “long-lasting”. Four of them read as “forever and ever”.</li>
<li><b>10 → 十全十美</b> (shí quán shí měi): the idiom “ten complete, ten beautiful” means perfect in every way.</li></ul>
<blockquote><b>999910 ≈ “forever perfect”</b> — a lasting, flawless wish, fit for a wedding, a brand or a legacy.</blockquote>
<p class="callout"><b>Honesty note:</b> 999910 is not a documented set phrase. This is our cultural reading of well-known symbols. Some numeric-domain investors also discount any name containing 0 or 4, so its <i>market</i> value is a separate question from its <i>meaning</i>.</p>
{ad("inContent")}
<h2 id="nine">Nine: the imperial, eternal number</h2>
<p>Nine is the largest single digit and the most “yang” number, so it became the emperor’s number. Imperial robes carried nine dragons; there were nine official ranks; palace gates carry 81 (9 × 9) golden doornails. The emperor was called <b>九五之尊</b> — a phrase from the I Ching’s first hexagram. Legend says the Forbidden City has <b>9,999½ rooms</b>, one half-room short of the 10,000 said to belong to Heaven (surveys actually count about 9,371).</p>
<p>In daily life 9 is the number of <b>lasting love</b>: couples give 99 or 999 roses, and wedding red envelopes of 9,999 or 99,999 yuan wish the marriage a long life.</p>
<h2 id="ten">Ten: 十全十美</h2>
<p>十 (shí) closes the decimal cycle, so it stands for completeness. 十全十美 describes something with no flaw. Paired with 9999, it turns “forever” into “forever perfect”.</p>
<h2 id="gold">9999: “four-nines” gold</h2>
<p>In the Chinese gold trade the number of nines is the purity: <b>足金</b> is at least 99.0%, <b>千足金 (999)</b> is 99.9% and the Hong Kong retail standard, and <b>万足金 (9999)</b> is 99.99%, used mostly for bars. China’s total gold demand reached about <b>1,003 tonnes in 2025</b>, with bars and coins up 28% while jewellery fell 25%.</p>
<h2 id="festivals">Double Ninth & 9/9 weddings</h2>
<p>The <b>Double Ninth Festival (重阳节)</b> falls on the 9th day of the 9th lunar month — <b>18 October 2026</b>. Because 九九 sounds like 久久, it became a day to honour elders; mainland China made it Seniors’ Day in 1989. On <b>9 September 2009</b>, Guangzhou registered <b>6,106 marriages</b> in a single day, a record since 1949.</p>
<h2 id="slang">Number slang: 520, 1314, 666, 88</h2>
<div class="table-wrap"><table><tr><th>Number</th><th>Reads as</th><th>Meaning</th></tr>
<tr><td>520</td><td>我爱你</td><td>I love you — 20 May is China’s online Valentine’s Day</td></tr>
<tr><td>1314</td><td>一生一世</td><td>For a lifetime</td></tr><tr><td>5201314</td><td>我爱你一生一世</td><td>I’ll love you forever</td></tr>
<tr><td>99</td><td>久久</td><td>Long-lasting</td></tr><tr><td>666</td><td>溜溜溜</td><td>Awesome / skilful</td></tr><tr><td>88</td><td>拜拜 / 发发</td><td>Bye-bye / double fortune</td></tr>
<tr><td>168</td><td>一路发</td><td>Prosper all the way</td></tr><tr><td>250</td><td>二百五</td><td>Fool (insult)</td></tr></table></div>
{ad("inContent")}
<h2 id="money">The economics of lucky numbers</h2>
<ul>
<li><b>Licence plates:</b> Hong Kong’s record is <b>HK$26M for “W” (2021)</b>; plate “28” sold for HK$18.1M (2016), “18” for HK$16.5M (2008) and “9” for HK$13M (1994). All proceeds go to the HK government.</li>
<li><b>Phone numbers:</b> Sichuan Airlines paid <b>¥2.33M</b> for 8888-8888 in 2003.</li>
<li><b>Events:</b> the Beijing Olympics opened at 8 pm on 08-08-2008.</li>
<li><b>Real estate:</b> towers skip floors 4, 14, 24 — some Hong Kong buildings skip the entire 40s.</li>
<li><b>Domains:</b> Chinese owners held about 59 of 100 NN.com and 480 of 1,000 NNN.com names; 55.com sold for $2.3M and 114.com for $2.1M. <a href="domains.html">Estimate a numeric domain →</a></li>
<li><b>Audience:</b> about <b>40 million</b> overseas Chinese live outside Greater China — the largest communities in Thailand, Malaysia, the US, Singapore and Canada.</li></ul>
<h2 id="avoid">Unlucky numbers</h2>
<p><b>4</b> (死 death) and combinations such as <b>14</b> (要死), <b>24</b> (易死), <b>54</b> (我死) and <b>74</b> (气死) are avoided. <b>250</b> and <b>38</b> are insults. The <b>7th lunar month</b> — Ghost Month — is avoided for weddings and moves.</p>
<h2>Frequently asked</h2>{faq_html(CULTURE_FAQ)}
<h2 id="sources">Sources</h2><ol class="sources">{src}</ol>
<p class="form-note">Facts were checked against the sources above in September 2026. Spot an error? <a href="contact.html">Tell us</a>.</p>
</article>
<aside><div class="side-sticky">
 <div class="card"><h3>Decode your number</h3><form class="searchbar" data-numsearch action="meaning.html" style="margin:8px 0 0"><input inputmode="numeric" placeholder="Any number" aria-label="Number"><button class="btn btn-red btn-sm" type="submit">Go</button></form></div>
 {ad("sidebar")}
 <div class="card"><h3>Daily lucky number</h3>{newsletter_form(root, compact=True)}</div>
</div></aside></div></section>"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": "999910 Decoded: Nine, Ten & the Chinese Economy of Luck",
           "datePublished": "2026-09-30", "dateModified": "2026-09-30", "author": {"@type": "Organization", "name": "999910.com"},
           "mainEntityOfPage": SITE + "/culture.html"}, faq_ld(CULTURE_FAQ)]
    return page("culture.html", "What Does 999910 Mean? Chinese Lucky Numbers 9, 10 & 9999 Explained | 999910.com",
                "999910 decoded: 9999 (久久久久, forever) + 10 (十全十美, perfect). Why 9 is imperial, what four-nines gold is, and how lucky numbers move real money.",
                body, jsonld=ld)


# ---------------- Number dictionary ----------------
NUMBERS = {
    "0": ("零", "líng", "Neutral", "Zero stands for wholeness and a fresh start. It is not unlucky in itself, but many Chinese number investors treat it as ‘empty’, so it lowers resale appeal in phone numbers and numeric domains."),
    "1": ("一", "yī", "Mildly lucky", "One means unity and leadership. In combinations it reads like 要 ‘will / want’, powering phrases such as 18 (要发, ‘will prosper’) and 168 (一路发)."),
    "2": ("二", "èr", "Lucky", "Two represents pairs — 好事成双, ‘good things come in pairs’ — which is why gifts are given in even numbers. In Cantonese it sounds like 易 ‘easy’."),
    "3": ("三", "sān", "Mixed-lucky", "Three sounds like 生 ‘life, birth’ in Cantonese, so it is popular in the south; in Mandarin it can echo 散 ‘scatter’. It is lucky for growth."),
    "4": ("四", "sì", "Avoided", "Four sounds like 死 ‘death’. Buildings skip 4th, 14th and 24th floors, and phone numbers or plates with 4 sell at a discount. It is fine in 4-letter Western contexts."),
    "5": ("五", "wǔ", "Neutral", "Five links to the Five Elements and balance. It reads as 我 ‘me’ in 520 and 518, or 无 ‘none’ in other contexts — neighbours decide its meaning."),
    "6": ("六", "liù", "Lucky", "Six sounds like 溜/流 ‘smooth, flowing’. 六六大顺 means ‘everything goes smoothly’; 666 is net slang for ‘awesome’."),
    "7": ("七", "qī", "Mixed", "Seven evokes togetherness (起 ‘arise’, 妻 ‘wife’, Qixi on 7/7) but also the 7th ‘Ghost’ month and 气 ‘anger’ in 74."),
    "8": ("八", "bā", "Luckiest for wealth", "Eight rhymes with 发 ‘prosper’. It is the most valuable digit in phone numbers, plates, prices and dates — Beijing opened the 2008 Olympics at 8 pm on 08-08-08."),
    "9": ("九", "jiǔ", "Very lucky", "Nine is a homophone of 久 ‘long-lasting’ and the emperor’s number. It is the number of eternal love (99 or 999 roses) and longevity (Double Ninth Festival)."),
    "10": ("十", "shí", "Lucky", "Ten stands for completeness — 十全十美, ‘perfect in every way’."),
    "18": ("一八", "yāo bā", "Very lucky", "要发 ‘will prosper’. In Hong Kong, plate ‘18’ sold for HK$16.5M in 2008."),
    "28": ("二八", "èr bā", "Very lucky", "易发 ‘easy prosperity’ in Cantonese. Hong Kong plate ‘28’ fetched HK$18.1M in 2016."),
    "58": ("五八", "wǔ bā", "Lucky", "我发 ‘I prosper’ — popular for shops and hotlines."),
    "68": ("六八", "liù bā", "Very lucky", "路发 ‘road to wealth’ / smooth prosperity — a favourite ending for business numbers."),
    "88": ("八八", "bā bā", "Very lucky", "发发 ‘double prosperity’. Also internet slang for ‘bye-bye’ (拜拜)."),
    "98": ("九八", "jiǔ bā", "Very lucky", "久发 ‘lasting prosperity’."),
    "99": ("九九", "jiǔ jiǔ", "Very lucky", "久久 ‘long, long time’ — the number of lasting love and longevity."),
    "168": ("一六八", "yāo liù bā", "Very lucky", "一路发 ‘prosper all the way’ — one of the most requested business numbers in China."),
    "518": ("五一八", "wǔ yāo bā", "Very lucky", "我要发 ‘I will prosper’ — beloved by entrepreneurs and used on 18 May promotions."),
    "520": ("五二零", "wǔ èr líng", "Lucky (love)", "我爱你 ‘I love you’. 20 May (5/20) is China’s online Valentine’s Day."),
    "521": ("五二一", "wǔ èr yāo", "Lucky (love)", "我愿意 ‘I do / I’m willing’ — a popular marriage-registration date (21 May)."),
    "666": ("六六六", "liù liù liù", "Very lucky", "Triple smoothness; in Chinese net slang, ‘awesome / pro’. Unlike the West, 666 is positive."),
    "888": ("八八八", "bā bā bā", "Very lucky", "Triple prosperity — the classic premium ending for phones, plates and prices."),
    "999": ("九九九", "jiǔ jiǔ jiǔ", "Very lucky", "久久久 ‘eternal’. Men give 999 roses for eternal love. (Note: ‘999’ is also a pharmaceutical trademark in some classes — we use it only as a numeral.)"),
    "1314": ("一三一四", "yī sān yī sì", "Lucky (love)", "一生一世 ‘for a lifetime’ — the 4 is ‘rescued’ by the romantic reading."),
    "5201314": ("五二零一三一四", "—", "Very lucky (love)", "我爱你一生一世 ‘I will love you for a lifetime’."),
    "8888": ("八八八八", "bā bā bā bā", "Very lucky", "Prosperity without end. Sichuan Airlines paid ¥2.33M for 8888-8888 in 2003."),
    "9999": ("九九九九", "jiǔ jiǔ jiǔ jiǔ", "Very lucky", "久久久久 ‘forever and ever’. Also the mark for 99.99% (‘four-nines’) gold, and the legendary room count of the Forbidden City."),
    "1688": ("一六八八", "yāo liù bā bā", "Very lucky", "一路发发 ‘prosper all the way, again and again’."),
    "6688": ("六六八八", "liù liù bā bā", "Very lucky", "顺顺发发 ‘smooth and prosperous’."),
    "999910": ("九九九九一零", "jiǔ jiǔ jiǔ jiǔ shí", "Very lucky", "Read as 9999 + 10: 久久久久 ‘forever and ever’ + 十全十美 ‘perfect’ — ‘forever perfect’. A cultural interpretation, not a set phrase."),
    "14": ("一四", "yāo sì", "Avoid", "要死 ‘want to die’. One of the most avoided endings."),
    "24": ("二四", "èr sì", "Avoid", "易死 ‘easy to die’ in Cantonese."),
    "44": ("四四", "sì sì", "Avoid", "Double ‘death’ — strongly avoided."),
    "74": ("七四", "qī sì", "Avoid", "气死 ‘angry to death’."),
    "250": ("二百五", "èr bǎi wǔ", "Avoid", "Slang for ‘fool, idiot’ — never price a gift at 250."),
    "38": ("三八", "sān bā", "Avoid in names", "Slang insult for a gossiping woman (though 8 March is Women’s Day)."),
}


def number_page(n):
    h, py, rep, text = NUMBERS[n]
    root = "../"
    related = [k for k in NUMBERS if k != n][:0]
    rel = [k for k in NUMBERS if k != n and (k in n or n in k)] or ["8", "9", "168", "888"]
    rel_html = "".join(f'<a href="{k}.html">{k}<small>{NUMBERS[k][2]}</small></a>' for k in rel[:8])
    faq = [(f"What does {n} mean in Chinese?", f"{n} ({h}, {py}) — {text}"),
           (f"Is {n} a lucky number?", f"Reputation: {rep}. Check any phone, plate or house number containing {n} with our free checker.")]
    body = page_hero(f"What does {n} mean in Chinese?", f"{h} · {py} · <b>{rep}</b>", f'<a href="index.html">Numbers</a> › {n}', root, "Number dictionary · 数字词典")
    body += f"""<section style="padding-top:10px"><div class="container layout-side"><div class="article">
<p class="lead">{text}</p>
<div class="result" id="meaning-static"></div>
{ad("inContent", root)}
<h2>Using {n} in real life</h2>
<ul><li><b>Phone & plates:</b> {'look for it in the last digits — endings carry the most weight.' if rep.startswith(('Very', 'Lucky')) else 'keep it out of the ending, or pair it with 8 or 9 to soften it.'}</li>
<li><b>Gifts & red envelopes:</b> {'amounts built on ' + n + ' make a warm wish.' if rep.startswith(('Very', 'Lucky')) else 'avoid amounts containing ' + n + '.'}</li>
<li><b>Business:</b> prices, hotlines and launch dates often use 8, 9, 6, 168 and 518.</li></ul>
<div class="flex"><a class="btn btn-red" href="../checker.html">Check a phone or plate</a><a class="btn btn-ghost" href="../consult.html?service=number&number={n}">Get a personal report</a></div>
<h2>Related numbers</h2><div class="num-grid">{rel_html}</div>
<h2>FAQ</h2>{faq_html(faq)}
</div>
<aside><div class="side-sticky"><div class="card"><h3>Decode another number</h3><form class="searchbar" data-numsearch action="../meaning.html" style="margin:8px 0 0"><input inputmode="numeric" placeholder="Any number" aria-label="Number"><button class="btn btn-red btn-sm" type="submit">Go</button></form></div>{ad("sidebar", root)}</div></aside>
</div></section>
<script>document.addEventListener("DOMContentLoaded",function(){{window.renderNumber&&renderNumber(document.getElementById("meaning-static"),"{n}","number")}})</script>"""
    return page(f"numbers/{n}.html", f"{n} Meaning in Chinese — {h} ({rep}) | 999910.com",
                f"What does {n} mean in Chinese? {text[:120]}", body, jsonld=[faq_ld(faq)])


def numbers_index():
    root = "../"
    groups = [("Very lucky & lucky", lambda r: r.startswith(("Very", "Lucky", "Mildly", "Mixed-lucky"))),
              ("Neutral & mixed", lambda r: r.startswith(("Neutral", "Mixed"))),
              ("Numbers to avoid", lambda r: r.startswith("Avoid"))]
    html = ""
    for title, fn in groups:
        items = "".join(f'<a href="{k}.html">{k}<small>{v[0]}</small></a>' for k, v in NUMBERS.items() if fn(v[2]))
        html += f"<h2 class='mt2'>{title}</h2><div class='num-grid'>{items}</div>"
    body = page_hero("Chinese Number Dictionary", "Meanings, homophones and real-world uses of the digits and combinations that matter in Chinese culture.", "Numbers", root, "数字词典")
    body += f'<section style="padding-top:10px"><div class="container">{html}{ad("inContent", root)}<p>Can’t find yours? <a href="../meaning.html">Decode any number instantly →</a></p></div></section>'
    return page("numbers/index.html", "Chinese Number Dictionary — Lucky & Unlucky Numbers A–Z | 999910.com",
                "Dictionary of Chinese number meanings: 8, 9, 6, 4, 168, 518, 520, 1314, 888, 9999 and more — lucky, neutral and unlucky numbers explained.", body)


def videos():
    root = ""
    topics = [("8 · 9 · 6", "Chinese lucky numbers explained", "chinese lucky numbers meaning"), ("520", "Chinese love numbers 520 & 1314", "520 1314 chinese love numbers"),
              ("重阳", "Double Ninth Festival traditions", "double ninth festival chongyang"), ("HK$", "Hong Kong vanity plate auctions", "hong kong number plate auction"),
              ("龙", "Chinese zodiac for beginners", "chinese zodiac explained"), ("卦", "Feng shui Kua number & directions", "kua number feng shui directions"),
              ("黄历", "How the Chinese almanac picks lucky days", "chinese almanac tong shu lucky days"), (".com", "Why numeric domains sell to Chinese buyers", "chinese numeric domain names"),
              ("金", "999 vs 9999 gold purity", "999 vs 9999 gold purity")]
    cards = "".join(f'<a class="card vcard" href="https://www.youtube.com/results?search_query={q.replace(" ", "+")}" target="_blank" rel="noopener"><div class="vthumb">{t}</div><h3>{h}</h3><span class="muted">Watch on YouTube →</span></a>' for t, h, q in topics)
    body = page_hero("Video Hub — Lucky Numbers, Zodiac & Feng Shui", "Short, practical videos on Chinese number culture. New episodes weekly on our channel.", "Videos", root, "视频 · Watch")
    body += f"""<section style="padding-top:10px"><div class="container">
<div class="flex" style="margin-bottom:18px"><a class="btn btn-red" data-yt-channel href="https://www.youtube.com/results?search_query=chinese+lucky+numbers" target="_blank" rel="noopener">▶ Subscribe on YouTube</a><a class="btn btn-ghost" href="#collab">Collaborate / submit a video</a></div>
<div class="grid g3" data-videos>{cards}</div>
{ad("inContent")}
<div class="grid g2 mt2" id="collab" style="align-items:start">
 <div><h2>Creators & brands: work with us</h2><p class="muted">Sponsor an episode, license our tools for your channel, or pitch a collaboration on Chinese culture, zodiac, feng shui or number investing.</p></div>
 <div class="card"><form data-lead="Video Collaboration">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="row2"><div class="field"><label for="v-n">Name</label><input id="v-n" name="name" required></div><div class="field"><label for="v-e">Email</label><input id="v-e" name="email" type="email" required></div></div>
  <div class="field"><label for="v-c">Channel / video link</label><input id="v-c" name="channel" type="url" placeholder="https://"></div>
  <div class="field"><label for="v-t">Idea</label><select id="v-t" name="type"><option>Sponsor an episode</option><option>Collaboration</option><option>Submit my video</option><option>License tools / embed</option></select></div>
  <div class="field"><label for="v-m">Message</label><textarea id="v-m" name="message"></textarea></div>
  <button class="btn btn-red btn-block" type="submit">Send</button></form></div>
</div></div></section>"""
    return page("videos.html", "Videos: Chinese Lucky Numbers, Zodiac & Feng Shui | 999910.com",
                "Watch short videos on Chinese lucky numbers, 520 & 1314, Double Ninth, Hong Kong plate auctions, zodiac, feng shui and numeric domains.", body)


def consult():
    root = ""
    radios = "".join(f'<label><input type="radio" name="service" value="{v}" data-prefill="service" {"checked" if k == "number" else ""} required>{v}</label>' for k, v in SERVICES)
    # prefill uses value keys; map radios by key too
    radios = "".join(f'<label><input type="radio" name="service" value="{k}" data-prefill="service" {"checked" if k == "number" else ""} required>{v}</label>' for k, v in SERVICES)
    pkgs = [("Quick Check", "Free", "One number or date, scored and explained by a person within 48 hours.", ["1 number or date", "Plain-English verdict", "Email reply"]),
            ("Personal Report", "Popular", "Your phone, plate, house and key dates analysed together with luckier alternatives.", ["Up to 5 numbers", "Zodiac & Kua directions", "Top 10 dates for your event", "PDF report"]),
            ("Business & Brand", "Premium", "Launch date, hotline, price points, address and numeric domain strategy for a business.", ["Brand & number audit", "Opening-date shortlist", "Domain & hotline sourcing", "Video call"])]
    pk = "".join(f'<div class="card tier{" best" if i == 1 else ""}">{"<span class=ribbon>MOST CHOSEN</span>" if i == 1 else ""}<h3>{t}</h3><div class="price" style="font-size:1.4rem">{p}</div><p>{d}</p><ul style="text-align:left">{"".join(f"<li>{x}</li>" for x in li)}</ul><a class="btn {"btn-red" if i == 1 else "btn-ghost"} btn-block" href="#consult-form">Request</a></div>' for i, (t, p, d, li) in enumerate(pkgs))
    body = page_hero("Get Your Personal Lucky Number Report", "Tell us what you’re choosing — a number, a date, a name or a domain. A consultant replies with a clear verdict and better options.", "Personal Reading", root, "Lead · 预约咨询")
    body += f"""<section style="padding-top:10px"><div class="container">
<div class="grid g3">{pk}</div>
<div class="grid g2 mt2" style="align-items:start">
 <div><h2>How it works</h2><ol><li><b>Tell us</b> what you’re choosing (60 seconds).</li><li><b>We analyse</b> digits, combinations, zodiac, almanac and market value.</li><li><b>You receive</b> a verdict, alternatives and next steps — quick checks are free.</li></ol>
 <div class="callout"><b>Our promise:</b> honest, transparent reasoning. If a number is fine as it is, we’ll tell you — no upsell.</div>
 <h3>Popular requests</h3><p class="muted">Choosing a new mobile number · buying a car plate · wedding registration dates · shop opening day · naming a business with lucky digits · valuing or selling a numeric domain.</p></div>
 <div class="card" id="consult-form"><form data-lead="Personal Report Request" data-steps data-ok="Thank you! Your request is in — expect a reply within 48 hours.">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="steps"><span></span><span></span><span></span></div>
  <div class="step"><h3>1 · What do you need?</h3><div class="choice">{radios}</div><button class="btn btn-red btn-block mt2" data-next>Continue →</button></div>
  <div class="step"><h3>2 · Details</h3>
   <div class="field"><label for="c-num">Number(s), date(s) or domain</label><input id="c-num" name="number" data-prefill="number" placeholder="e.g. 514 888 1688, 2027-05-20, 168168.com"></div>
   <div class="row2"><div class="field"><label for="c-dob">Birth date (optional)</label><input id="c-dob" name="birth_date" type="date"></div>
   <div class="field"><label for="c-bud">Budget</label><select id="c-bud" name="budget"><option>Free quick check</option><option>Under $50</option><option>$50–$150</option><option>$150–$500</option><option>$500+</option></select></div></div>
   <div class="field"><label for="c-msg">What are you deciding?</label><textarea id="c-msg" name="message" placeholder="Context helps us give a sharper answer."></textarea></div>
   <div class="flex"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-red" data-next>Continue →</button></div></div>
  <div class="step"><h3>3 · Where should we reply?</h3>
   <div class="row2"><div class="field"><label for="c-n">Name</label><input id="c-n" name="name" required autocomplete="name"></div><div class="field"><label for="c-e">Email</label><input id="c-e" name="email" type="email" required autocomplete="email"></div></div>
   <div class="row2"><div class="field"><label for="c-w">WhatsApp / phone (optional)</label><input id="c-w" name="phone" type="tel" autocomplete="tel"></div><div class="field"><label for="c-c">Country</label><input id="c-c" name="country" autocomplete="country-name"></div></div>
   <div class="field"><label class="flex" style="font-weight:500"><input type="checkbox" name="newsletter" value="yes" style="width:auto"> Also send me the free daily lucky number</label></div>
   <div class="field"><label class="flex" style="font-weight:500"><input type="checkbox" required style="width:auto"> I agree to the <a href="legal.html#privacy">privacy policy</a></label></div>
   <div class="flex"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-red" type="submit">Send my request →</button></div></div>
 </form></div>
</div></div></section>"""
    faq = [("Is the quick check really free?", "Yes. One number or date, reviewed by a person, free. Paid reports are optional and quoted before any work starts."),
           ("How fast will I hear back?", "Usually within 48 hours on business days."), ("Do you sell numbers or plates?", "We help you source and negotiate through legitimate channels and marketplaces; we don’t hold inventory of phone numbers or plates.")]
    body += f'<section class="section-alt"><div class="container article"><h2>FAQ</h2>{faq_html(faq)}</div></section>'
    return page("consult.html", "Personal Lucky Number Report & Consultation | 999910.com",
                "Request a personal Chinese lucky number report: phone, plate, house or business numbers, auspicious dates, feng shui and numeric domains. Free quick check.",
                body, jsonld=[faq_ld(faq)])


def advertise():
    root = ""
    fmts = [("Sponsored tool", "Your brand on a calculator result screen — seen at the moment of highest attention."),
            ("Homepage feature", "Hero-adjacent card or banner on the homepage and dictionary."),
            ("Newsletter sponsor", "Top slot in the daily lucky-number email."),
            ("Sponsored article", "Clearly labelled, editorially reviewed guide in your niche."),
            ("Contest sponsor", "Fund the monthly prize and get logo, mentions and entrant opt-ins."),
            ("Directory listing", "Feng shui consultants, jewellers, wedding planners, number & domain brokers."),
            ("Video integration", "Mention or segment in our YouTube episodes."),
            ("Partnership / acquisition", "Joint ventures, licensing, or acquiring 999910.com and this platform.")]
    fg = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in fmts)
    body = page_hero("Advertise, Sponsor or Partner with 999910.com", "Reach people making real decisions — weddings, homes, cars, phone numbers, business launches and investments — at the moment they decide.", "Advertise", root, "Sponsorship · 广告合作")
    body += f"""<section style="padding-top:10px"><div class="container">
<div class="grid g4">{fg}</div>
<div class="grid g3 mt2"><div class="card"><div class="kpi">High intent</div><p>Visitors arrive with a concrete choice to make.</p></div><div class="card"><div class="kpi">Global</div><p>Relevant to ~40M overseas Chinese plus Asia-curious audiences worldwide.</p></div><div class="card"><div class="kpi">Brand-safe</div><p>Clearly labelled sponsorships; no deceptive formats.</p></div></div>
<div class="grid g2 mt2" style="align-items:start">
 <div><h2>Ideal sponsors</h2><p class="muted">Jewellers & gold dealers · wedding planners & venues · real-estate agents · mobile carriers · car dealers · feng shui & astrology services · domain marketplaces & brokers · Chinese language schools · travel brands · fintech & remittance.</p>
 <div class="callout"><b>Founding-sponsor rates</b> are available for the first sponsors in each category. Ask for the media kit.</div>
 <p><a class="btn btn-gold" href="{INTEREST}" target="_blank" rel="noopener">Acquisition / partnership inquiry →</a></p></div>
 <div class="card"><form data-lead="Advertising & Sponsorship Inquiry" data-ok="Thanks! The media kit and availability are on their way.">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="row2"><div class="field"><label for="a-co">Company</label><input id="a-co" name="company" required></div><div class="field"><label for="a-w">Website</label><input id="a-w" name="website" type="url" placeholder="https://"></div></div>
  <div class="row2"><div class="field"><label for="a-n">Your name</label><input id="a-n" name="name" required></div><div class="field"><label for="a-e">Work email</label><input id="a-e" name="email" type="email" required></div></div>
  <div class="field"><span style="font-weight:600;font-size:.92rem">Interested in</span><div class="choice" style="margin-top:6px">
   <label><input type="checkbox" name="formats" value="Sponsored tool">Sponsored tool</label><label><input type="checkbox" name="formats" value="Banner">Banner</label><label><input type="checkbox" name="formats" value="Newsletter">Newsletter</label>
   <label><input type="checkbox" name="formats" value="Article">Article</label><label><input type="checkbox" name="formats" value="Contest">Contest</label><label><input type="checkbox" name="formats" value="Partnership">Partnership</label><label><input type="checkbox" name="formats" value="Acquisition">Acquisition</label></div></div>
  <div class="field"><label for="a-b">Monthly budget</label><select id="a-b" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option><option>Let’s discuss</option></select></div>
  <div class="field"><label for="a-m">Goals</label><textarea id="a-m" name="message"></textarea></div>
  <button class="btn btn-red btn-block" type="submit">Request media kit →</button></form></div>
</div></div></section>"""
    return page("advertise.html", "Advertise & Sponsor — Media Kit | 999910.com",
                "Advertise on 999910.com: sponsored tools, homepage features, newsletter, articles, contest sponsorship, directory listings, video and partnerships.", body)


def support():
    root = ""
    tiers = [("Lucky Nine", "$9", "Keeps a tool online for a week.", "9"), ("Double Nine 久久", "$99", "Funds a new article, video or tool feature.", "99"), ("Imperial Patron 九五", "$999", "Funds a month of prizes and hiring — plus founding-patron recognition.", "999")]
    tg = "".join(f'<div class="card tier{" best" if i == 1 else ""}">{"<span class=ribbon>BEST IMPACT</span>" if i == 1 else ""}<h3>{t}</h3><div class="price">{p}</div><p>{d}</p><button class="btn {"btn-red" if i == 1 else "btn-ghost"} btn-block" data-amount="{a}" data-tier="{t}">Choose {p}</button></div>' for i, (t, p, d, a) in enumerate(tiers))
    alloc = [("Operations & hosting", 30), ("Promotion & marketing", 25), ("Hiring talent", 25), ("Contest prizes", 20)]
    al = "".join(f'<div><span>{n}</span><div class="bar"><i style="width:{v}%"></i></div><b>{v}%</b></div>' for n, v in alloc)
    body = page_hero("Support 999910.com — Keep the Tools Free", "Your support pays for operations, promotion, new talent and the prizes in our monthly contests. Every tier is optional — every tool stays free.", "Support Us", root, "Donate · 支持我们")
    body += f"""<section style="padding-top:10px"><div class="container">
<div class="card" data-goal></div>
<div class="grid g3 mt2">{tg}</div>
<div class="flex mt2" style="justify-content:center">
 <a class="btn btn-gold" data-donate-link="buymeacoffee" hidden>Buy Me a Coffee</a><a class="btn btn-gold" data-donate-link="kofi" hidden>Ko-fi</a>
 <a class="btn btn-gold" data-donate-link="paypal" hidden>PayPal</a><a class="btn btn-gold" data-donate-link="stripe" hidden>Card (Stripe)</a><a class="btn btn-gold" data-donate-link="githubSponsors" hidden>GitHub Sponsors</a>
</div>
<div class="grid g2 mt2" style="align-items:start">
 <div><h2>Where your money goes</h2><div class="alloc">{al}</div>
 <h3 class="mt2">Other ways to help</h3><ul><li>Share a tool result with friends</li><li><a href="advertise.html">Sponsor a contest prize</a></li><li><a href="careers.html">Contribute as a writer, translator or creator</a></li><li><a href="contest.html">Enter the monthly contest</a></li></ul>
 <p class="form-note">Supporting 999910.com is a voluntary contribution to a private website, not a charitable donation, and is not tax-deductible.</p></div>
 <div class="card" id="pledge-form"><h3>Pledge your support</h3><p class="muted">Choose an amount; we’ll send a secure payment link (card, PayPal or bank) by email.</p>
 <form data-lead="Supporter Pledge" data-ok="Thank you! A secure payment link is on its way.">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="row2"><div class="field"><label for="s-a">Amount (USD)</label><input id="s-a" name="amount" type="number" min="1" value="99" required></div><div class="field"><label for="s-f">Frequency</label><select id="s-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
  <input type="hidden" name="tier">
  <div class="field"><label for="s-u">Support goes to</label><select id="s-u" name="purpose"><option>Wherever needed most</option><option>Operations</option><option>Promotion & marketing</option><option>Hiring talent</option><option>Contest prizes</option></select></div>
  <div class="row2"><div class="field"><label for="s-n">Name</label><input id="s-n" name="name" required></div><div class="field"><label for="s-e">Email</label><input id="s-e" name="email" type="email" required></div></div>
  <div class="field"><label class="flex" style="font-weight:500"><input type="checkbox" name="public_thanks" value="yes" style="width:auto"> List my name on the supporters wall</label></div>
  <button class="btn btn-red btn-block" type="submit">Send my pledge →</button></form></div>
</div></div></section>"""
    return page("support.html", "Support 999910.com — Donate to Keep Lucky Number Tools Free",
                "Support free Chinese lucky-number tools. Tiers from $9: funds operations, promotion, hiring talent and monthly contest prizes.", body)


def contest():
    root = ""
    body = page_hero('<span data-contest="title">Luckiest Number of the Month</span>', 'Share your luckiest phone number, plate, house number or date — and the story behind it. Prize: <b data-contest="prize">prize pool</b>. Closes <b data-contest="closes">month end</b>.', "Contest", root, 'Contest · <span data-contest="month">this month</span>')
    body += f"""<section style="padding-top:10px"><div class="container">
<div class="grid g4"><div class="card"><div class="kpi">1</div><h3>Check your number</h3><p>Score it with our <a href="checker.html">free checker</a>.</p></div><div class="card"><div class="kpi">2</div><h3>Tell the story</h3><p>How did it bring you luck?</p></div><div class="card"><div class="kpi">3</div><h3>Get votes</h3><p>Finalists are featured and shared.</p></div><div class="card"><div class="kpi">4</div><h3>Win</h3><p>Prize + Hall of Fame feature.</p></div></div>
<div class="grid g2 mt2" style="align-items:start">
 <div class="card"><h2>Enter now</h2><form data-lead="Contest Entry" data-ok="You’re entered! Watch your inbox for finalist news.">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="row2"><div class="field"><label for="k-n">Name</label><input id="k-n" name="name" required></div><div class="field"><label for="k-e">Email</label><input id="k-e" name="email" type="email" required></div></div>
  <div class="row2"><div class="field"><label for="k-cat">Category</label><select id="k-cat" name="category"><option>Phone number</option><option>Licence plate</option><option>House / address</option><option>Lucky date</option><option>Numeric domain</option></select></div><div class="field"><label for="k-c">Country</label><input id="k-c" name="country" required></div></div>
  <div class="field"><label for="k-num">Your number / date</label><input id="k-num" name="number" required></div>
  <div class="field"><label for="k-s">Your story (max 500 characters)</label><textarea id="k-s" name="story" maxlength="500" required></textarea></div>
  <div class="field"><label for="k-soc">Social handle (optional — for bonus shout-out)</label><input id="k-soc" name="social"></div>
  <div class="field"><label for="k-q">Skill-testing question: 9 × 10 + 9 − 9 = ?</label><input id="k-q" name="skill_answer" inputmode="numeric" required pattern="90" title="Hint: 9 × 10 = 90"></div>
  <div class="field"><label class="flex" style="font-weight:500"><input type="checkbox" required style="width:auto"> I am 18+ and accept the <a href="#rules">official rules</a></label></div>
  <button class="btn btn-red btn-block" type="submit">Submit my entry →</button></form></div>
 <div><h2>Prizes & sponsors</h2><p><b data-contest="prize">Prize pool</b></p><p class="muted">Prizes are funded by sponsors and supporters. Want your brand in front of every entrant?</p>
 <a class="btn btn-gold" href="advertise.html">Sponsor a prize</a> <a class="btn btn-ghost" href="support.html">Fund the prize pool</a>
 <h3 class="mt2">Hall of Fame</h3><div class="card center"><p class="muted mb0">Our first winner will be announced after the October 2026 contest closes. This could be you.</p></div>
 {ad("sidebar")}</div>
</div>
<div class="article mt2" id="rules"><h2>Official rules (summary)</h2>
<ol><li><b>No purchase necessary.</b> A purchase or donation does not improve your chances.</li>
<li><b>Eligibility:</b> 18+; void where prohibited. Employees of sponsors and their households are not eligible.</li>
<li><b>Entry period:</b> from the first day of the month until 23:59 (Eastern Time) on the closing date shown above. One entry per person per month.</li>
<li><b>Judging:</b> 50% cultural score from our public methodology, 50% originality of the story, judged by the 999910.com editorial team. Decisions are final.</li>
<li><b>Skill-testing question:</b> residents of Canada must correctly answer a mathematical skill-testing question to be declared a winner.</li>
<li><b>Prize:</b> as stated above; no cash substitution unless offered by the sponsor. Odds depend on the number of eligible entries.</li>
<li><b>Winners</b> are contacted by email and must reply within 14 days. Winners agree to publication of their first name, country and story.</li>
<li><b>Privacy:</b> entries are used only to run the contest and, if you opt in, for our newsletter. See <a href="legal.html#privacy">Privacy</a>.</li>
<li>This contest is not sponsored, endorsed or administered by Google, YouTube, Meta, X or any platform.</li></ol></div>
</div></section>"""
    return page("contest.html", "Luckiest Number of the Month — Contest & Prizes | 999910.com",
                "Enter the monthly Luckiest Number contest: share your lucky phone number, plate, address or date and its story to win prizes.", body)


def careers():
    root = ""
    roles = [("Content Writer — Chinese Culture (EN/中文)", "Freelance · Remote", "Research-driven guides on numbers, festivals, zodiac and feng shui. Bilingual a strong plus."),
             ("Numerology & Feng Shui Consultant", "Contract · Remote", "Deliver personal reports and date selections. Proven experience required."),
             ("Video Editor — YouTube & Shorts", "Freelance · Remote", "Turn scripts into short, punchy explainers. Motion graphics a plus."),
             ("SEO & Growth Marketer", "Part-time · Remote", "Own keyword strategy, programmatic pages, partnerships and newsletter growth."),
             ("Community & Contest Manager", "Part-time · Remote", "Run monthly contests, moderate entries and grow social channels."),
             ("Front-end Developer", "Contract · Remote", "Build new tools in vanilla JS; performance and accessibility minded.")]
    rg = "".join(f'<div class="card"><span class="tag">{m}</span><h3 style="margin-top:8px">{t}</h3><p>{d}</p><a class="btn btn-ghost btn-sm" href="#apply" onclick="document.getElementById(\'j-r\').value=\'{t}\'">Apply</a></div>' for t, m, d in roles)
    body = page_hero("Careers — Build the World’s Home for Lucky Numbers", "Remote, flexible roles for writers, consultants, creators, marketers and developers who love Chinese culture.", "Careers", root, "Hiring · 招聘")
    body += f"""<section style="padding-top:10px"><div class="container"><div class="grid g3">{rg}</div>
<div class="grid g2 mt2" id="apply" style="align-items:start">
 <div><h2>Why join</h2><ul><li>Remote-first, async, flexible hours</li><li>Paid per project or retainer, plus performance bonuses</li><li>Your name on published work</li></ul>
 <div class="callout"><b>Scam warning:</b> we never ask applicants for money, bank details or fees.</div></div>
 <div class="card"><form data-lead="Job Application" data-ok="Application received — thank you! We reply to shortlisted candidates within 10 days.">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="field"><label for="j-r">Role</label><select id="j-r" name="role">{''.join(f'<option>{t}</option>' for t, _, _ in roles)}<option>Open application</option></select></div>
  <div class="row2"><div class="field"><label for="j-n">Name</label><input id="j-n" name="name" required></div><div class="field"><label for="j-e">Email</label><input id="j-e" name="email" type="email" required></div></div>
  <div class="row2"><div class="field"><label for="j-p">Portfolio / LinkedIn</label><input id="j-p" name="portfolio" type="url" placeholder="https://" required></div><div class="field"><label for="j-l">Languages</label><input id="j-l" name="languages" placeholder="English, 中文…"></div></div>
  <div class="field"><label for="j-a">Availability</label><select id="j-a" name="availability"><option>Under 10 h/week</option><option>10–20 h/week</option><option>20+ h/week</option></select></div>
  <div class="field"><label for="j-m">Why you?</label><textarea id="j-m" name="message" required></textarea></div>
  <button class="btn btn-red btn-block" type="submit">Submit application →</button></form></div>
</div></div></section>"""
    return page("careers.html", "Careers — Remote Jobs in Chinese Culture Content & Growth | 999910.com",
                "Join 999910.com: remote roles for content writers, feng shui consultants, video editors, SEO marketers, community managers and developers.", body)


def contact():
    root = ""
    body = page_hero("Contact 999910.com", "Questions, corrections, partnerships or press — we read everything.", "Contact", root)
    body += f"""<section style="padding-top:10px"><div class="container grid g2" style="align-items:start">
 <div class="card"><form data-lead="Contact Form">
  <div class="hp"><input name="_gotcha" tabindex="-1" autocomplete="off"></div>
  <div class="row2"><div class="field"><label for="ct-n">Name</label><input id="ct-n" name="name" required></div><div class="field"><label for="ct-e">Email</label><input id="ct-e" name="email" type="email" required></div></div>
  <div class="field"><label for="ct-t">Topic</label><select id="ct-t" name="topic"><option>General question</option><option>Personal reading</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Buy this website / domain</option><option>Correction</option><option>Press</option><option>Copyright / takedown</option></select></div>
  <div class="field"><label for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea></div>
  <button class="btn btn-red btn-block" type="submit">Send message →</button></form></div>
 <div><h2>Other ways to reach us</h2>
 <div class="card"><h3>Website, domain, sponsorship, advertising or partnership</h3><p class="muted">For acquisition or commercial partnership of 999910.com:</p><a class="btn btn-gold" href="{INTEREST}" target="_blank" rel="noopener">Contact via web.works →</a></div>
 <div class="card mt2"><h3>Prefer email?</h3><p class="muted">Opens your email app — our address stays private to stop spam.</p><a class="btn btn-ghost" href="#" data-mail="Hello from 999910.com">Email us</a></div></div>
</div></section>"""
    return page("contact.html", "Contact | 999910.com", "Contact 999910.com for readings, advertising, partnerships, corrections or acquisition inquiries.", body)


def about():
    root = ""
    body = page_hero("About 999910.com", "Forever useful, perfect in every detail — the modern home for Chinese number culture.", "About", root, "关于我们")
    body += f"""<section style="padding-top:10px"><div class="container article">
<h2>Our mission</h2><p>Millions of people choose phone numbers, plates, homes, wedding dates and business names with Chinese number culture in mind — yet most online advice is thin, inconsistent or buried under pop-ups. 999910.com brings it together in fast, free, transparent tools and well-sourced guides.</p>
<h2>Editorial standards</h2><ul><li>Every factual claim links to a source; our <a href="methodology.html">methodology</a> is public.</li><li>We separate culture from superstition-as-fact: scores are cultural indicators, not predictions.</li><li>Sponsored content is always labelled.</li><li>Corrections are welcome via the <a href="contact.html">contact form</a>.</li></ul>
<h2>How we’re funded</h2><p>Advertising (Google AdSense), sponsorships, optional personal reports and supporter <a href="support.html">donations</a>. Funds cover operations, promotion, talent and contest prizes.</p>
<h2>Partnership & acquisition</h2><p>This website and the domain 999910.com are open to sponsorship, advertising, partnership or acquisition. <a href="{INTEREST}" target="_blank" rel="noopener">Contact us via web.works →</a></p>
</div></section>"""
    return page("about.html", "About 999910.com — Mission, Standards & Funding", "About 999910.com: mission, editorial standards, funding and partnership opportunities.", body)


def methodology():
    root = ""
    body = page_hero("How Our Tools Work", "Transparent formulas — so you can judge the results yourself.", "Methodology", root)
    body += """<section style="padding-top:10px"><div class="container article">
<h2 id="score">Lucky number score (0–99)</h2>
<ol><li><b>Digit weights</b> from common homophones: 8 (+3.2), 9 (+3.0), 6 (+2.2), 2 (+1.2), 3 (+0.8), 1 (+0.6), 7 (+0.3), 5 (+0.2), 0 (0), 4 (−3.2).</li>
<li><b>Position:</b> the last two digits count 1.6×, the two before 1.2× — endings are what people remember and say.</li>
<li><b>Combinations</b> such as 168, 518, 520, 1314, 888, 9999 add points; 14, 24, 54, 74, 250 subtract. Combos inside a longer matched combo are not double-counted.</li>
<li><b>Patterns</b> (AAAA, ABAB, ABCABC, AABBCC, palindromes, straights) add memorability points; numbers of 4+ digits with no 4 get a small bonus.</li>
<li>The average is mapped to 50 ± and clamped to 3–99. Verdicts: 85+ 大吉 Very Auspicious · 70+ 吉 · 50+ 中平 · 35+ 小凶 · below 35 凶.</li></ol>
<h2 id="dates">Auspicious dates</h2>
<ul><li><b>Day pillar</b> (stem-branch) counted from 1 October 1949, a 甲子 day; verified against 1 January 2000 = 戊午.</li>
<li><b>Twelve Day Officers (建除十二神)</b>: officer = day branch − month branch, with month branches starting at approximate solar-term (节) dates.</li>
<li><b>Lunar dates</b> from your browser’s built-in Chinese calendar (Unicode CLDR/ICU). Ghost Month = 7th lunar month.</li>
<li><b>Clash:</b> a day whose branch is opposite your birth-year branch (六冲) is heavily down-ranked.</li></ul>
<h2 id="zodiac">Zodiac & compatibility</h2><p>Zodiac year is taken from the lunar year (Lunar New Year boundary), element from the heavenly stem. Compatibility uses Six Harmonies (六合), Triple Harmonies (三合), Six Clashes (六冲) and Six Harms (六害).</p>
<h2 id="kua">Kua number</h2><p>Eight Mansions formula with a 4 February (立春) year boundary: before 2000, male = 10 − reduced digits of the year, female = reduced + 5; from 2000, male = 9 − reduced, female = reduced + 6. Kua 5 becomes 2 (male) or 8 (female).</p>
<h2 id="domains">Numeric domain bands</h2><p>Base ranges by length from public comparable sales (NN, NNN, 4N, 5N, 6N .com), adjusted for TLD, presence of 0 or 4, patterns and all-lucky digits. Indicative only — not an appraisal or investment advice.</p>
<div class="callout">All tools are for cultural education and entertainment. Traditions vary across regions and schools.</div>
</div></section>"""
    return page("methodology.html", "Methodology — How the Lucky Number Score & Date Finder Work | 999910.com",
                "Transparent formulas behind 999910.com’s lucky number score, auspicious date finder, zodiac compatibility, Kua calculator and numeric domain bands.", body)


def legal():
    root = ""
    body = page_hero("Legal: Trademark, Copyright, Privacy & Terms", "Plain-language policies. Last updated 30 September 2026.", "Legal", root)
    body += f"""<section style="padding-top:10px"><div class="container article">
<h2 id="trademark">Trademark & copyright disclosure</h2>
<ul>
<li><b>The number.</b> “999910” is used on this website only as a domain name and as a numeral with cultural meaning. The site owner does not claim trademark rights in the number 999910, 9999, 999, 99, 10 or any digit. A search of public trademark databases found no registration for “999910”.</li>
<li><b>No affiliation.</b> 999910.com is independent and is <b>not affiliated with, endorsed by, sponsored by or connected to</b> China Resources Sanjiu Medical & Pharmaceutical Co. or its “999” brand, Nine West or any owner of “9999”-formative marks, jewellers or gold refiners using “999”/“9999” purity marks, the Palace Museum, Google LLC (including AdSense and YouTube), FormSubmit, or any other company named on this site.</li>
<li><b>Purity marks.</b> References to “999” and “9999” gold describe purity grades (99.9% and 99.99%) in their ordinary descriptive sense.</li>
<li><b>Third-party marks.</b> All product names, logos and brands mentioned are property of their respective owners and are used for identification or commentary only (nominative fair use).</li>
<li><b>Our copyright.</b> Original text, tools, code, design and graphics © <span data-year>2026</span> 999910.com / the site owner. All rights reserved. You may quote short excerpts with a link back.</li>
<li><b>Sources.</b> Facts from third parties are cited and linked; quotations are brief and for commentary. Traditional idioms, numerals and calendar systems are public domain.</li>
<li><b>Fonts & libraries.</b> Google Fonts (Inter, Noto Serif SC) under the SIL Open Font License.</li>
<li><b>Takedown / notice.</b> If you believe content infringes your rights, use the <a href="contact.html">contact form</a> (topic “Copyright / takedown”) with the URL, your work and your contact details. We respond promptly.</li></ul>
<h2 id="disclaimer">Disclaimer</h2><p>All tools and articles are for cultural education and entertainment. They are not financial, investment, legal, medical, real-estate or marital advice, and no outcome is guaranteed. Numeric-domain figures are indicative bands, not appraisals. Consult a qualified professional before important decisions.</p>
<h2 id="privacy">Privacy policy</h2>
<ul><li><b>Tools</b> run in your browser; numbers and birth dates you type into calculators are not sent to us.</li>
<li><b>Forms</b> (consultation, newsletter, contest, careers, advertising, pledges, contact) are delivered to our private inbox through the FormSubmit service. We use the data only to answer you and, if you opt in, to send the newsletter. We never sell personal data.</li>
<li><b>Advertising:</b> third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google’s use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> and learn more at <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">How Google uses information from sites that use its services</a>.</li>
<li><b>Your rights</b> (including under Quebec Law 25, PIPEDA, GDPR and CCPA where applicable): access, correction and deletion — request via the <a href="contact.html">contact form</a>.</li>
<li><b>Retention:</b> form submissions are kept only as long as needed to respond or as required by law.</li></ul>
<h2 id="cookies">Cookies</h2><p>We store your theme and cookie choice in your browser. With “Accept all”, Google AdSense may use personalised-ad cookies and Google Analytics (if enabled) anonymous measurement cookies. With “Essential only”, ads are non-personalised and analytics stays off. Change your mind any time by clearing site data.</p>
<h2 id="terms">Terms of use</h2><ul><li>Use the site lawfully; don’t scrape at scale, overload or reverse-engineer it for competing services without permission.</li><li>Sponsored content is labelled. Contests follow their <a href="contest.html#rules">official rules</a>.</li><li>Supporter contributions are voluntary, non-refundable once processed, and not tax-deductible.</li><li>The site is provided “as is” without warranties; liability is limited to the extent permitted by law.</li><li>Governing law: the Province of Quebec, Canada, unless local consumer law provides otherwise.</li></ul>
<h2 id="affiliate">Advertising & affiliate disclosure</h2><p>We may earn from ads, sponsorships and affiliate links. This never changes our scores or methodology.</p>
</div></section>"""
    return page("legal.html", "Trademark & Copyright Disclosure, Privacy, Cookies & Terms | 999910.com",
                "999910.com legal: trademark and copyright disclosure (no affiliation with any 999/9999 mark owners), disclaimer, privacy, cookies and terms.", body)


def notfound(base="/999910-com/"):
    body = """<section class="page-hero"><div class="container center"><div class="bignum">404</div><h1>This page has gone ‘4’ — let’s find you an 8.</h1>
<p class="lead" style="margin:0 auto 18px">The page you wanted isn’t here.</p><div class="flex" style="justify-content:center"><a class="btn btn-red" href="/999910-com/index.html">Home</a><a class="btn btn-ghost" href="/999910-com/meaning.html">Decode a number</a></div></div></section>"""
    return page("404.html", "Page not found | 999910.com", "Page not found.", body.replace("/999910-com/", base), root=base)
