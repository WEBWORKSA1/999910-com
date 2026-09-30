/* 999910.com — core UI: nav, theme, consent, ads, forms (private inbox), video, modals */
(function () {
  "use strict";
  var S = window.SITE || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function sstore(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  window.$1 = $; window.$all = $$;

  /* ---- Private inbox (never rendered in the page) ---- */
  function inbox() { return (S._k || []).map(function (c) { return String.fromCharCode(c ^ 9); }).reverse().join(""); }
  function endpoint() { return "https://formsubmit.co/ajax/" + (S.formAlias || inbox()); }
  // Any element with [data-mail] opens the visitor's mail app on click, address assembled at click time only
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("[data-mail]");
    if (!a) return;
    e.preventDefault();
    var subj = encodeURIComponent(a.getAttribute("data-mail") || "Inquiry from 999910.com");
    window.location.href = "mai" + "lto:" + inbox() + "?subject=" + subj;
  });

  /* ---- Theme ---- */
  var root = document.documentElement, saved = store("theme");
  if (saved) root.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var dark = root.getAttribute("data-theme") === "dark" || (!root.getAttribute("data-theme") && matchMedia("(prefers-color-scheme: dark)").matches);
      var next = dark ? "light" : "dark"; root.setAttribute("data-theme", next); store("theme", next);
    });
  });

  /* ---- Mobile nav ---- */
  var menu = $(".menu");
  $$("[data-menu-open]").forEach(function (b) { b.addEventListener("click", function () { menu.classList.add("open"); b.setAttribute("aria-expanded", "true"); }); });
  $$("[data-menu-close]").forEach(function (b) { b.addEventListener("click", function () { menu.classList.remove("open"); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { menu && menu.classList.remove("open"); $$(".modal.show").forEach(function (m) { m.classList.remove("show"); }); } });

  /* ---- Year + contest/donate config text ---- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  var C = S.contest || {};
  $$("[data-contest]").forEach(function (el) { var k = el.getAttribute("data-contest"); if (C[k]) el.textContent = C[k]; });

  /* ---- Search: typed number → meaning page ---- */
  $$("form[data-numsearch]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = (f.querySelector("input").value || "").replace(/[^0-9]/g, "");
      if (v) location.href = f.getAttribute("action") + "?n=" + v;
    });
  });

  /* ---- Tabs ---- */
  $$("[data-tabs]").forEach(function (wrap) {
    var btns = $$("[role=tab]", wrap);
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) { x.setAttribute("aria-selected", "false"); var p = document.getElementById(x.getAttribute("aria-controls")); p && p.classList.remove("active"); });
        b.setAttribute("aria-selected", "true"); var p = document.getElementById(b.getAttribute("aria-controls")); p && p.classList.add("active");
      });
    });
  });

  /* ---- Consent (Quebec Law 25 / GDPR-friendly) ---- */
  var consent = store("consent");
  var cbox = $(".consent");
  if (!consent && cbox) cbox.classList.add("show");
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () { consent = b.getAttribute("data-consent"); store("consent", consent); cbox.classList.remove("show"); loadThirdParty(); });
  });

  /* ---- Ads: AdSense when configured, else house "advertise here" slots ---- */
  function renderAds() {
    var pub = S.adsenseClient;
    $$(".ad-slot").forEach(function (slot) {
      var key = slot.getAttribute("data-slot") || "inContent";
      if (pub && S.adSlots && S.adSlots[key] !== undefined) {
        slot.classList.add("filled");
        slot.innerHTML = '<span class="ad-label">Advertisement</span><ins class="adsbygoogle" style="display:block" data-ad-client="' + pub + '"' +
          (S.adSlots[key] ? ' data-ad-slot="' + S.adSlots[key] + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
        try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { }
      }
    });
  }
  function loadThirdParty() {
    if (S.adsenseClient && !window.__ads) {
      window.__ads = 1;
      window.adsbygoogle = window.adsbygoogle || [];
      if (consent === "essential") window.adsbygoogle.requestNonPersonalizedAds = 1;
      var s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
      s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + S.adsenseClient;
      document.head.appendChild(s); renderAds();
    }
    if (S.ga4 && consent === "all" && !window.__ga) {
      window.__ga = 1;
      var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + S.ga4; document.head.appendChild(g);
      window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", S.ga4);
    }
  }
  if (consent) loadThirdParty();
  function track(name, params) { try { window.gtag && gtag("event", name, params || {}); } catch (e) { } }
  window.track = track;

  /* ---- Forms → private inbox via FormSubmit ---- */
  function msg(form, ok, text) {
    var m = form.querySelector(".form-msg");
    if (!m) { m = document.createElement("div"); m.className = "form-msg"; form.appendChild(m); }
    m.className = "form-msg " + (ok ? "ok" : "err"); m.textContent = text; m.setAttribute("role", "status");
  }
  $$("form[data-lead]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var hp = form.querySelector(".hp input"); if (hp && hp.value) return;
      var data = {}, fd = new FormData(form);
      fd.forEach(function (v, k) { if (k === "_gotcha") return; data[k] = data[k] ? data[k] + ", " + v : v; });
      var type = form.getAttribute("data-lead");
      data._subject = "[999910.com] " + type + " — " + (data.name || data.email || "new submission");
      data._template = "table"; data._captcha = "false";
      data.form_type = type; data.page = location.href; data.submitted = new Date().toISOString();
      if (data.email) data._replyto = data.email;
      var btn = form.querySelector("[type=submit]"), label = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.innerHTML = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j.success) === "false") throw new Error(res.j.message || "failed");
          msg(form, true, form.getAttribute("data-ok") || "Thank you — received! We reply within 1–2 business days.");
          track("generate_lead", { form: type }); form.reset(); sstore("leadDone", "1");
          if (form.hasAttribute("data-steps")) resetSteps(form);
        })
        .catch(function () {
          msg(form, false, "Couldn’t send automatically. Click here to email us instead.");
          var m = form.querySelector(".form-msg"); m.style.cursor = "pointer";
          m.onclick = function () {
            var body = Object.keys(data).filter(function (k) { return k[0] !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
            location.href = "mai" + "lto:" + inbox() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body);
          };
        })
        .then(function () { if (btn) { btn.disabled = false; btn.innerHTML = label; } });
    });
  });

  /* ---- Multi-step forms ---- */
  function resetSteps(form) { goStep(form, 0); }
  function goStep(form, i) {
    var steps = $$(".step", form), bars = $$(".steps span", form);
    steps.forEach(function (s, k) { s.classList.toggle("active", k === i); });
    bars.forEach(function (b, k) { b.classList.toggle("on", k <= i); });
    form.setAttribute("data-cur", i);
  }
  $$("form[data-steps]").forEach(function (form) {
    goStep(form, 0);
    form.addEventListener("click", function (e) {
      var nx = e.target.closest("[data-next]"), pv = e.target.closest("[data-prev]");
      var cur = +form.getAttribute("data-cur");
      if (nx) {
        e.preventDefault();
        var fields = $$("input,select,textarea", $$(".step", form)[cur]), ok = true;
        fields.forEach(function (f) { if (ok && !f.checkValidity()) { f.reportValidity(); ok = false; } });
        if (ok) goStep(form, cur + 1);
      }
      if (pv) { e.preventDefault(); goStep(form, cur - 1); }
    });
  });

  /* ---- Prefill from query (?service=, ?number=) ---- */
  var q = new URLSearchParams(location.search);
  $$("[data-prefill]").forEach(function (el) { var v = q.get(el.getAttribute("data-prefill")); if (v) { if (el.type === "radio") { el.checked = el.value === v; } else el.value = v; } });

  /* ---- YouTube (lite, privacy-enhanced) ---- */
  function mountVideos() {
    var box = $("[data-videos]"); if (!box) return;
    var vids = S.videos || [];
    if (!vids.length) return; // fallback cards remain
    box.innerHTML = vids.map(function (v) {
      return '<div class="vcard"><div class="video" data-yt="' + v.id + '" role="button" tabindex="0" aria-label="Play: ' + (v.title || "video") + '">' +
        '<img loading="lazy" alt="" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg"><div class="play"><span>▶</span></div></div><h3>' + (v.title || "") + "</h3></div>";
    }).join("");
  }
  mountVideos();
  document.addEventListener("click", function (e) {
    var v = e.target.closest && e.target.closest("[data-yt]"); if (!v) return;
    v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute("data-yt") + '?autoplay=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="YouTube video"></iframe>';
    track("video_play", { id: v.getAttribute("data-yt") });
  });
  if (S.youtubeChannel) $$("[data-yt-channel]").forEach(function (a) { a.href = S.youtubeChannel; });

  /* ---- Donations ---- */
  var D = S.donate || {};
  $$("[data-donate-link]").forEach(function (a) {
    var k = a.getAttribute("data-donate-link");
    if (D[k]) { a.href = D[k]; a.target = "_blank"; a.rel = "noopener"; a.hidden = false; } else a.hidden = true;
  });
  $$("[data-goal]").forEach(function (el) {
    var pct = Math.min(100, Math.round((D.raised || 0) / (D.goal || 1) * 100));
    el.innerHTML = '<div class="flex" style="justify-content:space-between"><b>$' + (D.raised || 0).toLocaleString() + ' raised</b><span class="muted">Goal $' + (D.goal || 0).toLocaleString() + "</span></div>" +
      '<div class="bar" style="margin-top:8px"><i style="width:' + Math.max(pct, 2) + '%"></i></div>' +
      '<p class="form-note">' + (D.raised ? pct + "% funded — thank you!" : "Be one of the first supporters — every dollar is tracked publicly here.") + "</p>";
  });
  $$("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = $("#pledge-form"); if (!f) return;
      f.querySelector("[name=amount]").value = b.getAttribute("data-amount");
      f.querySelector("[name=tier]").value = b.getAttribute("data-tier") || "";
      f.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });

  /* ---- Share ---- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.getAttribute("data-share") || document.title, u = location.href;
      if (navigator.share) navigator.share({ title: t, url: u }).catch(function () { });
      else { try { navigator.clipboard.writeText(u); b.textContent = "Link copied ✓"; } catch (e) { } }
      track("share", { item: t });
    });
  });

  /* ---- Back to top + exit-intent lead modal (desktop, once per session) ---- */
  var top = $(".to-top");
  window.addEventListener("scroll", function () { top && top.classList.toggle("show", scrollY > 700); }, { passive: true });
  top && top.addEventListener("click", function () { scrollTo({ top: 0, behavior: "smooth" }); });
  var modal = $("#exit-modal");
  if (modal && matchMedia("(pointer:fine)").matches) {
    document.addEventListener("mouseout", function (e) {
      if (e.clientY < 8 && !e.relatedTarget && !sstore("exitShown") && !sstore("leadDone")) { modal.classList.add("show"); sstore("exitShown", "1"); track("exit_modal"); }
    });
  }
  $$("[data-close-modal]").forEach(function (b) { b.addEventListener("click", function () { b.closest(".modal").classList.remove("show"); }); });
  $$(".modal").forEach(function (m) { m.addEventListener("click", function (e) { if (e.target === m) m.classList.remove("show"); }); });
})();
