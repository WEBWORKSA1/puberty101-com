"""Shared layout + components for Puberty101.com (static, GitHub Pages)."""
import json, html

SITE = "https://puberty101.com"
NAME = "Puberty101.com"
SHORT = "Puberty101"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
CONTACT_URL = "https://web.works/contact"
UPDATED = "October 2026"

# Fill these in to switch donate buttons from "pledge" to direct payment. Leave "" to use the pledge form.
DONATE_LINKS = {"PayPal": "", "Buy Me a Coffee": "", "Stripe": ""}


def S(p, sw=2):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'


ICONS = {
    "sprout": S('<path d="M12 21v-9"/><path d="M12 12c0-4 3-7 8-7 0 5-3 8-8 7z"/><path d="M12 14c0-3-2.5-5.5-7-5.5 0 4 2.5 6 7 5.5z"/>'),
    "drop": S('<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>'),
    "heart": S('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>'),
    "sparkle": S('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 17l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>'),
    "users": S('<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 3.1a4 4 0 0 1 0 7.8M22 21a7 7 0 0 0-4-6.3"/>'),
    "school": S('<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5M22 9v6"/>'),
    "chat": S('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01"/>'),
    "play": S('<rect x="2" y="5" width="20" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/>'),
    "tool": S('<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>'),
    "calendar": S('<rect x="3" y="4" width="18" height="17" rx="3"/><path d="M8 2v4M16 2v4M3 10h18"/>'),
    "quiz": S('<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17h.01"/>'),
    "book": S('<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/><path d="M20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/>'),
    "check": S('<path d="M20 6L9 17l-5-5"/>', 2.5),
    "shield": S('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>'),
    "gift": S('<path d="M20 12v10H4V12M2 7h20v5H2zM12 22V7M12 7H7.5a2.5 2.5 0 1 1 0-5C11 2 12 7 12 7zM12 7h4.5a2.5 2.5 0 1 0 0-5C13 2 12 7 12 7z"/>'),
    "trophy": S('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>'),
    "mega": S('<path d="M3 11v2a1 1 0 0 0 1 1h3l5 4V6L7 10H4a1 1 0 0 0-1 1zM16 8a5 5 0 0 1 0 8M19 5a9 9 0 0 1 0 14"/>'),
    "brief": S('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>'),
    "moon": S('<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>'),
    "search": S('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    "menu": S('<path d="M4 7h16M4 12h16M4 17h16"/>'),
    "x": S('<path d="M18 6L6 18M6 6l12 12"/>'),
    "phone": S('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'),
    "lock": S('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),
    "print": S('<path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>'),
    "share": S('<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/>'),
    "mail": S('<rect x="2" y="4" width="20" height="16" rx="3"/><path d="M22 7l-10 7L2 7"/>'),
    "arrow": S('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "smile": S('<circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/>'),
    "leaf": S('<path d="M11 20A7 7 0 0 1 4 13C4 7 9 3 20 3c0 11-4 17-9 17z"/><path d="M4 21c4-6 8-9 12-11"/>'),
}

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#5b3fd6"/><stop offset="1" stop-color="#0f8a8a"/></linearGradient></defs>'
        '<rect width="40" height="40" rx="11" fill="url(#lg)"/>'
        '<rect x="9" y="22" width="5" height="9" rx="2.5" fill="#fff" opacity=".7"/>'
        '<rect x="17.5" y="17" width="5" height="14" rx="2.5" fill="#fff" opacity=".85"/>'
        '<rect x="26" y="12" width="5" height="19" rx="2.5" fill="#fff"/>'
        '<path d="M28.5 12c0-3 2-5 5-5 0 3-2 5-5 5z" fill="#ffc23d"/></svg>')

CATS = {
    "Body Changes": ("sprout", "brand", "t-brand"),
    "Periods": ("drop", "coral", "t-coral"),
    "Health & Hygiene": ("sparkle", "teal", "t-teal"),
    "Feelings & Mind": ("heart", "sun", "t-sun"),
    "For Parents": ("users", "mint", "t-mint"),
    "For Educators": ("school", "brand", "t-brand"),
}

NAV = [("Learn", "learn/"), ("Tools", "tools/"), ("Videos", "videos.html"), ("Parents", "parents.html"),
       ("Schools", "schools.html"), ("Ask", "ask.html")]


def esc(s):
    return html.escape(s, quote=True)


def honeypot():
    return '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'


def status():
    return '<div class="form-status" role="status" aria-live="polite"></div>'


def newsletter_form(source="Footer"):
    return f'''<form class="newsletter" data-form="Newsletter signup" data-success="You're subscribed. One useful email a month — that's it.">
  {honeypot()}<input type="hidden" name="Form" value="Newsletter ({source})">
  <label class="sr-only" for="nl-{source}">Email address</label>
  <input id="nl-{source}" type="email" name="email" placeholder="Parent or educator email" required>
  <button class="btn btn-sun" type="submit">Subscribe</button>
  {status()}
</form>'''


def kit_form(r, fid="kit", compact=False):
    """Primary B2C lead magnet: Puberty Talk Starter Kit (adults only)."""
    topics = "" if compact else '''<div class="field"><span class="label">What would help most? (optional)</span>
      <div class="radio-cards" style="grid-template-columns:repeat(auto-fit,minmax(140px,1fr))">
        <label><input type="checkbox" name="Interests" value="First period prep">First period prep</label>
        <label><input type="checkbox" name="Interests" value="Boys puberty">Boys' puberty</label>
        <label><input type="checkbox" name="Interests" value="Emotions">Moods &amp; emotions</label>
        <label><input type="checkbox" name="Interests" value="Body safety">Body safety</label>
        <label><input type="checkbox" name="Interests" value="Neurodivergent kids">Neurodivergent kids</label>
        <label><input type="checkbox" name="Interests" value="Hygiene">Hygiene habits</label>
      </div></div>'''
    return f'''<form data-form="Starter Kit request" data-next="{r}kit.html" data-success="Done! Opening your kit…">
  {honeypot()}<input type="hidden" name="Form" value="Puberty Talk Starter Kit">
  <div class="row">
    <div class="field"><label for="{fid}-name">First name</label><input id="{fid}-name" type="text" name="name" autocomplete="given-name" required></div>
    <div class="field"><label for="{fid}-email">Email</label><input id="{fid}-email" type="email" name="email" autocomplete="email" required></div>
  </div>
  <div class="row">
    <div class="field"><label for="{fid}-role">I'm a…</label><select id="{fid}-role" name="Role" required><option value="">Choose one</option><option>Parent / caregiver</option><option>Teacher / educator</option><option>School nurse / counselor</option><option>Health professional</option><option>Other adult</option></select></div>
    <div class="field"><label for="{fid}-age">Child's age</label><select id="{fid}-age" name="Child age"><option value="">Optional</option><option>7–9</option><option>10–11</option><option>12–13</option><option>14+</option><option>Several ages</option></select></div>
  </div>
  {topics}
  <label class="check"><input type="checkbox" name="Adult confirmation" value="Yes, 18+" required> I'm 18 or older and agree to receive the kit and occasional emails (unsubscribe any time).</label>
  <button class="btn btn-primary btn-block" type="submit">Send me the free kit {ICONS["arrow"]}</button>
  {status()}
  <p class="form-note">{ICONS["lock"].replace('<svg', '<svg style="width:13px;height:13px;vertical-align:-2px"')} We never sell your details. See our <a href="{r}privacy-policy.html">Privacy Policy</a>.</p>
</form>'''


def hero(title, sub, r="", crumbs=None, eyebrow=None, extra=""):
    c = ""
    if crumbs:
        c = '<nav class="crumbs" aria-label="Breadcrumb"><a href="' + r + 'index.html">Home</a>' + "".join(
            f' / <a href="{r}{h}">{t}</a>' if h else f" / <span>{t}</span>" for t, h in crumbs) + "</nav>"
    e = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'<section class="page-hero"><div class="container">{c}{e}<h1 style="margin-top:14px">{title}</h1><p>{sub}</p>{extra}</div></section>'


def help_strip(r):
    return f'''<div class="help-strip">{ICONS["phone"]}<div><strong>Need to talk to someone now?</strong> In the US call or text <b>988</b> or call Childhelp at <b>1-800-422-4453</b>. In Canada call <b>Kids Help Phone 1-800-668-6868</b> or text 686868. In the UK call <b>Childline 0800 1111</b>. In an emergency call your local emergency number. <a href="{r}resources.html">More helplines &amp; trusted organizations →</a></div></div>'''


def page(path, title, description, body, active="", scripts=(), schema=None, og_type="website",
         noindex=False, ads=True, no_modal=False, inline_js=""):
    depth = path.count("/")
    r = "../" * depth
    url_path = path[:-10] if path.endswith("index.html") else path
    canonical = f"{SITE}/{url_path}"
    full_title = title if (NAME in title or SHORT in title) else f"{title} | {NAME}"
    nav_links = "".join(
        '<a href="%s%s"%s>%s</a>' % (r, href, ' aria-current="page"' if active == label else "", label) for label, href in NAV)
    mobile = "".join(f'<a href="{r}{href}">{label}</a>' for label, href in NAV)
    base_ld = [{"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE + "/",
                "logo": SITE + "/assets/img/logo.svg",
                "description": "Independent, plain-language puberty education for teens, parents and educators."}]
    if path == "index.html":
        base_ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/",
                        "potentialAction": {"@type": "SearchAction", "target": SITE + "/search.html?q={q}",
                                            "query-input": "required name=q"}})
    if schema:
        base_ld.extend(schema if isinstance(schema, list) else [schema])
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n' for s in base_ld)
    extra_js = "".join(f'<script src="{r}{s}" defer></script>' for s in scripts)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    body_attr = ' data-no-modal' if no_modal else ''
    modal = "" if no_modal else f'''<div class="modal" id="kit-modal" role="dialog" aria-modal="true" aria-labelledby="km-t">
  <div class="box"><button class="icon-btn x" data-close aria-label="Close">{ICONS["x"]}</button>
    <span class="eyebrow">Free for parents &amp; educators</span>
    <h3 id="km-t" class="mt-2">Get the Puberty Talk Starter Kit</h3>
    <p class="muted">Age-by-age conversation scripts, a first-period kit list, a boys' puberty checklist and 40 question-jar cards. Printable.</p>
    {kit_form(r, "km", compact=True)}
  </div></div>
<div class="sticky-cta" id="sticky-cta"><span>Free puberty talk scripts for parents</span><span><a class="btn btn-sun btn-sm" href="#" data-open-kit>Get the kit</a><button class="x" aria-label="Dismiss">×</button></span></div>'''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#5b3fd6">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{r}assets/img/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/logo.svg">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
<script>try{{var t=localStorage.getItem("p101-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ADSENSE if ads else ""}
{ld}</head>
<body{body_attr}>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="{CONTACT_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="{r}index.html" aria-label="Puberty101.com home">{LOGO}<span>Puberty101<span class="tld">.com</span></span></a>
    <nav class="nav-links" aria-label="Primary">{nav_links}</nav>
    <div class="nav-cta">
      <a class="icon-btn" href="{r}search.html" aria-label="Search">{ICONS["search"]}</a>
      <button class="icon-btn" type="button" data-theme-toggle aria-label="Toggle dark mode">{ICONS["moon"]}</button>
      <a class="btn btn-coral btn-sm" href="{r}support.html">{ICONS["heart"]} Support</a>
      <button class="icon-btn menu-btn" type="button" data-menu-toggle aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">{ICONS["menu"]}</button>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu">{mobile}<a href="{r}support.html">Support / Donate</a><a href="{r}contests.html">Contests &amp; Prizes</a><a href="{r}advertise.html">Advertise &amp; Sponsor</a><a href="{r}careers.html">Join the Team</a><a href="{r}contact.html">Contact</a></div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <a class="logo" href="{r}index.html">{LOGO}<span>Puberty101<span class="tld" style="color:#a29dcb">.com</span></span></a>
        <p class="mt-2">Plain-language, judgment-free puberty education for teens, the parents who love them and the educators who teach them.</p>
        <h4 class="mt-2">The monthly parent &amp; educator note</h4>
        {newsletter_form()}
      </div>
      <div><h4>Learn</h4><ul>
        <li><a href="{r}learn/">All guides</a></li>
        <li><a href="{r}learn/puberty-changes-girls.html">Puberty for girls</a></li>
        <li><a href="{r}learn/puberty-changes-boys.html">Puberty for boys</a></li>
        <li><a href="{r}learn/first-period-guide.html">First period guide</a></li>
        <li><a href="{r}tools/">Interactive tools</a></li>
        <li><a href="{r}videos.html">Video library</a></li>
        <li><a href="{r}tools/glossary.html">Glossary</a></li>
      </ul></div>
      <div><h4>Get involved</h4><ul>
        <li><a href="{r}schools.html">For schools &amp; organizations</a></li>
        <li><a href="{r}parents.html">Free parent starter kit</a></li>
        <li><a href="{r}support.html">Donate &amp; support</a></li>
        <li><a href="{r}contests.html">Contests &amp; prizes</a></li>
        <li><a href="{r}careers.html">Join the team</a></li>
        <li><a href="{r}advertise.html">Advertise &amp; sponsor</a></li>
        <li><a href="{CONTACT_URL}" target="_blank" rel="noopener">Acquire / partner on this domain</a></li>
      </ul></div>
      <div><h4>About</h4><ul>
        <li><a href="{r}about.html">About us</a></li>
        <li><a href="{r}editorial-policy.html">Editorial &amp; ad policy</a></li>
        <li><a href="{r}resources.html">Helplines &amp; resources</a></li>
        <li><a href="{r}contact.html">Contact</a></li>
        <li><a href="{r}privacy-policy.html">Privacy Policy</a></li>
        <li><a href="{r}cookie-policy.html">Cookie Policy</a></li>
        <li><a href="{r}terms.html">Terms of Use</a></li>
        <li><a href="{r}disclaimer.html">Disclaimer &amp; Trademark Notice</a></li>
      </ul></div>
    </div>
    <div class="legal-strip">
      <p><strong>Health disclaimer:</strong> Puberty101.com provides general educational information only. It is not medical advice, diagnosis or treatment. Always talk to a doctor, nurse or other qualified health professional about your own health or your child's.</p>
      <p><strong>Trademark &amp; copyright notice:</strong> Puberty101.com is an independent publication. It is not affiliated with, endorsed by, sponsored by or connected to any organization, book, course, curriculum, product or registered trademark using the name "Puberty 101", "Puberty101" or any similar name. Third-party names, logos and trademarks belong to their respective owners and are used for identification only. Embedded videos are hosted by YouTube and remain the property of their creators.</p>
      <p>&copy; <span data-year>2026</span> Puberty101.com. All rights reserved. Original text, design and tools &copy; Puberty101.com — reproduction without permission is prohibited.</p>
    </div>
  </div>
</footer>
{modal}
<div class="cookie" id="cookie" role="dialog" aria-live="polite" aria-label="Cookie notice">
  <strong>Cookies on Puberty101.com</strong>
  <p style="margin:6px 0 0">We and our advertising partners, including Google, use cookies to show and measure ads and to improve the site. See our <a href="{r}cookie-policy.html">Cookie Policy</a>.</p>
  <div class="btns"><button class="btn btn-primary btn-sm" data-cookie="all">Accept</button><button class="btn btn-ghost btn-sm" data-cookie="essential">Essential only</button></div>
</div>
<div class="toast" id="toast" role="status"></div>
<script src="{r}assets/js/main.js" defer></script>{extra_js}{inline_js}
</body>
</html>
'''
