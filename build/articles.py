"""Article loading + rendering."""
import os, re, json, markdown
from layout import page, ICONS, CATS, esc, SITE, UPDATED, kit_form, help_strip

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART_DIR = os.path.join(ROOT, "content", "articles")

# Editorial order on hubs
ORDER = ["what-is-puberty", "puberty-timeline", "puberty-changes-girls", "puberty-changes-boys", "first-period-guide",
         "growth-spurts-voice-body-hair", "acne-and-skin-care", "hygiene-guide", "emotions-and-mood-swings",
         "body-image-confidence", "sleep-food-movement", "early-or-late-puberty", "puberty-myths-vs-facts",
         "first-period-kit-checklist", "talking-to-your-child-about-puberty", "body-safety-and-privacy",
         "puberty-and-neurodivergent-kids", "teaching-puberty-in-the-classroom"]

# Matching video per article (YouTube IDs, see videos.py)
ART_VIDEO = {
    "what-is-puberty": "IAIpqX5V2Jg", "puberty-timeline": "DdadICiLZZ4", "puberty-changes-girls": "FKHHjIVpuB8",
    "puberty-changes-boys": "4tF4cB4B7Do", "first-period-guide": "QPtKavUGbGc", "hygiene-guide": "3yQUVlNsRT0",
    "acne-and-skin-care": "QPoN03EYIaw", "growth-spurts-voice-body-hair": "4SRXvGHKA-k",
    "emotions-and-mood-swings": "-WF6NzZpHhc", "sleep-food-movement": "00BYyDr8Xdg",
}


def parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    meta_txt, body = m.group(1), m.group(2)
    meta = {"faq": [], "source": []}
    for line in meta_txt.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if k == "faq" and "::" in v:
            q, a = v.split("::", 1)
            meta["faq"].append((q.strip(), a.strip()))
        elif k == "source" and "|" in v:
            n, u = v.split("|", 1)
            meta["source"].append((n.strip(), u.strip()))
        else:
            meta[k] = v
    meta["slug"] = os.path.splitext(os.path.basename(path))[0]
    meta["body"] = body
    meta["words"] = len(body.split())
    return meta


def load():
    arts = {}
    for f in os.listdir(ART_DIR):
        if f.endswith(".md"):
            a = parse(os.path.join(ART_DIR, f))
            arts[a["slug"]] = a
    ordered = [arts[s] for s in ORDER if s in arts] + [a for s, a in arts.items() if s not in ORDER]
    return ordered


def card(a, r):
    icon, color, tag = CATS.get(a["category"], ("book", "brand", "t-brand"))
    return f'''<a class="card article-card" href="{r}learn/{a["slug"]}.html" data-cat="{esc(a["category"])} {esc(a["audience"])}">
  <div class="thumb bg-{color}">{ICONS[icon]}</div>
  <div class="body"><div class="meta"><span class="tag {tag}">{esc(a["category"])}</span><span>{a["read_minutes"]} min read</span></div>
  <h3>{esc(a["title"])}</h3><p>{esc(a["description"])}</p></div></a>'''


