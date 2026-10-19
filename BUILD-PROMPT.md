# Puberty101.com — Strategy & Phase-Wise Build Prompt

## 1. The idea (and why this one)

**Position:** the one puberty resource that serves all three people in the conversation — the **teen**, the **parent**, the **educator** — with linked content on every topic, interactive tools, and a B2B school channel.

Competitive sweep of 40 niche sites (KidsHealth, AMAZE, NHS, AAP/HealthyChildren, Brook, Girlology, Young Men's Health, Kotex, Always, Days for Girls, YoungMinds, Kids Help Phone, Clue, PERIOD., Childline, Raising Children, and more) found five open gaps this build targets:

| Gap found | How Puberty101.com fills it |
|---|---|
| Teen, parent and school content live in silos | Every guide links to parent scripts + classroom guide + school resources |
| Interactive tools are rare (~12–20% of sites) | 6 tools: body-changes explorer, period predictor, quiz, kit builder, conversation starters, glossary |
| No downloadable, age-banded parent scripts | Gated **Puberty Talk Starter Kit** (lead magnet) |
| Boys' puberty under-served | Dedicated boys' guide, boys' checklist, boys' videos |
| Stale trust signals; anonymous Q&A rare | "Updated" dates, sources per guide, editorial policy, anonymous question box |

### Revenue model — ranked by expected value

| Stream | Mechanism | Why it matters |
|---|---|---|
| **1. Brand sponsorships** | Period-care, personal-care, pediatric telehealth brands sponsor hubs, kits, video series, contests | Highest ceiling. Kotex, Always, Dove already fund school curricula — this is where they spend. |
| **2. School / district leads (B2B)** | 4-step request form → workshops, staff training, custom kits, sponsor-funded programs | One district deal can out-earn a year of display ads. |
| **3. Google AdSense** | Auto ads on evergreen guides | The floor. Health is a strong-RPM vertical, but teen-adjacent audiences and family-safe ad filtering pull RPM down. |
| **4. Email list** | Starter Kit + newsletter → sponsor inventory + product launches | Owned audience; multiplies 1 and 2. |
| **5. Donations** | Monthly/one-time tiers, directed gifts, sponsor-a-classroom | Small but sticky; strong for mission credibility. |

### Rough traffic → revenue scenarios (AdSense only, illustrative)

Assumptions: blended page RPM $6–12 (US/CA/UK-heavy parent traffic; teen traffic monetizes lower), 1.6 pages/session.

| Monthly pageviews | AdSense @ $6 RPM | AdSense @ $12 RPM |
|---|---|---|
| 25,000 | $150 | $300 |
| 100,000 | $600 | $1,200 |
| 500,000 | $3,000 | $6,000 |

AdSense alone is a thin business. The asset value is in **sponsorship + school leads + list**: a single category sponsor at $1–5k/month or one district program typically exceeds 100k-pageview AdSense revenue. Build traffic for the ads; build the business on the leads.

### Risks you must manage
- **YMYL health content:** Google weighs expertise heavily. Adding a named, credentialed medical reviewer (physician, NP or RN) to guides is the single biggest ranking/approval lever not yet in place.
- **Minors:** content is clinical and age-appropriate; lead forms are adult-only (18+ checkbox); the question box collects no personal data; site states it is not directed to under-13s (COPPA). Keep it that way.
- **AdSense approval:** needs the custom domain live, ~15–30 substantive original pages (18 guides + tools + policy pages are in place), privacy policy with AdSense disclosures, ads.txt, clear navigation. All done.

---

## 2. Phase-wise build prompt (reusable)

> Copy each phase into your AI builder in order. Each phase assumes the previous one is complete.

### Phase 0 — Strategy & research
"Research at least 35 leading puberty, adolescent-health, period-education and child-safety websites (KidsHealth, AMAZE, NHS, AAP HealthyChildren, Brook, Girlology, Young Men's Health, Center for Young Women's Health, Kotex, Always, Days for Girls, PERIOD., YoungMinds, Childline, NSPCC, Kids Help Phone, Raising Children Network, Clue, Common Sense Media, WHO, UNICEF Parenting, etc.). For each, record audience, navigation, signature features, lead capture, donation mechanics, monetization, design and trust signals. Output a feature-frequency matrix, top topics, best lead/donation patterns and 5 gaps nobody fills well. Recommend the positioning and revenue model for the domain Puberty101.com."

### Phase 1 — Foundation & design system
"Build a static, GitHub-Pages-compatible website for Puberty101.com using a Python build script (build/build.py) that renders HTML from templates and Markdown. Create a modern, friendly, trustworthy design system: violet brand (#5b3fd6), teal, coral and sunshine accents; Bricolage Grotesque headings + Inter body; rounded cards; light/dark mode; fully responsive with no horizontal scroll at 390px; accessible (skip link, focus states, ARIA, reduced motion). Every page must show a top bar reading 'Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership' linked to https://web.works/contact. Include the AdSense script `ca-pub-6620975821265271` in the <head> of every content page, plus `<meta name="google-adsense-account">`. Add ads.txt, robots.txt, sitemap.xml, CNAME, .nojekyll, web manifest, favicon, OG image, and JSON-LD (Organization, WebSite+SearchAction, Article, FAQPage, BreadcrumbList)."

### Phase 2 — Content library
"Write 18 original, medically accurate, age-appropriate guides (1,000–1,300 words each) in line with AAP, NHS, WHO, CDC and KidsHealth guidance: What Is Puberty, Puberty Timeline, Puberty for Girls, Puberty for Boys, First Period, Growth Spurts/Voice/Body Hair, Acne, Hygiene, Mood Swings, Body Image, Sleep/Food/Movement, Early or Late Puberty, Myths vs Facts, First-Period Kit, Talking to Your Child, Body Safety & Privacy, Neurodivergent Kids, Teaching Puberty in the Classroom. Each: intro, Key Takeaways, tables where useful, 'when to see a doctor', bottom line, 3 FAQs (FAQ schema), 3–5 authoritative sources. Clinical, never sexualized. Render with sticky table of contents, reading-progress bar, share/print, a matching YouTube video (privacy-enhanced, click-to-load), a mid-article CTA (parents → Starter Kit; teens → anonymous question), helpline strip, related guides and parent/educator cross-links."

### Phase 3 — Interactive tools
"Build 6 client-side tools with no data leaving the device: Body Changes Explorer (girls/boys toggle + age slider showing typical changes), Period Predictor (next 6 estimated periods), 12-question Myth-or-Fact quiz with score and share, printable First-Period Kit Builder (saves to localStorage), age-banded Conversation Starter generator, and a searchable 60+ term glossary (DefinedTermSet schema). Add a tools hub and client-side site search backed by search-index.json."

### Phase 4 — Lead generation engine
"Create high-converting, adult-only lead capture: (a) the Puberty Talk Starter Kit lead magnet (name, email, role, child age, interests, 18+ consent) that redirects to a printable kit page; (b) a 4-step school/organization request form (role → organization → needs, timeline, budget → contact) with progress bar; (c) exit-intent modal on desktop and a sticky mobile CTA, once per session; (d) footer newsletter; (e) inline kit CTAs inside parent articles. Route ALL submissions via FormSubmit AJAX to a single inbox whose address is assembled at runtime in JavaScript and never appears in page HTML or text. Include honeypot spam protection and success states."

### Phase 5 — Monetization & community
"Build: Support page (monthly/one-time toggle, preset amounts, tiers, directed giving to operations/promotions/marketing/hiring/contests, planned-allocation bars, in-kind donations, honest 'not tax-deductible' note, config slots for PayPal/Stripe/Buy Me a Coffee links with pledge-form fallback); Contests page (3 challenges, official rules, adult-submitted entries, prize-sponsor CTA); Careers page (medical reviewers, writers, illustrators, video creators, school ambassadors, translators + application form); Advertise page (packages, brand-safety standards, media-kit form, domain-acquisition link); Video library with category filters; anonymous Ask page with FAQ schema; Helplines & resources page."

### Phase 6 — Trust, compliance & legal
"Add About, Editorial & Advertising Policy (sources, review cadence, corrections, ad separation, banned ad categories), Contact (form + click-to-email that never reveals the address), Privacy Policy (AdSense/Google cookie disclosures, opt-out links, FormSubmit, YouTube, children's privacy/COPPA, GDPR/CCPA/PIPEDA rights), Cookie Policy with consent banner, Terms of Use, and Disclaimer with a full trademark/copyright disclosure stating no affiliation with any entity using 'Puberty 101'/'Puberty101'. Add medical disclaimer to every page footer."

### Phase 7 — QA & launch
"Verify: zero broken internal links; the inbox address appears nowhere in built files; AdSense script on all content pages, absent on 404/search; no horizontal scroll at 390px; no console errors; forms submit. Push to GitHub repo WEBWORKSA1/puberty101-com (branch main), enable GitHub Pages (Deploy from branch → main → /root), set custom domain puberty101.com with HTTPS, then apply to AdSense and submit sitemap in Search Console."

### Phase 8 — Growth (post-launch)
"Add a named medical reviewer to every guide; publish 2 new guides per week from top Ask questions; translate top 10 guides to Spanish and Hindi; launch the sponsor outreach list (period-care, deodorant, skincare, pediatric telehealth brands); pitch 50 school districts with the free resource pack; commission original animated videos; add a Puberty101 YouTube channel and Pinterest boards for parent printables."

---

## 3. Launch checklist
1. GitHub → repo Settings → Pages → Source: **Deploy from a branch** → `main` / `(root)` → Save.
2. DNS at registrar: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `www` CNAME → `webworksa1.github.io`. Then tick **Enforce HTTPS**.
3. Submit any form once and click **Activate** in the FormSubmit email (one-time). Optionally paste the random alias FormSubmit gives you into `P101.formAlias` in `assets/js/main.js`.
4. Add payment links to `DONATE_LINKS` in `build/layout.py` and run `python3 build/build.py`.
5. Google Search Console → add property → submit `sitemap.xml`. Then apply in AdSense.
