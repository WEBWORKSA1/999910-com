/* 999910.com — interactive tool renderers */
(function () {
  "use strict";
  var L = window.Luck, $ = window.$1, $$ = window.$all;
  if (!L) return;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var ROOT = document.body.getAttribute("data-root") || "";
  function leadCTA(kind, value) {
    return '<div class="callout"><b>Want the full personal report?</b> Get a hand-checked analysis of <b>' + esc(value) + '</b> with better alternatives and the best dates to use it. ' +
      '<a class="btn btn-red btn-sm" style="margin-left:6px" href="' + ROOT + 'consult.html?service=' + kind + '&number=' + encodeURIComponent(value) + '">Get my report →</a></div>';
  }
  function gauge(score, v) {
    return '<div class="gauge" style="--v:' + score + '"><div><span><b>' + score + '</b><small>of 99</small></span></div></div>' +
      '<div><div class="stamp" style="border-color:' + v.c + ';color:' + v.c + '">' + v.zh + "</div>" +
      '<div class="verdict" style="margin-top:8px">' + v.en + "</div></div>";
  }
  function renderNumber(target, value, kind) {
    var a = L.analyzeNumber(value);
    if (!a) { target.innerHTML = '<p class="muted">Enter at least one digit.</p>'; target.classList.add("show"); return; }
    var chips = a.digits.map(function (d) { return '<span class="chip ' + d.cls + '">' + d.d + "<small>" + d.h + " " + d.py + "</small></span>"; }).join("");
    var combos = a.combos.length ? "<ul>" + a.combos.map(function (c) {
      return "<li><b>" + c.c + "</b> " + c.h + " — " + esc(c.m) + ' <span class="tag ' + (c.s > 0 ? "" : "red") + '">' + (c.s > 0 ? "+" : "") + c.s + "</span></li>";
    }).join("") + "</ul>" : '<p class="muted">No famous combinations found — the score comes from individual digits and their position.</p>';
    var els = Object.keys(a.elements).map(function (k) { return k + " ×" + a.elements[k]; }).join(" · ");
    var sug = L.suggest(a.n).filter(function (s) { return s.score > a.score; });
    var sugHtml = sug.length && a.score < 85 ? '<h3 class="mt2">Luckier alternatives</h3><div class="chips">' + sug.map(function (s) { return '<span class="chip great">' + s.n + "<small>score " + s.score + "</small></span>"; }).join("") + "</div>" : "";
    target.innerHTML = '<div class="card"><div class="score-wrap">' + gauge(a.score, a.verdict) +
      '<div style="flex:1;min-width:200px"><div class="muted">Number</div><div style="font-family:var(--serif);font-size:1.8rem;font-weight:800;word-break:break-all">' + a.n + "</div>" +
      '<div class="muted" style="font-size:.9rem">Pattern: ' + a.pattern + " · Digit sum " + a.sum + " → root " + a.root + " · Elements: " + els + "</div></div></div>" +
      '<h3 class="mt2">Digit by digit</h3><div class="chips">' + chips + "</div>" +
      "<h3>Meaningful combinations</h3>" + combos + sugHtml +
      '<div class="ad-slot" data-slot="result"><span>Ad space · <a href="' + ROOT + 'advertise.html">Sponsor this tool</a></span></div>' +
      leadCTA(kind || "number", a.n) +
      '<div class="flex"><button class="btn btn-ghost btn-sm" data-share="My number ' + a.n + ' scored ' + a.score + '/99 on 999910.com">Share result</button>' +
      '<a class="btn btn-ghost btn-sm" href="' + ROOT + 'meaning.html?n=' + a.n + '">Full meaning page</a></div></div>';
    target.classList.add("show");
    rebindShare(target);
    window.track && window.track("tool_use", { tool: kind || "number" });
  }
  function rebindShare(scope) {
    $$("[data-share]", scope).forEach(function (b) {
      b.addEventListener("click", function () {
        var t = b.getAttribute("data-share"), u = location.href;
        if (navigator.share) navigator.share({ title: t, text: t, url: u }).catch(function () { });
        else { try { navigator.clipboard.writeText(t + " " + u); b.textContent = "Copied ✓"; } catch (e) { } }
      });
    });
  }
  window.renderNumber = renderNumber;

  /* Generic number checker forms: <form data-tool="phone|plate|house|number"> */
  $$("form[data-tool]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var kind = f.getAttribute("data-tool"), out = document.getElementById(f.getAttribute("data-out"));
      renderNumber(out, f.querySelector("input").value, kind);
    });
  });

  /* Meaning page: ?n= */
  var mean = $("#meaning-out");
  if (mean) {
    var n = new URLSearchParams(location.search).get("n") || "999910";
    var inp = $("#meaning-input"); if (inp) inp.value = n;
    renderNumber(mean, n, "number");
    var h = $("#meaning-title"); if (h) h.textContent = "What does " + String(n).replace(/[^0-9]/g, "") + " mean in Chinese?";
  }

  /* Daily widget */
  $$("[data-daily]").forEach(function (box) {
    var d = L.daily(new Date()), l = d.lunar;
    box.innerHTML =
      '<div class="card"><small class="muted">Today’s lucky number</small><b>' + d.number + "</b></div>" +
      '<div class="card"><small class="muted">Lucky colour</small><b style="color:' + d.color[1] + '">' + d.color[0] + "</b></div>" +
      '<div class="card"><small class="muted">Joy direction 喜神</small><b>' + d.direction + "</b></div>" +
      '<div class="card"><small class="muted">Day ' + d.pillar.text + " · " + d.officer.zh + " " + d.officer.en + '</small><b style="font-size:1.1rem">Clashes: ' + d.pillar.clash.n + " " + d.pillar.clash.h + "</b>" +
      (l ? '<small class="muted">Lunar ' + l.month + (l.leap ? " (leap)" : "") + "/" + l.day + "</small>" : "") + "</div>";
  });

  /* Zodiac finder */
  var zf = $("#zodiac-form");
  if (zf) zf.addEventListener("submit", function (e) {
    e.preventDefault();
    var p = zf.querySelector("[name=dob]").value.split("-").map(Number); if (p.length < 3) return;
    var z = L.zodiacFromDate(p[0], p[1], p[2]), a = z.animal, out = $("#zodiac-out");
    var best = L.ANIMALS.map(function (x, i) { return { a: x, c: L.compat(z.index, i) }; }).sort(function (x, y) { return y.c.score - x.c.score; });
    out.innerHTML = '<div class="card"><div class="score-wrap"><div class="tool-ico" style="width:90px;height:90px;font-size:2.6rem">' + a.h + "</div><div>" +
      '<div class="verdict">' + z.element + " " + a.n + " <span class='hanzi'>" + z.stemBranch + "</span></div>" +
      '<p class="muted mb0">Lunar year ' + z.lunarYear + (z.lunar ? " · born on lunar " + z.lunar.month + "/" + z.lunar.day : "") + "</p></div></div>" +
      '<div class="grid g2 mt2"><div><h3>Lucky numbers</h3><div class="chips">' + a.lucky.map(function (x) { return '<span class="chip great">' + x + "</span>"; }).join("") + "</div></div>" +
      '<div><h3>Numbers to soften</h3><div class="chips">' + a.unlucky.map(function (x) { return '<span class="chip bad">' + x + "</span>"; }).join("") + "</div></div></div>" +
      "<h3>Best matches</h3><p>" + best.slice(0, 3).map(function (x) { return "<b>" + x.a.n + " " + x.a.h + "</b> (" + x.c.score + ")"; }).join(" · ") + "</p>" +
      "<h3>Challenging match</h3><p>" + best[best.length - 1].a.n + " " + best[best.length - 1].a.h + " — " + best[best.length - 1].c.label + "</p>" +
      leadCTA("zodiac", z.element + " " + a.n) + "</div>";
    out.classList.add("show");
  });
  /* Compatibility */
  var cf = $("#compat-form");
  if (cf) {
    $$("select", cf).forEach(function (s) { s.innerHTML = L.ANIMALS.map(function (a, i) { return '<option value="' + i + '">' + a.h + " " + a.n + "</option>"; }).join(""); });
    cf.querySelector("[name=b]").value = "4";
    cf.addEventListener("submit", function (e) {
      e.preventDefault();
      var a = +cf.a.value, b = +cf.b.value, c = L.compat(a, b), out = $("#compat-out");
      out.innerHTML = '<div class="card"><div class="score-wrap">' + gauge(c.score, L.verdict(c.score)) + '<div style="flex:1;min-width:200px"><h3>' + L.ANIMALS[a].n + " + " + L.ANIMALS[b].n + "</h3><p>" + c.label + "</p></div></div>" + leadCTA("compatibility", L.ANIMALS[a].n + " & " + L.ANIMALS[b].n) + "</div>";
      out.classList.add("show");
    });
  }
  /* Kua */
  var kf = $("#kua-form");
  if (kf) kf.addEventListener("submit", function (e) {
    e.preventDefault();
    var p = kf.dob.value.split("-").map(Number), k = L.kua(p[0], p[1], p[2], kf.gender.value), out = $("#kua-out");
    out.innerHTML = '<div class="card"><div class="score-wrap"><div class="tool-ico" style="width:90px;height:90px;font-size:2.6rem">' + k.kua + '</div><div><div class="verdict">Kua ' + k.kua + " · " + k.group + '</div><p class="muted mb0">Your four favourable directions (Eight Mansions / 八宅)</p></div></div>' +
      '<div class="table-wrap mt2"><table><tr><th>Purpose</th><th>Direction</th><th>Use it for</th></tr>' +
      "<tr><td>Sheng Qi 生气 · Wealth</td><td><b>" + k.dirs.wealth + "</b></td><td>Desk facing, front door, business negotiations</td></tr>" +
      "<tr><td>Tian Yi 天医 · Health</td><td><b>" + k.dirs.health + "</b></td><td>Bed head, dining seat, recovery</td></tr>" +
      "<tr><td>Yan Nian 延年 · Love</td><td><b>" + k.dirs.love + "</b></td><td>Bedroom, relationship & family harmony</td></tr>" +
      "<tr><td>Fu Wei 伏位 · Growth</td><td><b>" + k.dirs.growth + "</b></td><td>Study, meditation, personal development</td></tr></table></div>" + leadCTA("fengshui", "Kua " + k.kua) + "</div>";
    out.classList.add("show");
  });
  /* Date finder */
  var df = $("#dates-form");
  if (df) {
    var now = new Date(), next = new Date(now.getFullYear(), now.getMonth() + 1, 1);
    df.month.value = next.getFullYear() + "-" + String(next.getMonth() + 1).padStart(2, "0");
    df.addEventListener("submit", function (e) {
      e.preventDefault();
      var ym = df.month.value.split("-").map(Number), by = df.birthyear.value ? +df.birthyear.value : null;
      var list = L.dateFinder(ym[0], ym[1], df.occasion.value, by), out = $("#dates-out");
      var best = list.slice().sort(function (a, b) { return b.score - a.score; }).slice(0, 5);
      var wk = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
      function row(x) {
        return "<tr><td><b>" + x.date.toISOString().slice(0, 10) + "</b><br><small class='muted'>" + wk[x.date.getUTCDay()] + (x.lunar ? " · lunar " + x.lunar.month + "/" + x.lunar.day : "") + "</small></td>" +
          "<td>" + x.pillar.text + " · " + x.officer.zh + " " + x.officer.en + "<br><small class='muted'>Clashes " + x.clash.n + "</small></td>" +
          '<td><span class="stamp" style="font-size:.8rem;border-color:' + x.verdict.c + ";color:" + x.verdict.c + '">' + x.verdict.zh + "</span> <b>" + x.score + "</b></td>" +
          "<td><small>" + (x.notes.join("; ") || "—") + "</small></td></tr>";
      }
      out.innerHTML = '<div class="card"><h3>Top 5 dates</h3><div class="table-wrap"><table><tr><th>Date</th><th>Almanac</th><th>Score</th><th>Why</th></tr>' + best.map(row).join("") + "</table></div>" +
        leadCTA("dates", df.occasion.value + " " + df.month.value) +
        '<details><summary>Show the whole month</summary><div class="table-wrap"><table><tr><th>Date</th><th>Almanac</th><th>Score</th><th>Why</th></tr>' + list.map(row).join("") + "</table></div></details></div>";
      out.classList.add("show");
      window.track && window.track("tool_use", { tool: "dates" });
    });
  }
  /* Domain indicator */
  var dm = $("#domain-form");
  if (dm) dm.addEventListener("submit", function (e) {
    e.preventDefault();
    var r = L.domainValue(dm.domain.value), out = $("#domain-out");
    if (!r.ok) { out.innerHTML = '<div class="card"><p>' + r.msg + '</p><a class="btn btn-red" href="#domain-lead">Request a human valuation</a></div>'; out.classList.add("show"); return; }
    var a = r.analysis;
    out.innerHTML = '<div class="card"><div class="score-wrap">' + gauge(a.score, a.verdict) +
      '<div style="flex:1;min-width:220px"><div class="muted">' + r.cls + '</div><div style="font-family:var(--serif);font-size:1.8rem;font-weight:800">' + esc(r.label + "." + r.tld) + "</div>" +
      '<div class="kpi">' + L.money(r.lo) + " – " + L.money(r.hi) + '</div><div class="muted" style="font-size:.85rem">Indicative wholesale-to-retail band, not an appraisal</div></div></div>' +
      "<h3 class='mt2'>What moves the price</h3><ul>" + r.notes.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" +
      '<div class="callout"><b>Buying, selling or leasing a numeric domain?</b> Get comparable sales, a buyer list and a broker strategy. <a class="btn btn-red btn-sm" href="#domain-lead">Talk to us →</a></div></div>';
    out.classList.add("show");
    var f = $("#domain-lead [name=domain]"); if (f) f.value = r.label + "." + r.tld;
  });
})();