def render(a, all_arts):
    r = "../"
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists"])
    html = md.convert(a["body"])
    # inject a mid-article CTA after the 3rd H2
    parentish = a["audience"] in ("Parents", "Educators") or a["category"] in ("For Parents", "For Educators")
    if parentish:
        cta = f'''<div class="callout kit"><h3>Free: the Puberty Talk Starter Kit</h3><p>Age-by-age scripts, a first-period kit list, a boys' checklist and 40 question-jar cards — printable, for parents and educators.</p><a class="btn btn-primary" href="#" data-open-kit>Get the free kit {ICONS["arrow"]}</a></div>'''
    else:
        cta = f'''<div class="callout ask"><h3>Got a question you don't want to ask out loud?</h3><p>Ask it anonymously — no name, no email. We answer the most common questions in plain language.</p><a class="btn btn-primary" href="{r}ask.html">Ask anonymously {ICONS["arrow"]}</a></div>'''
    parts = re.split(r"(?=<h2)", html)
    if len(parts) > 4:
        parts.insert(4, cta)
    html = "".join(parts)
    # video embed after key takeaways list
    vid = ART_VIDEO.get(a["slug"])
    if vid:
        v = f'<figure style="margin:28px 0"><button class="yt" data-id="{vid}" aria-label="Play video: {esc(a["title"])}" style="border-radius:16px;overflow:hidden"></button><figcaption class="muted" style="font-size:14px;margin-top:8px">Watch: a short explainer video on this topic (hosted on YouTube).</figcaption></figure>'
        html = re.sub(r"(<h2 id=\"key-takeaways\">.*?</ul>)", lambda m: m.group(1) + v, html, count=1, flags=re.S)
    toc_items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    toc = "".join(f'<a href="#{i}">{re.sub("<.*?>", "", t)}</a>' for i, t in toc_items)
    icon, color, tag = CATS.get(a["category"], ("book", "brand", "t-brand"))
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q, ans in a["faq"])
    src_html = "".join(f'<li>{esc(n)} — <a href="{esc(u)}" target="_blank" rel="noopener nofollow">{esc(u.replace("https://", "").replace("www.", "").rstrip("/"))}</a></li>' for n, u in a["source"])
    same = [x for x in all_arts if x["category"] == a["category"] and x["slug"] != a["slug"]]
    others = [x for x in all_arts if x["slug"] != a["slug"] and x not in same]
    related = (same + others)[:3]
    rel_html = "".join(card(x, r) for x in related)
    # Linked resources for the three audiences (teen / parent / educator)
    trio = f'''<div class="card"><h4>Use this topic at home &amp; in class</h4>
      <ul class="ticks dark" style="margin:10px 0 0;font-size:15px">
      <li><a href="{r}learn/talking-to-your-child-about-puberty.html">Parent conversation guide</a></li>
      <li><a href="{r}tools/conversation-starters.html">Conversation-starter generator</a></li>
      <li><a href="{r}learn/teaching-puberty-in-the-classroom.html">Classroom teaching guide</a></li>
      <li><a href="{r}schools.html">Free resources for your school</a></li></ul></div>'''
    url = f"{SITE}/learn/{a['slug']}.html"
    schema = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["description"],
         "mainEntityOfPage": url, "dateModified": "2026-10-19", "datePublished": "2026-10-19",
         "author": {"@type": "Organization", "name": "Puberty101.com Editorial Team", "url": SITE + "/about.html"},
         "publisher": {"@type": "Organization", "name": "Puberty101.com", "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.svg"}},
         "keywords": a.get("keywords", ""), "wordCount": a["words"], "audience": {"@type": "Audience", "audienceType": a["audience"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Learn", "item": SITE + "/learn/"},
            {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
    ]
    body = f'''<div class="progress" aria-hidden="true"></div>
<section class="article-hero"><div class="container">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">Home</a> / <a href="{r}learn/">Learn</a> / <span>{esc(a["category"])}</span></nav>
  <span class="tag {tag}">{esc(a["category"])}</span>
  <h1 class="mt-1" style="max-width:900px">{esc(a["title"])}</h1>
  <p class="muted" style="font-size:1.12rem;max-width:760px">{esc(a["description"])}</p>
  <div class="byline"><span>By the Puberty101 Editorial Team</span><i class="dot"></i><span>Updated {UPDATED}</span><i class="dot"></i><span>{a["read_minutes"]} min read</span><i class="dot"></i><span>For {esc(a["audience"])}</span></div>
  <div class="share mt-2 no-print"><button class="btn btn-ghost btn-sm" data-share>{ICONS["share"]} Share</button><button class="btn btn-ghost btn-sm" data-print>{ICONS["print"]} Print</button></div>
</div></section>
<div class="container article-layout">
  <article>
    <div class="prose">{html}</div>
    <h2 class="mt-4" style="font-size:1.5rem">Frequently asked questions</h2>
    <div class="faq">{faq_html}</div>
    <div class="card mt-3"><h4>Sources &amp; further reading</h4><p class="sources" style="margin-bottom:8px">This guide was written in line with public guidance from the organizations below. It is reviewed regularly; spot an error? <a href="{r}contact.html">Tell us</a> and we'll correct it.</p><ul class="sources">{src_html}</ul></div>
    <div class="mt-3">{help_strip(r)}</div>
    <p class="muted mt-2" style="font-size:13.5px">This article is general education, not medical advice. If you're worried about your health or your child's, talk to a doctor or nurse.</p>
  </article>
  <aside class="toc no-print">
    <div class="card"><h4>On this page</h4><nav aria-label="Table of contents">{toc}</nav></div>
    {trio}
    <div class="card" style="background:linear-gradient(150deg,#2a1b7a,#5b3fd6);color:#fff;border:0"><h4 style="color:#fff">Free starter kit</h4><p style="font-size:14.5px;color:#e6e1ff">Printable scripts &amp; checklists for parents and teachers.</p><a class="btn btn-sun btn-sm btn-block" href="#" data-open-kit>Get it free</a></div>
  </aside>
</div>
<section class="bg-soft section-tight"><div class="container"><h2 style="font-size:1.6rem">Keep reading</h2><div class="grid g3 mt-2">{rel_html}</div></div></section>'''
    return page(f"learn/{a['slug']}.html", a["title"], a["description"], body, active="Learn", schema=schema, og_type="article")


def hub(arts):
    r = "../"
    cats = ["Body Changes", "Periods", "Health & Hygiene", "Feelings & Mind", "For Parents", "For Educators"]
    chips = '<button class="chip active" data-filter="all">All guides</button>' + "".join(
        f'<button class="chip" data-filter="{esc(c)}">{esc(c)}</button>' for c in cats) + \
        '<button class="chip" data-filter="Teens">For teens</button><button class="chip" data-filter="Parents">For parents</button>'
    cards = "".join(card(a, r) for a in arts)
    body = f'''<section class="page-hero"><div class="container">
<nav class="crumbs"><a href="{r}index.html">Home</a> / <span>Learn</span></nav>
<span class="eyebrow">{ICONS["book"].replace("<svg", '<svg style="width:14px;height:14px"')} The Puberty101 library</span>
<h1 class="mt-2">Every puberty question, answered plainly</h1>
<p>{len(arts)} in-depth guides on body changes, periods, hygiene, feelings, body safety and more — written for teens, parents and educators, in line with guidance from pediatric and public-health organizations.</p>
<div class="chips mt-3" data-filter-group="#lib">{chips}</div>
</div></section>
<section class="section-tight"><div class="container"><div class="grid g3" id="lib">{cards}</div></div></section>'''
    schema = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Puberty guides", "url": SITE + "/learn/",
              "hasPart": [{"@type": "Article", "headline": a["title"], "url": f"{SITE}/learn/{a['slug']}.html"} for a in arts]}
    return page("learn/index.html", "Puberty Guides for Teens, Parents & Educators",
                "Plain-language puberty guides: body changes, first periods, voice changes, acne, hygiene, moods, body safety and how to talk about it all.",
                body, active="Learn", schema=schema)
