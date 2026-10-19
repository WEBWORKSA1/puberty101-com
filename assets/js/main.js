/* Puberty101.com — core interactions */
(function () {
  "use strict";
  var d = document, w = window;

  // ---- Contact routing (address assembled at runtime, never printed on the page) ----
  var _k = [119,101,98,119,111,114,107,115,97,49,64,103,109,97,105,108,46,99,111,109];
  function inbox() { return String.fromCharCode.apply(null, _k); }
  w.P101 = w.P101 || {};
  // Optional: after FormSubmit activation, paste the random alias it emails you here to stop using the address entirely.
  w.P101.formAlias = "";
  function endpoint() { return "https://formsubmit.co/ajax/" + (w.P101.formAlias || inbox()); }

  d.querySelectorAll("[data-mail]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-subject") || "Puberty101.com enquiry";
      w.location.href = "mai" + "lto:" + inbox() + "?subject=" + encodeURIComponent(subj);
    });
  });

  // ---- Theme ----
  var root = d.documentElement;
  try { var t = localStorage.getItem("p101-theme"); if (t) root.setAttribute("data-theme", t); } catch (e) {}
  d.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = root.getAttribute("data-theme") || (w.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var next = cur === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("p101-theme", next); } catch (e) {}
    });
  });

  // ---- Mobile menu ----
  var mb = d.querySelector("[data-menu-toggle]"), mm = d.getElementById("mobile-menu");
  if (mb && mm) mb.addEventListener("click", function () {
    var open = mm.classList.toggle("open"); mb.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // ---- Year ----
  d.querySelectorAll("[data-year]").forEach(function (n) { n.textContent = new Date().getFullYear(); });

  // ---- Toast ----
  function toast(msg) {
    var t = d.getElementById("toast"); if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 3200);
  }
  w.P101.toast = toast;

  // ---- Cookie notice ----
  var ck = d.getElementById("cookie");
  try { if (ck && !localStorage.getItem("p101-cookie")) setTimeout(function () { ck.classList.add("show"); }, 900); } catch (e) {}
  d.querySelectorAll("[data-cookie]").forEach(function (b) {
    b.addEventListener("click", function () {
      try { localStorage.setItem("p101-cookie", b.getAttribute("data-cookie")); } catch (e) {}
      ck.classList.remove("show");
    });
  });

  // ---- Forms (AJAX to FormSubmit) ----
  function serialize(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (data[k]) data[k] += ", " + v; else data[k] = v;
    });
    return data;
  }
  d.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var st = form.querySelector(".form-status");
      var hp = form.querySelector("[name=_honey]");
      if (hp && hp.value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = serialize(form);
      data._subject = "[Puberty101.com] " + form.getAttribute("data-form");
      data._template = "table";
      data._captcha = "false";
      data.Page = location.pathname;
      delete data._honey;
      var btn = form.querySelector("[type=submit]");
      if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
      if (st) { st.className = "form-status"; st.textContent = ""; }
      fetch(endpoint(), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().catch(function () { return {}; }); })
        .then(function () { done(true); })
        .catch(function () { done(false); });
      function done(ok) {
        if (btn) { btn.disabled = false; btn.textContent = btn._t; }
        if (ok) {
          var msg = form.getAttribute("data-success") || "Thank you — we received your message.";
          if (st) { st.className = "form-status ok"; st.textContent = msg; }
          toast("Sent ✓");
          try { sessionStorage.setItem("p101-lead", "1"); } catch (e) {}
          var next = form.getAttribute("data-next");
          form.reset();
          if (next) setTimeout(function () { location.href = next; }, 900);
        } else if (st) {
          st.className = "form-status err";
          st.textContent = "Something went wrong. Please check your connection and try again.";
        }
      }
    });
  });

  // ---- Multi-step forms ----
  d.querySelectorAll("[data-steps]").forEach(function (form) {
    var steps = form.querySelectorAll(".step"), bars = form.querySelectorAll(".steps-bar i"), i = 0;
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
      bars.forEach(function (b, k) { b.classList.toggle("on", k <= n); });
      i = n;
    }
    form.addEventListener("click", function (e) {
      var nx = e.target.closest("[data-next-step]"), pv = e.target.closest("[data-prev-step]");
      if (nx) {
        var ok = true;
        steps[i].querySelectorAll("input,select,textarea").forEach(function (f) { if (ok && !f.checkValidity()) { f.reportValidity(); ok = false; } });
        if (ok && i < steps.length - 1) show(i + 1);
      }
      if (pv && i > 0) show(i - 1);
    });
    show(0);
  });

  // ---- Lite YouTube ----
  d.querySelectorAll(".yt[data-id]").forEach(function (b) {
    var id = b.getAttribute("data-id");
    b.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    b.addEventListener("click", function () {
      if (b.classList.contains("playing")) return;
      var f = d.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label") || "Video";
      f.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      b.appendChild(f); b.classList.add("playing");
    });
  });

  // ---- Filters (chips) ----
  d.querySelectorAll("[data-filter-group]").forEach(function (g) {
    var target = d.querySelector(g.getAttribute("data-filter-group"));
    g.addEventListener("click", function (e) {
      var c = e.target.closest("[data-filter]"); if (!c || !target) return;
      g.querySelectorAll("[data-filter]").forEach(function (x) { x.classList.toggle("active", x === c); });
      var v = c.getAttribute("data-filter");
      target.querySelectorAll("[data-cat]").forEach(function (it) {
        it.style.display = (v === "all" || it.getAttribute("data-cat").indexOf(v) > -1) ? "" : "none";
      });
    });
  });

  // ---- Reading progress + TOC highlight ----
  var prog = d.querySelector(".progress"), prose = d.querySelector(".prose");
  if (prog && prose) {
    var heads = prose.querySelectorAll("h2[id]"), links = d.querySelectorAll(".toc nav a");
    w.addEventListener("scroll", function () {
      var r = prose.getBoundingClientRect(), h = prose.offsetHeight - w.innerHeight;
      prog.style.width = Math.max(0, Math.min(100, (-r.top / (h || 1)) * 100)) + "%";
      var cur = "";
      heads.forEach(function (hh) { if (hh.getBoundingClientRect().top < 140) cur = hh.id; });
      links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + cur); });
    }, { passive: true });
  }

  // ---- Share / copy ----
  d.querySelectorAll("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var u = location.href, ti = d.title;
      if (navigator.share) navigator.share({ title: ti, url: u }).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(u).then(function () { toast("Link copied"); });
    });
  });
  d.querySelectorAll("[data-print]").forEach(function (b) { b.addEventListener("click", function () { w.print(); }); });

  // ---- Lead modal (exit intent on desktop, once per session) + mobile sticky CTA ----
  var modal = d.getElementById("kit-modal");
  function seen() { try { return sessionStorage.getItem("p101-modal") || sessionStorage.getItem("p101-lead"); } catch (e) { return false; } }
  function openModal() {
    if (!modal || seen()) return;
    modal.classList.add("show");
    try { sessionStorage.setItem("p101-modal", "1"); } catch (e) {}
  }
  if (modal && !d.body.hasAttribute("data-no-modal")) {
    d.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 8) openModal(); });
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest("[data-close]")) modal.classList.remove("show"); });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape") modal.classList.remove("show"); });
  }
  d.querySelectorAll("[data-open-kit]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); if (modal) { modal.classList.add("show"); } }); });
  var sticky = d.getElementById("sticky-cta");
  if (sticky) {
    var dismissed = false;
    try { dismissed = !!sessionStorage.getItem("p101-sticky"); } catch (e) {}
    if (!dismissed) w.addEventListener("scroll", function () { if (w.scrollY > 900 && !seen()) sticky.classList.add("show"); }, { passive: true });
    var sx = sticky.querySelector(".x");
    if (sx) sx.addEventListener("click", function () { sticky.classList.remove("show"); try { sessionStorage.setItem("p101-sticky", "1"); } catch (e) {} });
  }

  // ---- Donation amount picker ----
  d.querySelectorAll("[data-amounts]").forEach(function (g) {
    var input = d.querySelector(g.getAttribute("data-amounts"));
    g.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-amt]"); if (!b) return;
      e.preventDefault();
      g.querySelectorAll("button").forEach(function (x) { x.classList.toggle("on", x === b); });
      if (input) input.value = b.getAttribute("data-amt");
    });
  });
})();
