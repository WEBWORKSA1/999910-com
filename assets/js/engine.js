/* 999910.com — Lucky Number & Chinese Almanac engine (client-side, no dependencies)
   For cultural education & entertainment. Methods are documented on /methodology.html */
(function (g) {
  "use strict";
  var DIGITS = {
    "0": { h: "零", py: "líng", w: 0, el: "Earth", m: "Wholeness, a fresh start; neutral. Some Chinese investors treat 0 as ‘empty’, so it lowers resale appeal in numbers and numeric domains." },
    "1": { h: "一", py: "yī", w: 0.6, el: "Water", m: "Unity and leadership. In combos it reads like 要 yào ‘will / want’ (e.g. 18 = 要发 ‘will prosper’)." },
    "2": { h: "二", py: "èr", w: 1.2, el: "Fire", m: "Pairs and harmony — 好事成双 ‘good things come in pairs’. In Cantonese it sounds like 易 ‘easy’." },
    "3": { h: "三", py: "sān", w: 0.8, el: "Wood", m: "Growth and life — in Cantonese close to 生 ‘birth, life’. In Mandarin it can echo 散 ‘scatter’, so it is mildly mixed." },
    "4": { h: "四", py: "sì", w: -3.2, el: "Metal", m: "Near-homophone of 死 sǐ ‘death’. The most avoided digit; many buildings skip 4th/14th/24th floors." },
    "5": { h: "五", py: "wǔ", w: 0.2, el: "Earth", m: "The Five Elements and balance. Sounds like 我 ‘me’ (520) or 无 ‘none’ — meaning depends on neighbours." },
    "6": { h: "六", py: "liù", w: 2.2, el: "Water", m: "Sounds like 溜 / 流 ‘smooth, flowing’ — 六六大顺 ‘everything goes smoothly’. 666 is net slang for ‘awesome’." },
    "7": { h: "七", py: "qī", w: 0.3, el: "Fire", m: "Togetherness (起 ‘arise’, 妻 ‘wife’) but also the 7th ‘ghost’ lunar month and 气 ‘anger’ — mixed." },
    "8": { h: "八", py: "bā", w: 3.2, el: "Wood", m: "Rhymes with 发 fā ‘prosper, get rich’. The luckiest digit for wealth; Beijing opened the Olympics at 8 pm on 08-08-2008." },
    "9": { h: "九", py: "jiǔ", w: 3.0, el: "Metal", m: "Homophone of 久 jiǔ ‘long-lasting, forever’. The imperial number — highest single digit, symbol of the emperor and of eternity." }
  };
  /* Combination dictionary (substring matches). s = score impact */
  var COMBOS = [
    ["5201314", "我爱你一生一世", "I love you for a lifetime", 14],
    ["1314", "一生一世", "For a whole lifetime", 8], ["520", "我爱你", "I love you", 6], ["521", "我愿意", "I’m willing / I do", 5],
    ["9999", "久久久久", "Forever and ever", 12], ["999", "久久久", "Eternal", 9], ["99", "久久", "Long-lasting", 5],
    ["8888", "发发发发", "Prosperity without end", 12], ["888", "发发发", "Triple prosperity", 9], ["88", "发发 / 拜拜", "Double fortune (net slang: bye-bye)", 5],
    ["666", "六六六", "Smooth sailing / ‘awesome’", 8], ["66", "六六大顺", "Everything smooth", 4],
    ["168", "一路发", "Prosper all the way", 9], ["1688", "一路发发", "Prosper all the way, twice", 6], ["518", "我要发", "I will prosper", 8],
    ["5188", "我要发发", "I will prosper greatly", 5], ["18", "要发", "Will prosper", 4], ["28", "易发", "Easy prosperity (Cantonese)", 4],
    ["58", "我发", "I prosper", 3], ["68", "路发", "Road to wealth", 4], ["98", "久发", "Lasting prosperity", 5], ["89", "发久", "Prosperity that lasts", 4],
    ["69", "顺久", "Smooth for a long time", 3], ["96", "久顺", "Long and smooth", 3], ["10", "十全十美", "Perfect in every way (as a whole ‘ten’)", 3],
    ["1010", "十全十美", "Perfect, twice over", 3], ["6688", "顺顺发发", "Smooth and prosperous", 5], ["8866", "发发顺顺", "Prosperous and smooth", 5],
    ["3344", "生生世世?", "Mixed — contains a double 4", -2],
    ["14", "要死", "‘Want to die’ — avoid", -9], ["24", "易死", "‘Easy death’ (Cantonese) — avoid", -8], ["54", "我死", "‘I die’ — avoid", -8],
    ["514", "我要死", "‘I will die’ — avoid", -6], ["74", "气死", "‘Angry to death’ — avoid", -7], ["748", "去死吧", "Insult — avoid", -8],
    ["44", "死死", "Double death — strongly avoid", -8], ["444", "死死死", "Strongly avoid", -6], ["250", "二百五", "‘Fool’ — slang insult", -8],
    ["38", "三八", "Insulting slang — avoid in names/brands", -5], ["13", "—", "Unlucky in Western culture (neutral in Chinese)", -1],
    ["94", "就是", "‘Exactly / that’s it’ — neutral slang", 0], ["57", "我去 / 吾妻", "Mixed", 0], ["1314520", "一生一世我爱你", "A lifetime of love", 6]
  ];
  var ANIMALS = [
    { n: "Rat", h: "鼠", lucky: [2, 3], unlucky: [5, 9] }, { n: "Ox", h: "牛", lucky: [1, 4], unlucky: [3, 6] },
    { n: "Tiger", h: "虎", lucky: [1, 3, 4], unlucky: [6, 7, 8] }, { n: "Rabbit", h: "兔", lucky: [3, 4, 6], unlucky: [1, 7, 8] },
    { n: "Dragon", h: "龙", lucky: [1, 6, 7], unlucky: [3, 8] }, { n: "Snake", h: "蛇", lucky: [2, 8, 9], unlucky: [1, 6, 7] },
    { n: "Horse", h: "马", lucky: [2, 3, 7], unlucky: [1, 5, 6] }, { n: "Goat", h: "羊", lucky: [3, 4, 9], unlucky: [6, 7, 8] },
    { n: "Monkey", h: "猴", lucky: [4, 9], unlucky: [2, 7] }, { n: "Rooster", h: "鸡", lucky: [5, 7, 8], unlucky: [1, 3, 9] },
    { n: "Dog", h: "狗", lucky: [3, 4, 9], unlucky: [1, 6, 7] }, { n: "Pig", h: "猪", lucky: [2, 5, 8], unlucky: [1, 7, 9] }
  ];
  var STEMS = "甲乙丙丁戊己庚辛壬癸", BRANCH = "子丑寅卯辰巳午未申酉戌亥";
  var STEM_EL = ["Wood", "Wood", "Fire", "Fire", "Earth", "Earth", "Metal", "Metal", "Water", "Water"];
  var EL_COLOR = { Wood: ["Green", "#2E7D6B"], Fire: ["Red", "#C8102E"], Earth: ["Yellow / Brown", "#B8860B"], Metal: ["White / Gold", "#C9971C"], Water: ["Blue / Black", "#1F4E79"] };
  var JOY_DIR = ["North-east", "North-west", "South-west", "South", "South-east", "North-east", "North-west", "South-west", "South", "South-east"];
  var OFFICERS = [["建", "Establish"], ["除", "Remove"], ["满", "Full"], ["平", "Balance"], ["定", "Stable"], ["执", "Initiate"], ["破", "Destruction"], ["危", "Danger"], ["成", "Success"], ["收", "Receive"], ["开", "Open"], ["闭", "Close"]];
  /* Approximate start days of the 12 solar-term months (节): month branch index */
  var TERM_START = [[1, 6, 1], [2, 4, 2], [3, 6, 3], [4, 5, 4], [5, 6, 5], [6, 6, 6], [7, 7, 7], [8, 8, 8], [9, 8, 9], [10, 8, 10], [11, 7, 11], [12, 7, 0]];

  function mod(a, n) { return ((a % n) + n) % n; }
  function clean(s) { return String(s || "").replace(/[^0-9]/g, ""); }

  /* ---------- Number scoring ---------- */
  function analyzeNumber(input) {
    var n = clean(input);
    if (!n) return null;
    var len = n.length, raw = 0, digits = [], found = [];
    for (var i = 0; i < len; i++) {
      var d = n[i], info = DIGITS[d];
      var weight = info.w * (i >= len - 2 ? 1.6 : (i >= len - 4 ? 1.2 : 1)); // endings matter most
      raw += weight;
      digits.push({ d: d, h: info.h, py: info.py, cls: info.w >= 2.5 ? "great" : info.w > 0.5 ? "good" : info.w < 0 ? "bad" : "" });
    }
    var used = {};
    COMBOS.slice().sort(function (a, b) { return b[0].length - a[0].length; }).forEach(function (c) {
      var idx = n.indexOf(c[0]);
      if (idx > -1) {
        // avoid double-counting shorter combos fully inside an already-counted longer one
        var covered = true;
        for (var k = idx; k < idx + c[0].length; k++) if (!used[k]) { covered = false; break; }
        if (covered) return;
        for (var j = idx; j < idx + c[0].length; j++) used[j] = true;
        raw += c[3];
        found.push({ c: c[0], h: c[1], m: c[2], s: c[3] });
      }
    });
    // Pattern bonuses
    var pat = pattern(n);
    raw += pat.bonus;
    var avg = raw / Math.max(len, 3);
    var score = Math.round(50 + avg * 14);
    if (n.indexOf("4") === -1 && len >= 4) score += 4;
    score = Math.max(3, Math.min(99, score));
    var sum = n.split("").reduce(function (a, b) { return a + (+b); }, 0), root = sum;
    while (root > 9) root = String(root).split("").reduce(function (a, b) { return a + (+b); }, 0);
    var els = {}; n.split("").forEach(function (d) { els[DIGITS[d].el] = (els[DIGITS[d].el] || 0) + 1; });
    return { n: n, score: score, verdict: verdict(score), digits: digits, combos: found, pattern: pat.name, sum: sum, root: root, elements: els, last: n.slice(-2) };
  }
  function pattern(n) {
    if (/^(\d)\1+$/.test(n)) return { name: "Solid (all same digit)", bonus: n.length * 1.2 };
    if (/^(\d\d)\1+$/.test(n)) return { name: "Repeating pair (ABAB…)", bonus: 4 };
    if (/^(\d{3})\1+$/.test(n)) return { name: "Repeating triple (ABCABC)", bonus: 4 };
    if (/(\d)\1\1\1/.test(n)) return { name: "Quad run (AAAA)", bonus: 5 };
    if (/^(\d)\1(\d)\2(\d)\3$/.test(n)) return { name: "Stepped pairs (AABBCC)", bonus: 3 };
    if (/(\d)\1\1/.test(n)) return { name: "Triple run (AAA)", bonus: 3 };
    if (n.length > 2 && n === n.split("").reverse().join("")) return { name: "Palindrome", bonus: 2 };
    if ("0123456789".indexOf(n) > -1 || "9876543210".indexOf(n) > -1) return { name: "Straight sequence", bonus: 2 };
    return { name: "Mixed", bonus: 0 };
  }
  function verdict(s) {
    if (s >= 85) return { zh: "大吉", en: "Very Auspicious", c: "var(--gold)" };
    if (s >= 70) return { zh: "吉", en: "Auspicious", c: "var(--jade)" };
    if (s >= 50) return { zh: "中平", en: "Neutral", c: "var(--muted)" };
    if (s >= 35) return { zh: "小凶", en: "Use with Caution", c: "var(--red)" };
    return { zh: "凶", en: "Best Avoided", c: "var(--red)" };
  }
  function suggest(n) {
    // Replace every 4 with 8 or 9 and propose endings — simple improvement ideas
    var out = [], base = clean(n);
    if (!base) return out;
    if (base.indexOf("4") > -1) out.push(base.replace(/4/g, "8"), base.replace(/4/g, "9"));
    ["88", "68", "99", "18", "168", "888"].forEach(function (end) {
      if (base.length > end.length) out.push(base.slice(0, base.length - end.length) + end);
    });
    return out.filter(function (v, i, a) { return a.indexOf(v) === i && v !== base; }).slice(0, 5)
      .map(function (v) { return { n: v, score: analyzeNumber(v).score }; })
      .sort(function (a, b) { return b.score - a.score; });
  }

  /* ---------- Calendar ---------- */
  var lunarFmt = null;
  try { lunarFmt = new Intl.DateTimeFormat("en-u-ca-chinese", { year: "numeric", month: "numeric", day: "numeric", timeZone: "UTC" }); } catch (e) { }
  function utc(y, m, d) { return new Date(Date.UTC(y, m - 1, d, 12)); }
  function lunar(date) {
    if (!lunarFmt) return null;
    var p = {}; lunarFmt.formatToParts(date).forEach(function (x) { p[x.type] = x.value; });
    var mm = String(p.month || ""), leap = /bis/i.test(mm);
    return { year: +(p.relatedYear || p.year), month: parseInt(mm, 10), leap: leap, day: +p.day };
  }
  var ANCHOR = Date.UTC(1949, 9, 1, 12); // 1949-10-01 was a 甲子 (jiǎ-zǐ) day
  function dayPillar(date) {
    var days = Math.round((date.getTime() - ANCHOR) / 864e5);
    var s = mod(days, 10), b = mod(days, 12);
    return { stem: s, branch: b, text: STEMS[s] + BRANCH[b], animal: ANIMALS[b], clash: ANIMALS[(b + 6) % 12], element: STEM_EL[s] };
  }
  function monthBranch(date) {
    var m = date.getUTCMonth() + 1, d = date.getUTCDate(), br = 0;
    for (var i = TERM_START.length - 1; i >= 0; i--) {
      var t = TERM_START[i];
      if (m > t[0] || (m === t[0] && d >= t[1])) { br = t[2]; break; }
      if (i === 0) br = 0; // before Jan 6 → 子 month
    }
    return br;
  }
  function officer(date) { var o = mod(dayPillar(date).branch - monthBranch(date), 12); return { i: o, zh: OFFICERS[o][0], en: OFFICERS[o][1] }; }
  function zodiacFromDate(y, m, d) {
    var date = utc(y, m, d), L = lunar(date), ly = L ? L.year : (m < 2 || (m === 2 && d < 4) ? y - 1 : y);
    var idx = mod(ly - 4, 12), st = mod(ly - 4, 10);
    return { lunarYear: ly, animal: ANIMALS[idx], index: idx, element: STEM_EL[st], stemBranch: STEMS[st] + BRANCH[idx], lunar: L };
  }
  function compat(a, b) {
    var trines = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]];
    var harmony = [[0, 1], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]];
    var harm = [[0, 7], [1, 6], [2, 5], [3, 4], [8, 11], [9, 10]];
    function pairIn(list) { return list.some(function (p) { return (p[0] === a && p[1] === b) || (p[0] === b && p[1] === a); }); }
    if (a === b) return { score: 72, label: "Same sign — natural understanding, watch for stubborn mirrors" };
    if (pairIn(harmony)) return { score: 95, label: "Six Harmony (六合) — a classic ideal match" };
    if (trines.some(function (t) { return t.indexOf(a) > -1 && t.indexOf(b) > -1; })) return { score: 90, label: "Triple Harmony (三合) — strong shared values" };
    if (mod(a - b, 12) === 6) return { score: 25, label: "Six Clash (六冲) — opposite forces; needs conscious effort" };
    if (pairIn(harm)) return { score: 40, label: "Six Harm (六害) — friction points; communication is key" };
    return { score: 62, label: "Neutral — compatible with mutual respect" };
  }
  function kua(year, month, day, gender) {
    var y = (month < 2 || (month === 2 && day < 4)) ? year - 1 : year; // Lìchūn boundary ≈ Feb 4
    var s = String(y).slice(-2).split("").reduce(function (a, b) { return a + (+b); }, 0);
    while (s > 9) s = String(s).split("").reduce(function (a, b) { return a + (+b); }, 0);
    var k;
    if (gender === "m") k = y < 2000 ? 10 - s : 9 - s; else k = y < 2000 ? s + 5 : s + 6;
    while (k > 9) k = String(k).split("").reduce(function (a, b) { return a + (+b); }, 0);
    if (k === 0) k = 9;
    if (k === 5) k = gender === "m" ? 2 : 8;
    var D = { 1: ["South-east", "East", "South", "North"], 2: ["North-east", "West", "North-west", "South-west"], 3: ["South", "North", "South-east", "East"], 4: ["North", "South", "East", "South-east"], 6: ["West", "North-east", "South-west", "North-west"], 7: ["North-west", "South-west", "North-east", "West"], 8: ["South-west", "North-west", "West", "North-east"], 9: ["East", "South-east", "North", "South"] };
    return { kua: k, group: [1, 3, 4, 9].indexOf(k) > -1 ? "East Group" : "West Group", dirs: { wealth: D[k][0], health: D[k][1], love: D[k][2], growth: D[k][3] } };
  }
  function daily(date) {
    date = date || new Date(); var d = utc(date.getFullYear(), date.getMonth() + 1, date.getDate());
    var dp = dayPillar(d), L = lunar(d), seed = d.getUTCFullYear() * 372 + d.getUTCMonth() * 31 + d.getUTCDate();
    var pool = [8, 9, 6, 2, 1, 3, 5, 7, 18, 28, 68, 88, 99, 168, 518, 666, 888, 999, 1314, 9999];
    return { pillar: dp, lunar: L, officer: officer(d), number: pool[mod(seed * 9301 + 49297, pool.length)], color: EL_COLOR[dp.element], direction: JOY_DIR[dp.stem] };
  }
  var OCC = {
    wedding: { good: { 8: 16, 4: 14, 10: 12, 2: 5 }, bad: { 6: -30, 11: -15, 7: -12, 0: -5 }, ghost: -25, weekend: 5 },
    move: { good: { 8: 15, 10: 12, 1: 8, 4: 8 }, bad: { 6: -30, 7: -12, 11: -10 }, ghost: -20, weekend: 3 },
    opening: { good: { 10: 20, 8: 15, 2: 10, 4: 6 }, bad: { 6: -30, 11: -18, 7: -10 }, ghost: -20, weekend: 0 },
    signing: { good: { 4: 15, 8: 15, 5: 12, 10: 8 }, bad: { 6: -30, 7: -12, 11: -8 }, ghost: -8, weekend: -3 },
    travel: { good: { 10: 14, 8: 10, 1: 6 }, bad: { 7: -14, 6: -16, 11: -6 }, ghost: -6, weekend: 2 }
  };
  function dateFinder(year, month, occasion, birthYear) {
    var cfg = OCC[occasion] || OCC.wedding, out = [], last = new Date(Date.UTC(year, month, 0)).getUTCDate();
    var userBranch = birthYear ? mod(+birthYear - 4, 12) : null;
    for (var day = 1; day <= last; day++) {
      var dt = utc(year, month, day), dp = dayPillar(dt), off = officer(dt), L = lunar(dt), s = 55, notes = [];
      if (cfg.good[off.i]) { s += cfg.good[off.i]; notes.push(off.zh + " " + off.en + " day favours this"); }
      if (cfg.bad[off.i]) { s += cfg.bad[off.i]; notes.push(off.zh + " " + off.en + " day — traditionally avoided"); }
      if (L && L.month === 7 && !L.leap) { s += cfg.ghost; notes.push("7th lunar ‘Ghost Month’"); }
      var ds = String(day);
      if (/8/.test(ds)) s += 5; if (/9/.test(ds)) s += 5; if (/6/.test(ds)) s += 3;
      if (/4/.test(ds)) { s -= 7; notes.push("date contains 4"); }
      var wd = dt.getUTCDay(); if (wd === 0 || wd === 6) s += cfg.weekend;
      if (L && L.month === 9 && L.day === 9) { s += 8; notes.push("Double Ninth 重阳"); }
      if (L && L.month === 7 && L.day === 7) { s += occasion === "wedding" ? 8 : 0; notes.push("Qixi 七夕 (Chinese Valentine’s)"); }
      if (month === 4 && (day === 4 || day === 5)) { s -= 12; notes.push("near Qingming (tomb-sweeping)"); }
      if (userBranch !== null && mod(dp.branch - userBranch, 12) === 6) { s -= 30; notes.push("clashes with your sign (" + ANIMALS[userBranch].n + ")"); }
      s = Math.max(5, Math.min(99, s));
      out.push({ date: dt, day: day, score: s, verdict: verdict(s), pillar: dp, officer: off, lunar: L, notes: notes, clash: dp.clash });
    }
    return out;
  }
  /* ---------- Numeric domain indicator ---------- */
  function domainValue(input) {
    var raw = String(input || "").trim().toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "").replace(/\/.*$/, "");
    var m = raw.match(/^([a-z0-9-]+)\.([a-z.]+)$/); if (!m) m = [raw, raw, "com"];
    var label = m[1], tld = m[2];
    if (!/^\d+$/.test(label)) return { ok: false, label: label, tld: tld, msg: "This quick indicator covers all-numeric domains only. Request a human valuation for brandable or keyword names." };
    var len = label.length;
    var bands = { 1: [1e6, 1e7], 2: [3e5, 3e6], 3: [3e4, 1.5e6], 4: [3e3, 1.2e5], 5: [250, 1.5e4], 6: [100, 4e3], 7: [15, 600] };
    var b = bands[Math.min(len, 7)] || [10, 300];
    var tf = { com: 1, cn: 0.15, net: 0.12, "com.cn": 0.1, cc: 0.08, org: 0.06, co: 0.06, io: 0.05, xyz: 0.02 }[tld] || 0.03;
    var f = 1, notes = [];
    var a = analyzeNumber(label), p = pattern(label);
    if (label.indexOf("4") > -1) { f *= 0.4; notes.push("Contains 4 — Chinese buyers typically discount heavily"); }
    if (label.indexOf("0") > -1 && len >= 5) { f *= 0.6; notes.push("Contains 0 — outside the ‘premium’ no-0/no-4 set many 5N/6N investors prefer"); }
    if (label.indexOf("4") === -1 && label.indexOf("0") === -1 && len >= 5) { f *= 1.5; notes.push("No 0 or 4 — in the ‘premium’ pool for Chinese investors"); }
    if (p.bonus >= 5) { f *= 3; notes.push("Strong pattern: " + p.name); } else if (p.bonus >= 3) { f *= 1.8; notes.push("Pattern: " + p.name); } else if (p.bonus > 0) { f *= 1.3; notes.push("Pattern: " + p.name); }
    if (/^[689]+$/.test(label)) { f *= 1.6; notes.push("All-lucky digits (6/8/9)"); }
    if (label[0] === "0") { f *= 0.5; notes.push("Leading zero reduces liquidity"); }
    if (a.score >= 85) notes.push("Cultural score " + a.score + "/99 — " + a.verdict.en);
    var lo = Math.round(b[0] * tf * f), hi = Math.round(b[1] * tf * f);
    return { ok: true, label: label, tld: tld, len: len, cls: len + "N ." + tld, lo: Math.max(lo, 10), hi: Math.max(hi, 50), notes: notes, analysis: a };
  }
  function money(n) { return "$" + (n >= 1e6 ? (n / 1e6).toFixed(n >= 1e7 ? 0 : 1) + "M" : n >= 1e3 ? Math.round(n / 1e3) + "K" : n); }

  g.Luck = { DIGITS: DIGITS, COMBOS: COMBOS, ANIMALS: ANIMALS, STEMS: STEMS, BRANCH: BRANCH, EL_COLOR: EL_COLOR, analyzeNumber: analyzeNumber, suggest: suggest, verdict: verdict, lunar: lunar, dayPillar: dayPillar, officer: officer, zodiacFromDate: zodiacFromDate, compat: compat, kua: kua, daily: daily, dateFinder: dateFinder, domainValue: domainValue, money: money, utc: utc, pattern: pattern };
})(window);
