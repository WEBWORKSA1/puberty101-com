"""Build Puberty101.com into the repo root.  Run:  python3 build/build.py"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import SITE, LOGO
import articles, tools, pages

OG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#5b3fd6"/><stop offset="1" stop-color="#0f8a8a"/></linearGradient></defs>'
      '<rect width="1200" height="630" fill="url(#g)"/><g transform="translate(80 90) scale(3.75)">' + LOGO.replace('<svg viewBox="0 0 40 40" aria-hidden="true">', "").replace("</svg>", "").replace('id="lg"', 'id="lg2"').replace("url(#lg)", "#ffffff22") + '</g>'
      '<text x="80" y="370" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="92" fill="#fff">Puberty101.com</text>'
      '<text x="80" y="440" font-family="Arial,Helvetica,sans-serif" font-size="40" fill="#ece9ff">Puberty, explained — for teens, parents &amp; educators.</text>'
      '<text x="80" y="540" font-family="Arial,Helvetica,sans-serif" font-size="38" fill="#ffc23d">Free guides · Interactive tools · Videos</text></svg>')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    arts = articles.load()
    out = {}
    out["index.html"] = pages.home(arts)
    out["learn/index.html"] = articles.hub(arts)
    for a in arts:
        out[f"learn/{a['slug']}.html"] = articles.render(a, arts)
    out.update(tools.all_tools())
    out["videos.html"] = pages.videos()
    out["ask.html"] = pages.ask()
    out["parents.html"] = pages.parents(arts)
    out["schools.html"] = pages.schools()
    out["kit.html"] = pages.kit()
    out["support.html"] = pages.support()
    out["contests.html"] = pages.contests()
    out["careers.html"] = pages.careers()
    out["advertise.html"] = pages.advertise()
    out["about.html"] = pages.about()
    out["editorial-policy.html"] = pages.editorial()
    out["contact.html"] = pages.contact()
    out["resources.html"] = pages.resources()
    out["search.html"] = pages.search()
    out.update(pages.legal_pages())
    nf = pages.notfound()
    # 404 can be served from any depth: make asset/link paths root-absolute
    nf = re.sub(r'(href|src)="(?!https?:|/|#|mailto)', r'\1="/', nf)
    out["404.html"] = nf

    for k, v in out.items():
        write(k, v)

    # search index
    idx = [{"t": a["title"], "d": a["description"], "k": a.get("keywords", "") + " " + a["category"], "u": f"learn/{a['slug']}.html"} for a in arts]
    idx += [{"t": t, "d": d, "k": "tool interactive", "u": f"tools/{f}"} for f, t, d, _, _ in tools.TOOLS]
    idx += [{"t": t, "d": d, "k": k, "u": u} for t, d, k, u in [
        ("Video library", "Short puberty explainer videos.", "video watch youtube", "videos.html"),
        ("Ask anonymously", "Send a puberty question with no name or email.", "question anonymous ask", "ask.html"),
        ("Parent hub & free starter kit", "Scripts and tips for talking about puberty.", "parent talk kit", "parents.html"),
        ("Resources for schools", "Lesson resources, parent nights, workshops and kits.", "school teacher educator classroom", "schools.html"),
        ("Helplines", "Youth helplines and trusted organizations.", "help crisis hotline", "resources.html"),
        ("Support us", "Donate or sponsor free puberty education.", "donate support", "support.html")]]
    for t, d in tools.GLOSSARY:
        idx.append({"t": f"{t} (glossary)", "d": d, "k": "glossary definition", "u": "tools/glossary.html#" + t.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("'", "")})
    write("search-index.json", json.dumps(idx, ensure_ascii=False))

    # sitemap (exclude noindex pages)
    skip = {"404.html", "kit.html", "search.html"}
    urls = []
    for k in sorted(out):
        if k in skip:
            continue
        loc = SITE + "/" + (k[:-10] if k.endswith("index.html") else k)
        pri = "1.0" if k == "index.html" else ("0.8" if k.startswith("learn/") or k.startswith("tools/") else "0.6")
        urls.append(f"<url><loc>{loc}</loc><lastmod>2026-10-19</lastmod><priority>{pri}</priority></url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /kit.html\nDisallow: /search.html\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("ads.txt", "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    write("CNAME", "puberty101.com\n")
    write(".nojekyll", "")
    write("site.webmanifest", json.dumps({"name": "Puberty101.com", "short_name": "Puberty101", "start_url": "/", "display": "standalone",
                                          "background_color": "#fffdf8", "theme_color": "#5b3fd6",
                                          "icons": [{"src": "/assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))
    write("assets/img/logo.svg", LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
    write("assets/img/og.svg", OG)
    print(f"Built {len(out)} pages, {len(arts)} articles, {len(idx)} index entries.")


if __name__ == "__main__":
    main()
