"""Core pages: home, hubs, lead gen, monetization, legal."""
import json
from layout import (page, hero, ICONS, esc, kit_form, newsletter_form, honeypot, status, help_strip, SITE,
                    CONTACT_URL, DONATE_LINKS, UPDATED)
from articles import card

VIDEOS = [
    ("IAIpqX5V2Jg", "Puberty: Am I Normal?", "AMAZE", "Body Changes"),
    ("DdadICiLZZ4", "Changes", "AMAZE", "Body Changes"),
    ("31y0h2LX5Ps", "What Is Puberty?", "YouTube", "Body Changes"),
    ("FKHHjIVpuB8", "Am I Normal? (Girls and Puberty)", "AMAZE", "Girls"),
    ("Z3iZQM0Xm28", "Puberty for Girls: Top 10 Things to Expect", "YouTube", "Girls"),
    ("QPtKavUGbGc", "Why Haven't I Started My Period Yet?", "AMAZE", "Periods"),
    ("4tF4cB4B7Do", "Puberty for Boys: 10 Top Things to Expect", "YouTube", "Boys"),
    ("4SRXvGHKA-k", "Puberty, Body Odor and Other Changes for Boys", "YouTube", "Boys"),
    ("3yQUVlNsRT0", "I Use Deodorant! Why Do I Still Stink?", "AMAZE", "Hygiene"),
    ("00BYyDr8Xdg", "Taking Care of Your Body During Puberty", "YouTube", "Hygiene"),
    ("QPoN03EYIaw", "Managing Acne: 10 Tips to Help Your Teen", "Mayo Clinic Health System", "Hygiene"),
    ("-WF6NzZpHhc", "How to Know if Your Teen Needs Mental Health Support", "Mayo Clinic", "Feelings"),
]


def vcard(v, cat=True):
    vid, t, ch, c = v
    return f'''<div class="card video-card" data-cat="{c}"><button class="yt" data-id="{vid}" aria-label="Play: {esc(t)}"></button>
<div class="body"><span class="tag">{c}</span><h3 style="font-size:1.05rem;margin-top:8px">{esc(t)}</h3><p class="muted" style="font-size:14px;margin:0">Source: {esc(ch)} on YouTube</p></div></div>'''


HERO_ART = '''<svg viewBox="0 0 520 470" role="img" aria-label="Illustration of a growth chart with topic cards">
<defs><linearGradient id="hg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7c62f0"/><stop offset="1" stop-color="#0f8a8a"/></linearGradient>
<linearGradient id="hg2" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ff6a55"/><stop offset="1" stop-color="#ffc23d"/></linearGradient></defs>
<path d="M70 70 Q260 -10 440 90 Q540 200 450 350 Q330 480 160 420 Q20 360 30 220 Q35 120 70 70z" fill="url(#hg1)" opacity=".14"/>
<g transform="translate(110 120)">
 <rect x="0" y="230" width="300" height="2" fill="var(--line)"/>
 <rect x="10" y="180" width="44" height="50" rx="12" fill="url(#hg1)" opacity=".45"/>
 <rect x="72" y="140" width="44" height="90" rx="12" fill="url(#hg1)" opacity=".6"/>
 <rect x="134" y="95" width="44" height="135" rx="12" fill="url(#hg1)" opacity=".78"/>
 <rect x="196" y="45" width="44" height="185" rx="12" fill="url(#hg1)"/>
 <path d="M218 45 C218 15 238 -5 268 -5 C268 25 248 45 218 45z" fill="url(#hg2)"/>
 <path d="M218 45 C218 22 202 8 180 8 C180 30 196 45 218 45z" fill="#2fbf8f"/>
 <text x="32" y="255" text-anchor="middle" font-family="Inter" font-size="13" font-weight="700" fill="var(--muted)">8</text>
 <text x="94" y="255" text-anchor="middle" font-family="Inter" font-size="13" font-weight="700" fill="var(--muted)">10</text>
 <text x="156" y="255" text-anchor="middle" font-family="Inter" font-size="13" font-weight="700" fill="var(--muted)">12</text>
 <text x="218" y="255" text-anchor="middle" font-family="Inter" font-size="13" font-weight="700" fill="var(--muted)">14+</text>
</g>
<g font-family="Inter" font-weight="700" font-size="15">
 <g transform="translate(18 70)"><rect width="150" height="50" rx="16" fill="var(--surface)" stroke="var(--line)"/><circle cx="26" cy="25" r="11" fill="#ffece8"/><circle cx="26" cy="25" r="5" fill="#ff6a55"/><text x="46" y="30" fill="var(--ink)">Periods</text></g>
 <g transform="translate(350 40)"><rect width="150" height="50" rx="16" fill="var(--surface)" stroke="var(--line)"/><circle cx="26" cy="25" r="11" fill="#fff4d6"/><path d="M20 25h12M26 19v12" stroke="#e0a000" stroke-width="3" stroke-linecap="round"/><text x="46" y="30" fill="var(--ink)">Feelings</text></g>
 <g transform="translate(372 280)"><rect width="134" height="50" rx="16" fill="var(--surface)" stroke="var(--line)"/><circle cx="26" cy="25" r="11" fill="#e2f6f4"/><path d="M21 25q5-8 10 0" stroke="#0f8a8a" stroke-width="3" fill="none" stroke-linecap="round"/><text x="46" y="30" fill="var(--ink)">Voice</text></g>
 <g transform="translate(6 300)"><rect width="150" height="50" rx="16" fill="var(--surface)" stroke="var(--line)"/><circle cx="26" cy="25" r="11" fill="#efeaff"/><path d="M26 31v-10M22 25l4-4 4 4" stroke="#5b3fd6" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="46" y="30" fill="var(--ink)">Growth</text></g>
</g>
</svg>'''


MYTHS = [
    ("Everyone starts puberty at the same age.", "Normal start ranges span about five years: roughly 8–13 for girls and 9–14 for boys."),
    ("You can't exercise on your period.", "Movement is fine and can even ease cramps. Choose whatever product feels comfortable."),
    ("Acne means you're not clean.", "Acne is driven by hormones and oil glands. Gentle cleansing helps; scrubbing harder doesn't."),
    ("Boys don't have emotional changes.", "Hormones affect everyone's mood. Boys benefit from talking about feelings just as much."),
    ("Talking about puberty early makes kids grow up faster.", "Accurate, age-appropriate information helps kids feel prepared, safer and less anxious."),
    ("A cracking voice means something's wrong.", "It's the voice box growing. The cracks fade as the new, deeper voice settles."),
]


def home(arts):
    r = ""
    feat = "".join(card(a, r) for a in arts[:6])
    myths = "".join(f'''<button class="flip" type="button" aria-label="Flip card"><div class="in"><div class="f"><small>Myth</small><strong style="font-size:1.1rem">{esc(m)}</strong><span class="muted" style="font-size:13px;margin-top:10px">Tap to flip →</span></div><div class="b"><small style="color:var(--teal)">Fact</small>{esc(f)}</div></div></button>''' for m, f in MYTHS)
    vids = "".join(vcard(v) for v in VIDEOS[:3])
    body = f'''<section class="hero"><div class="container hero-grid">
<div>
  <span class="eyebrow">{ICONS["sprout"].replace("<svg", '<svg style="width:14px;height:14px"')} Puberty, explained — without the awkward</span>
  <h1 class="mt-2">Growing up is weird.<br><span class="hl">Understanding it shouldn't be.</span></h1>
  <p class="lead">Clear, kind, medically grounded answers about body changes, periods, voice changes, skin, feelings and staying safe — for teens, the parents who love them and the educators who teach them.</p>
  <div class="hero-actions"><a class="btn btn-primary" href="learn/">Start learning {ICONS["arrow"]}</a><a class="btn btn-ghost" href="tools/stage-explorer.html">What's next for my body?</a></div>
  <div class="chips"><a class="chip" href="learn/first-period-guide.html">First period</a><a class="chip" href="learn/puberty-changes-boys.html">Boys' puberty</a><a class="chip" href="learn/acne-and-skin-care.html">Acne</a><a class="chip" href="learn/emotions-and-mood-swings.html">Mood swings</a><a class="chip" href="learn/talking-to-your-child-about-puberty.html">How to talk about it</a></div>
</div>
<div class="hero-art">{HERO_ART}</div>
</div></section>

<section class="section-tight"><div class="container">
<div class="section-head"><span class="eyebrow">Choose your path</span><h2 class="mt-2">Built for everyone in the conversation</h2></div>
<div class="paths">
  <a class="path" href="learn/"><div class="ico bg-brand">{ICONS["sprout"]}</div><h3>I'm a teen</h3><p>What's happening, what's normal, and how to handle it — no judgment, no awkward lectures.</p><span class="go">Explore the guides →</span></a>
  <a class="path" href="parents.html"><div class="ico bg-coral">{ICONS["users"]}</div><h3>I'm a parent</h3><p>What to say, when to say it, and printable scripts that make "the talk" a series of easy chats.</p><span class="go">Parent hub + free kit →</span></a>
  <a class="path" href="schools.html"><div class="ico bg-teal">{ICONS["school"]}</div><h3>I'm an educator</h3><p>Lesson structure, handouts and classroom-ready resources — plus free support for your school.</p><span class="go">Resources for schools →</span></a>
</div></div></section>

<section class="section-tight"><div class="container">
<div class="facts">
  <div class="fact"><b>8–13</b><span>Typical age range for puberty to begin in girls</span></div>
  <div class="fact"><b>9–14</b><span>Typical age range for puberty to begin in boys</span></div>
  <div class="fact"><b>~12</b><span>Average age of a first period in many countries</span></div>
  <div class="fact"><b>8–10 h</b><span>Recommended nightly sleep for teens aged 13–18</span></div>
</div>
<p class="form-note">Ranges summarize public guidance from pediatric and public-health organizations; individual timing varies.</p>
</div></section>

<section><div class="container">
<div class="section-head"><span class="eyebrow">Most-read guides</span><h2 class="mt-2">Start with the essentials</h2><p>In-depth, plain-language guides — each with key takeaways, a "when to see a doctor" checklist and sources.</p></div>
<div class="grid g3">{feat}</div>
<div class="center mt-3"><a class="btn btn-ghost" href="learn/">See all {len(arts)} guides {ICONS["arrow"]}</a></div>
</div></section>

<section class="bg-soft"><div class="container">
<div class="lead-box">
  <div class="pitch">
    <span class="eyebrow">Free for parents &amp; educators</span>
    <h2 class="mt-2" style="font-size:2rem">The Puberty Talk Starter Kit</h2>
    <p style="color:#e6e1ff">Turn one dreaded "big talk" into lots of small, easy ones. Printable and ready tonight.</p>
    <ul class="ticks"><li>Age-by-age scripts for 7 to 14+</li><li>"What do I say if…" quick answers</li><li>First-period kit list + boys' puberty checklist</li><li>40 printable question-jar cards</li></ul>
    <div class="kit-preview"><div><b>4</b>age-banded script sets</div><div><b>40</b>question cards</div><div><b>2</b>printable checklists</div></div>
  </div>
  <div class="form-side"><h3>Where should we send it?</h3><p class="muted">Instant access after you submit.</p>{kit_form(r, "home")}</div>
</div></div></section>

<section><div class="container">
<div class="section-head"><span class="eyebrow">Interactive</span><h2 class="mt-2">Tools that make it click</h2></div>
<div class="grid g3">
  <a class="card path" href="tools/stage-explorer.html"><div class="ico bg-brand">{ICONS["sprout"]}</div><h3>Body Changes Explorer</h3><p>Slide to an age, see what's typical.</p><span class="go">Try it →</span></a>
  <a class="card path" href="tools/period-calculator.html"><div class="ico bg-coral">{ICONS["calendar"]}</div><h3>Period Predictor</h3><p>Private, on-device estimates.</p><span class="go">Try it →</span></a>
  <a class="card path" href="tools/puberty-quiz.html"><div class="ico bg-sun">{ICONS["quiz"]}</div><h3>Myth or Fact Quiz</h3><p>12 questions, 2 minutes.</p><span class="go">Take the quiz →</span></a>
</div></div></section>

<section class="bg-soft"><div class="container">
<div class="section-head"><span class="eyebrow">Myth busting</span><h2 class="mt-2">Tap a myth to flip it</h2></div>
<div class="flip-grid">{myths}</div>
</div></section>

<section><div class="container">
<div class="section-head"><span class="eyebrow">Watch &amp; learn</span><h2 class="mt-2">Short videos worth watching together</h2></div>
<div class="grid g3">{vids}</div>
<div class="center mt-3"><a class="btn btn-ghost" href="videos.html">Open the video library {ICONS["arrow"]}</a></div>
</div></section>

<section class="bg-ink"><div class="container">
<div class="grid g2" style="align-items:center">
  <div><span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff">For schools &amp; organizations</span><h2 class="mt-2">Bring better puberty education to your students</h2><p class="muted">Free classroom resources, parent-night materials, staff guides and sponsored period-product kits. Tell us what your school needs and we'll put together a plan.</p>
  <ul class="ticks"><li>Curriculum-aligned lesson structure</li><li>Anonymous question-box templates</li><li>Bilingual parent letters (coming soon)</li></ul>
  <a class="btn btn-sun" href="schools.html">Request school resources {ICONS["arrow"]}</a></div>
  <div class="grid g2">
    <a class="card" href="ask.html" style="color:var(--ink)"><div class="ico bg-mint" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["chat"]}</div><h3 class="mt-2">Ask anonymously</h3><p class="muted">No name, no email.</p></a>
    <a class="card" href="support.html" style="color:var(--ink)"><div class="ico bg-coral" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["heart"]}</div><h3 class="mt-2">Support us</h3><p class="muted">Keep it free for every family.</p></a>
    <a class="card" href="contests.html" style="color:var(--ink)"><div class="ico bg-sun" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["trophy"]}</div><h3 class="mt-2">Contests</h3><p class="muted">Classroom challenges &amp; prizes.</p></a>
    <a class="card" href="careers.html" style="color:var(--ink)"><div class="ico bg-teal" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["brief"]}</div><h3 class="mt-2">Join us</h3><p class="muted">Writers, reviewers, creators.</p></a>
  </div>
</div></div></section>

<section class="section-tight"><div class="container">{help_strip(r)}</div></section>'''
    js = '<script>document.querySelectorAll(".flip").forEach(function(f){f.addEventListener("click",function(){f.classList.toggle("on")})});</script>'
    return page("index.html", "Puberty101.com — Puberty Explained for Teens, Parents & Educators",
                "Clear, kind, medically grounded puberty education: body changes, first periods, voice changes, acne, emotions and body safety. Free tools, guides and videos.",
                body, inline_js=js)


def videos():
    cats = ["Body Changes", "Girls", "Boys", "Periods", "Hygiene", "Feelings"]
    chips = '<button class="chip active" data-filter="all">All</button>' + "".join(f'<button class="chip" data-filter="{c}">{c}</button>' for c in cats)
    grid = "".join(vcard(v) for v in VIDEOS)
    schema = [{"@context": "https://schema.org", "@type": "VideoObject", "name": t, "description": f"{t} — an educational puberty video ({c}).",
               "thumbnailUrl": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", "embedUrl": f"https://www.youtube-nocookie.com/embed/{vid}",
               "uploadDate": "2020-01-01"} for vid, t, ch, c in VIDEOS]
    body = hero("Puberty video library", "Hand-picked short explainers on body changes, periods, boys' puberty, hygiene and feelings. Videos load only when you press play, and play in privacy-enhanced mode.", "",
                [("Videos", None)], f"{len(VIDEOS)} videos") + f'''
<section class="section-tight"><div class="container">
<div class="chips" data-filter-group="#vg">{chips}</div>
<div class="grid g3 mt-3" id="vg">{grid}</div>
<div class="card mt-4"><h3>More great channels</h3><p class="muted">For more animated, age-appropriate explainers, see <a href="https://www.youtube.com/@amazeorg" target="_blank" rel="noopener">AMAZE on YouTube</a> and the <a href="https://kidshealth.org" target="_blank" rel="noopener">Nemours KidsHealth</a> video library. Parents: preview videos first and watch together where possible.</p>
<p class="form-note">Videos are embedded from YouTube and remain the property of their creators. Puberty101.com is not affiliated with these channels. Spot a broken video? <a href="contact.html">Let us know</a>.</p></div>
<div class="card mt-3" style="background:var(--tint-sun)"><h3>Make videos with us</h3><p>We're commissioning original animated explainers. Creators, animators and medical reviewers — <a href="careers.html">see open roles</a>. Brands — <a href="advertise.html">sponsor a series</a>.</p></div>
</div></section>'''
    return page("videos.html", "Puberty Videos for Teens & Families", "Watch hand-picked puberty videos on body changes, first periods, boys' puberty, hygiene, acne and emotions — privacy-friendly embeds.", body, active="Videos", schema=schema)


ASK_FAQ = [
    ("Is it normal for one breast to grow faster than the other?", "Yes. It's very common for one side to start first or grow faster. Most even out over time, and small differences are normal into adulthood."),
    ("I'm 13 and haven't started yet. Is something wrong?", "Probably not — timing varies a lot. Doctors usually suggest a check-up if girls have no breast development by 13 or boys have no testicular growth by 14, just to make sure."),
    ("How do I know my first period is coming?", "Common clues: breast development for about 2–3 years, pubic hair, and white or clear discharge in your underwear for a few months. Pack a kit in your bag so you're ready."),
    ("Why does my voice keep cracking?", "Your voice box is growing and your vocal cords are getting longer and thicker. The cracks are temporary and usually settle within months."),
    ("I sweat a lot and smell even after showering. What can I do?", "Shower daily, wear clean clothes, and try an antiperspirant (it reduces sweat) rather than only a deodorant. Breathable fabrics help. If sweating is extreme, a doctor can help."),
    ("Is it normal to feel angry or sad for no reason?", "Big, fast-changing feelings are common in puberty. Sleep, movement and talking help. If sadness lasts for weeks or you feel unsafe, tell a trusted adult or call a helpline."),
    ("Can I use a tampon for my first period?", "You can, if you feel comfortable and follow the instructions, but many people start with pads. Choose the lowest absorbency you need and change it every 4–8 hours."),
    ("Do boys go through puberty later than girls?", "On average, yes — by about one to two years. But individual timing varies a lot for everyone."),
]


def ask():
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in ASK_FAQ)
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ASK_FAQ]}
    body = hero("Ask anything — anonymously", "Some questions are hard to say out loud. Ask here: no name, no email, no account. We answer the most common questions in plain language on the site.", "",
                [("Ask", None)], "100% anonymous") + f'''
<section class="section-tight"><div class="container"><div class="grid g2" style="align-items:start">
<div class="tool-wrap">
<form data-form="Anonymous question" data-success="Got it — thank you! We read every question. Popular ones get answered on the site.">
  {honeypot()}<input type="hidden" name="Form" value="Anonymous question">
  <div class="field"><span class="label">Who's asking?</span><div class="radio-cards">
    <label><input type="radio" name="Asker" value="Teen 13-15" required>Teen<span>13–15</span></label>
    <label><input type="radio" name="Asker" value="Teen 16-17">Teen<span>16–17</span></label>
    <label><input type="radio" name="Asker" value="Parent">Parent<span>or caregiver</span></label>
    <label><input type="radio" name="Asker" value="Educator">Educator<span>or school staff</span></label></div></div>
  <div class="field"><label for="aq-t">Topic</label><select id="aq-t" name="Topic"><option>Body changes</option><option>Periods</option><option>Boys' puberty</option><option>Skin, sweat &amp; hygiene</option><option>Feelings &amp; mood</option><option>Body image</option><option>Something else</option></select></div>
  <div class="field"><label for="aq-q">Your question</label><textarea id="aq-q" name="Question" required maxlength="1200" placeholder="Type your question… please don't include names, addresses, school names or contact details."></textarea></div>
  <label class="check"><input type="checkbox" required> I understand answers are general education, not medical advice, and I haven't included any personal or contact details.</label>
  <button class="btn btn-primary btn-block" type="submit">Send my question anonymously</button>{status()}
  <p class="form-note">Under 13? Please ask a parent, caregiver or school nurse to help you. We can't reply privately — if you need help now, use a helpline below.</p>
</form></div>
<div><h2 style="font-size:1.6rem">Questions people ask most</h2><div class="faq">{faq}</div></div>
</div>
<div class="mt-4">{help_strip("")}</div>
</div></section>'''
    return page("ask.html", "Ask a Puberty Question Anonymously", "Ask any puberty question anonymously — no name or email. Read plain-language answers to the questions teens and parents ask most.", body, active="Ask", schema=schema)


def parents(arts):
    pa = [a for a in arts if a["audience"] in ("Parents", "Teens & Parents") or a["category"] == "For Parents"][:6]
    cards = "".join(card(a, "") for a in pa)
    body = hero("The parent's guide to puberty", "You don't need perfect words — you need to start early, keep it short and keep the door open. Here's everything to help you do exactly that.", "",
                [("Parents", None)], "For parents & caregivers") + f'''
<section class="section-tight"><div class="container">
<div class="lead-box">
  <div class="pitch"><span class="eyebrow">Free download</span><h2 class="mt-2" style="font-size:2rem">The Puberty Talk Starter Kit</h2>
    <p style="color:#e6e1ff">Built from what the best puberty-education programs get right — and the gaps they miss, like boys' puberty and age-banded scripts.</p>
    <ul class="ticks"><li>Scripts for ages 7–9, 10–11, 12–13 and 14+</li><li>"What do I say if…" answers to 12 tricky moments</li><li>First-period kit list + boys' puberty checklist</li><li>40 question-jar cards and a family agreement</li></ul></div>
  <div class="form-side"><h3>Get instant access</h3>{kit_form("", "par")}</div>
</div></div></section>
<section class="section-tight"><div class="container">
<div class="section-head"><h2>The 5 rules that make puberty talks easier</h2></div>
<div class="grid g3">
<div class="card"><h3>1. Start before it starts</h3><p class="muted">Begin simple body talk around 7–8, before changes appear. Information before experience prevents fear.</p></div>
<div class="card"><h3>2. Many small talks</h3><p class="muted">Two minutes in the car beats one hour at the kitchen table. Repetition builds comfort.</p></div>
<div class="card"><h3>3. Use real words</h3><p class="muted">Correct anatomical names are a health and safety skill — not an embarrassment.</p></div>
<div class="card"><h3>4. Answer, then stop</h3><p class="muted">Answer what was asked, check understanding, and let your child steer the next question.</p></div>
<div class="card"><h3>5. "I don't know — let's find out"</h3><p class="muted">Looking things up together models curiosity and keeps you the trusted source.</p></div>
<div class="card"><h3>6. Keep the door open</h3><p class="muted">End every talk with "you can always ask me." Then mean it — calmly, every time.</p></div>
</div></div></section>
<section class="bg-soft"><div class="container"><div class="section-head"><h2>Guides for parents</h2></div><div class="grid g3">{cards}</div>
<div class="grid g3 mt-3"><a class="card" href="tools/conversation-starters.html"><h3>Conversation starters →</h3><p class="muted">Age-matched openers, one tap away.</p></a><a class="card" href="tools/period-kit-builder.html"><h3>Period kit builder →</h3><p class="muted">Pack it together, print it out.</p></a><a class="card" href="learn/body-safety-and-privacy.html"><h3>Body safety guide →</h3><p class="muted">Boundaries, privacy and trusted adults.</p></a></div>
</div></section>'''
    return page("parents.html", "Parent's Guide to Puberty + Free Talk Starter Kit", "How to talk to your child about puberty: age-by-age advice, conversation starters, body-safety tips and a free printable Puberty Talk Starter Kit.", body, active="Parents")


def schools():
    body = hero("Puberty education for schools &amp; organizations", "Free classroom resources, parent-night support, staff guides and sponsored period-product kits. Tell us about your students and we'll build a plan that fits.", "",
                [("Schools", None)], "For educators, nurses &amp; youth orgs") + f'''
<section class="section-tight"><div class="container"><div class="grid g4">
<div class="card"><div class="ico bg-brand" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["book"]}</div><h3 class="mt-2">Lesson resources</h3><p class="muted">Ready-to-teach structure, ground rules and handouts for grades 4–9.</p></div>
<div class="card"><div class="ico bg-coral" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["gift"]}</div><h3 class="mt-2">Period-kit program</h3><p class="muted">Sponsor-funded starter kits for students who need them.</p></div>
<div class="card"><div class="ico bg-teal" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["users"]}</div><h3 class="mt-2">Parent nights</h3><p class="muted">Slides, letters and FAQs for a calm, well-attended parent session.</p></div>
<div class="card"><div class="ico bg-sun" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS["school"]}</div><h3 class="mt-2">Workshops &amp; training</h3><p class="muted">Virtual or in-person sessions for students and staff.</p></div>
</div></div></section>

<section class="bg-soft" id="request"><div class="container"><div class="lead-box">
<div class="pitch"><span class="eyebrow">Takes 90 seconds</span><h2 class="mt-2" style="font-size:2rem">Request resources for your school</h2>
<p style="color:#e6e1ff">Free resources are free — always. Workshops, custom materials and kit programs are scoped to your budget, and many can be sponsor-funded.</p>
<ul class="ticks"><li>Personal reply from our education team</li><li>Inclusive, medically grounded content</li><li>Clear parent-communication templates</li><li>No obligation, no sales pressure</li></ul></div>
<div class="form-side">
<form data-form="School / organization request" data-steps data-success="Thank you! Your request is in. We'll reply within 2 business days with next steps.">
  {honeypot()}<input type="hidden" name="Form" value="School resource request">
  <div class="steps-bar"><i></i><i></i><i></i><i></i></div>
  <div class="step"><h3>1. Who are you?</h3><div class="radio-cards">
    <label><input type="radio" name="Role" value="Teacher" required>Teacher</label><label><input type="radio" name="Role" value="School nurse">School nurse</label>
    <label><input type="radio" name="Role" value="Counselor">Counselor</label><label><input type="radio" name="Role" value="Administrator">Administrator</label>
    <label><input type="radio" name="Role" value="Youth / community org">Youth org</label><label><input type="radio" name="Role" value="Parent council">Parent council</label></div>
    <div class="step-nav mt-2"><span></span><button type="button" class="btn btn-primary" data-next-step>Next →</button></div></div>
  <div class="step"><h3>2. Your school or organization</h3>
    <div class="field"><label for="s-org">School / organization name</label><input id="s-org" name="Organization" required></div>
    <div class="row"><div class="field"><label for="s-country">Country</label><input id="s-country" name="Country" required></div><div class="field"><label for="s-region">State / province</label><input id="s-region" name="Region"></div></div>
    <div class="row"><div class="field"><label for="s-grades">Grades</label><select id="s-grades" name="Grades" required><option value="">Choose</option><option>Grades 3–5</option><option>Grades 5–6</option><option>Grades 6–8</option><option>Grades 9–12</option><option>Mixed / multiple</option></select></div>
    <div class="field"><label for="s-size">Students reached</label><select id="s-size" name="Students"><option>Under 50</option><option>50–200</option><option>200–500</option><option>500–2,000</option><option>2,000+ (district)</option></select></div></div>
    <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="button" class="btn btn-primary" data-next-step>Next →</button></div></div>
  <div class="step"><h3>3. What do you need?</h3><div class="radio-cards" style="grid-template-columns:1fr 1fr">
    <label><input type="checkbox" name="Needs" value="Free lesson resources">Free lesson resources</label><label><input type="checkbox" name="Needs" value="Printable handouts">Printable handouts</label>
    <label><input type="checkbox" name="Needs" value="Parent night kit">Parent night kit</label><label><input type="checkbox" name="Needs" value="Student workshop">Student workshop</label>
    <label><input type="checkbox" name="Needs" value="Staff training">Staff training</label><label><input type="checkbox" name="Needs" value="Period product kits">Period-product kits</label></div>
    <div class="row mt-2"><div class="field"><label for="s-when">Timeline</label><select id="s-when" name="Timeline"><option>This month</option><option>This term</option><option>Next school year</option><option>Just exploring</option></select></div>
    <div class="field"><label for="s-bud">Budget</label><select id="s-bud" name="Budget"><option>Free resources only</option><option>Under $500</option><option>$500–$2,000</option><option>$2,000+</option><option>Seeking sponsorship</option></select></div></div>
    <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="button" class="btn btn-primary" data-next-step>Next →</button></div></div>
  <div class="step"><h3>4. Where should we reply?</h3>
    <div class="row"><div class="field"><label for="s-name">Full name</label><input id="s-name" name="name" required autocomplete="name"></div><div class="field"><label for="s-email">Work email</label><input id="s-email" type="email" name="email" required autocomplete="email"></div></div>
    <div class="field"><label for="s-phone">Phone (optional)</label><input id="s-phone" type="tel" name="Phone" autocomplete="tel"></div>
    <div class="field"><label for="s-msg">Anything else? (optional)</label><textarea id="s-msg" name="Notes" style="min-height:80px"></textarea></div>
    <label class="check"><input type="checkbox" required name="Consent" value="Yes"> I'm 18+ and agree to be contacted about this request.</label>
    <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev-step>← Back</button><button type="submit" class="btn btn-coral">Send request</button></div>{status()}</div>
</form></div></div></div></section>

<section><div class="container"><div class="grid g2">
<div><h2>What great puberty education looks like</h2><p class="muted">Our classroom approach follows widely accepted best practice for health education.</p>
<ul class="ticks dark"><li>Clear ground rules and an anonymous question box</li><li>Accurate anatomical language</li><li>Inclusive of every student, including neurodivergent learners</li><li>Coverage of boys' puberty, not just periods</li><li>Proactive, transparent communication with families</li></ul>
<a class="btn btn-ghost mt-2" href="learn/teaching-puberty-in-the-classroom.html">Read the educator guide {ICONS["arrow"]}</a></div>
<div class="card" style="background:var(--tint-sun)"><h3>Brands &amp; foundations: fund a classroom</h3><p>Sponsor period-product kits, workshops or a whole district program. Your support is credited (tastefully) on materials.</p><a class="btn btn-primary" href="advertise.html">Explore sponsorship</a></div>
</div></div></section>'''
    return page("schools.html", "Puberty Education Resources for Schools", "Free puberty education resources for schools: lesson structure, handouts, parent-night kits, workshops and sponsored period-product kits.", body, active="Schools", no_modal=True)


def kit():
    def sec(title, inner):
        return f'<div class="card mt-3"><h2 style="font-size:1.5rem">{title}</h2>{inner}</div>'
    scripts = {
        "Ages 7–9: lay the groundwork": ["Name body parts correctly: \"Your body belongs to you, and these are the real names for its parts.\"",
                                         "\"In a few years your body will start to change, like everyone's does. It's called puberty. You can ask me anything about it.\"",
                                         "\"Surprises are fun and get shared soon. Secrets about bodies or touching are never OK to keep — always tell me.\""],
        "Ages 10–11: before changes begin": ["\"Some kids your age are starting to grow and change. Have you noticed anything, or heard kids talking?\"",
                                             "\"Let's make a just-in-case kit for your bag — then you never have to worry.\"",
                                             "\"Feelings can get bigger in puberty. That's hormones, not you being 'too much.'\""],
        "Ages 12–13: while it's happening": ["\"No lecture. Is there anything you've been wondering about or seen online that seemed weird?\"",
                                             "\"How's your skin/sleep/sweat situation? Want to pick some products together?\"",
                                             "\"If anyone ever makes you uncomfortable — online or in person — I will never be angry at you for telling me.\""],
        "Ages 14+: coaching independence": ["\"Would you like some time alone with the doctor at your next check-up?\"",
                                            "\"Who are three adults you trust if you can't reach me?\"",
                                            "\"Is there anything you wish I'd explained better?\""],
    }
    s_html = "".join(f'<h3 class="mt-2">{t}</h3><ul>' + "".join(f"<li>{esc(x)}</li>" for x in xs) + "</ul>" for t, xs in scripts.items())
    whatif = [("Your child asks something you can't answer", "\"Great question — I'm not sure. Let's look it up together.\""),
              ("They seem embarrassed", "\"Lots of people feel awkward about this. We can talk while we walk or drive.\""),
              ("They heard something false at school", "\"I'm glad you asked me. Here's what's actually true…\""),
              ("They start their period at school", "\"You did exactly the right thing. Let's restock your kit together.\""),
              ("Their friend is developing faster", "\"Bodies follow their own schedules. Yours is right on time for you.\""),
              ("They're worried they're 'not normal'", "\"Tell me what you've noticed. If we have questions, we'll ask the doctor together.\"")]
    w_html = "<ul>" + "".join(f"<li><strong>{esc(a)}:</strong> {esc(b)}</li>" for a, b in whatif) + "</ul>"
    cards = ["What is puberty?", "Why do we get pimples?", "What does a period feel like?", "Why does my voice crack?",
             "When will I get taller?", "Why do I sweat more now?", "Is it normal to feel moody?", "What's discharge?",
             "What are hormones?", "Why do I need deodorant?", "Can I swim on my period?", "What are growth spurts?",
             "Why are my feet growing so fast?", "What is a trusted adult?", "What's the difference between a secret and a surprise?",
             "Why is my skin oilier?", "What is body hair for?", "Why do some boys get sore chests?", "How do I use a pad?",
             "How much sleep do I need?", "What should be in my period kit?", "Who can I ask if I'm embarrassed?",
             "What's a growth plate?", "Why do I feel clumsy?", "What happens at a check-up?", "How do I handle cramps?",
             "Do boys and girls change at the same time?", "What is the Adam's apple?", "How do I wash my face properly?",
             "What's a healthy breakfast for school?", "How can I feel good about my body?", "What do I do if someone makes me uncomfortable?",
             "What's the difference between deodorant and antiperspirant?", "How long does puberty last?", "Will my voice stay squeaky?",
             "What's a normal cycle length?", "Why do I want more privacy?", "How do I talk about feelings?", "What is menarche?", "What's one thing you wish you knew?"]
    c_html = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px">' + "".join(f'<div style="border:1.5px dashed var(--line);border-radius:12px;padding:12px;font-weight:600;font-size:14px">{esc(c)}</div>' for c in cards) + "</div>"
    body = hero("The Puberty Talk Starter Kit", "Your free kit is ready. Print it, save it as a PDF, or come back to this page anytime.", "",
                [("Starter Kit", None)], "Thanks for downloading",
                f'<div class="hero-actions"><button class="btn btn-primary" data-print>{ICONS["print"]} Print / save as PDF</button><a class="btn btn-ghost" href="tools/conversation-starters.html">Open conversation starters</a></div>') + f'''
<section class="section-tight"><div class="container narrow">
{sec("1. Age-by-age talk scripts", s_html)}
{sec("2. What do I say if…", w_html)}
{sec("3. First-period kit list", "<ul><li>2–3 pads + 1–2 liners</li><li>Spare underwear and dark leggings</li><li>Small zip bag for used items</li><li>Unscented wipes</li><li>A note with a trusted adult's number</li></ul><p class='muted'>Interactive version: <a href='tools/period-kit-builder.html'>Period Kit Builder</a>.</p>")}
{sec("4. Boys' puberty checklist", "<ul><li>Talk about voice changes, growth spurts and sweat before they happen</li><li>Antiperspirant, face wash and a fresh-clothes routine</li><li>Explain that temporary breast swelling and unexpected erections are common and normal</li><li>Normalize talking about feelings — and name trusted adults</li><li>Check-up if no signs of puberty by 14</li></ul>")}
{sec("5. 40 question-jar cards", "<p class='muted'>Cut out, fold, and pull one at dinner or in the car. Answer together.</p>" + c_html)}
{sec("6. Family agreement", "<ul><li>Any question is OK — nobody gets laughed at.</li><li>We use the real names for body parts.</li><li>No secrets about bodies or safety.</li><li>If you can't ask out loud, write it down.</li><li>We look things up together from trusted sources.</li></ul>")}
<p class="muted mt-3">This kit is general education, not medical advice. Share it freely for personal and classroom use with attribution to Puberty101.com.</p>
</div></section>'''
    return page("kit.html", "Your Puberty Talk Starter Kit", "The free Puberty Talk Starter Kit: age-by-age scripts, what-to-say answers, kit lists and 40 question-jar cards.", body, noindex=True, no_modal=True)


def support():
    has_links = any(DONATE_LINKS.values())
    pay_btns = "".join(f'<a class="btn btn-ghost" href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in DONATE_LINKS.items() if u)
    pay = f'<p class="label mt-2">Pay securely with</p><div class="hero-actions" style="margin:0">{pay_btns}</div><p class="form-note">Or use the pledge form to give by invoice or bank transfer.</p>' if has_links else ""
    tiers = [("Friend", "$10", "a month", ["Keeps one guide reviewed and up to date", "Supporter newsletter", "Our sincere thanks"]),
             ("Champion", "$25", "a month", ["Funds a new interactive tool each quarter", "Name on the supporters page (optional)", "Early access to new resources"]),
             ("Classroom Hero", "$100", "one-time", ["Helps fund period-product kits for a classroom", "Thank-you certificate", "Impact update from the program"]),
             ("Founding Partner", "$1,000+", "one-time or annual", ["Fund a video, tool or school program", "Recognition on sponsored materials", "Quarterly impact call"])]
    t_html = "".join(f'''<div class="card tier{' featured' if i == 1 else ''}"><h3>{n}</h3><div class="price">{p}</div><p class="muted" style="margin-top:-4px">{per}</p><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul><a class="btn {'btn-primary' if i == 1 else 'btn-ghost'} btn-block" href="#give" data-tier="{n}">Choose {n}</a></div>''' for i, (n, p, per, xs) in enumerate(tiers))
    alloc = [("Content &amp; medical review", 35, "var(--brand)"), ("Free school kits &amp; resources", 25, "var(--coral)"),
             ("Original videos &amp; tools", 20, "var(--teal)"), ("Contests, prizes &amp; community", 10, "var(--sun)"), ("Operations &amp; outreach", 10, "var(--mint)")]
    a_html = "".join(f'<div><div style="display:flex;justify-content:space-between;font-weight:600;font-size:14.5px"><span>{n}</span><span>{v}%</span></div><div class="bar"><i style="width:{v}%;background:{c}"></i></div></div>' for n, v, c in alloc)
    body = hero("Keep puberty education free for every family", "Your support funds new guides, medical review, free school resources, original videos, contests and the day-to-day work of keeping this site running.", "",
                [("Support", None)], f'{ICONS["heart"].replace("<svg", "<svg style=\"width:14px;height:14px\"")} Support Puberty101') + f'''
<section class="section-tight"><div class="container"><div class="grid g4">{t_html}</div></div></section>
<section class="bg-soft" id="give"><div class="container"><div class="grid g2" style="align-items:start">
<div class="tool-wrap">
<h2 style="font-size:1.6rem">Make your contribution</h2>
<form data-form="Donation pledge" data-success="Thank you! We'll email you a secure payment link and receipt details within 1 business day.">
  {honeypot()}<input type="hidden" name="Form" value="Donation pledge">
  <div class="seg" style="margin-bottom:14px"><label style="padding:8px 14px;cursor:pointer;font-weight:700;font-size:14px"><input type="radio" name="Frequency" value="Monthly" checked> Monthly</label><label style="padding:8px 14px;cursor:pointer;font-weight:700;font-size:14px"><input type="radio" name="Frequency" value="One-time"> One-time</label></div>
  <div class="amounts" data-amounts="#amt"><button data-amt="10">$10</button><button data-amt="25" class="on">$25</button><button data-amt="50">$50</button><button data-amt="100">$100</button></div>
  <div class="row mt-2"><div class="field"><label for="amt">Amount (USD)</label><input id="amt" type="number" name="Amount" min="1" value="25" required></div>
  <div class="field"><label for="d-use">Direct my gift to</label><select id="d-use" name="Direct to"><option>Where it's needed most</option><option>Free school kits</option><option>New videos &amp; tools</option><option>Contests &amp; prizes</option><option>Hiring writers &amp; reviewers</option><option>Marketing &amp; outreach</option></select></div></div>
  <div class="row"><div class="field"><label for="d-name">Name</label><input id="d-name" name="name" required></div><div class="field"><label for="d-email">Email</label><input id="d-email" type="email" name="email" required></div></div>
  <label class="check"><input type="checkbox" name="Public recognition" value="Yes"> List my name on the supporters page</label>
  <label class="check"><input type="checkbox" required> I'm 18 or older.</label>
  <button class="btn btn-coral btn-block" type="submit">{ICONS["heart"]} Pledge my support</button>{status()}
  {pay}
  <p class="form-note">Puberty101.com is an independent educational publisher, not a registered charity, so contributions are not tax-deductible. We'll confirm every pledge personally before any payment is taken.</p>
</form></div>
<div><h2 style="font-size:1.6rem">Where the money goes</h2><p class="muted">Planned allocation of supporter contributions.</p><div class="alloc mt-2">{a_html}</div>
<div class="card mt-3"><h3>Other ways to help</h3><ul class="ticks dark" style="font-size:15px">
<li><strong>Donate products:</strong> pads, liners and hygiene items for school kits.</li>
<li><strong>Corporate sponsorship:</strong> fund a series, tool or district program — <a href="advertise.html">see packages</a>.</li>
<li><strong>Sponsor a prize:</strong> back a classroom contest — <a href="contests.html">see contests</a>.</li>
<li><strong>Volunteer your skills:</strong> writing, illustration, video, translation — <a href="careers.html">join us</a>.</li>
<li><strong>Share:</strong> send a guide to one parent or teacher today.</li></ul></div></div>
</div></div></section>'''
    js = '<script>document.querySelectorAll("[data-tier]").forEach(function(a){a.addEventListener("click",function(){var m={"Friend":10,"Champion":25,"Classroom Hero":100,"Founding Partner":1000},v=m[a.getAttribute("data-tier")];var i=document.getElementById("amt");if(i&&v)i.value=v;document.querySelectorAll("[data-amt]").forEach(function(b){b.classList.toggle("on",+b.getAttribute("data-amt")===v)});var f=document.querySelector("[name=Frequency][value="+(v>=100?"One-time":"Monthly")+"]");if(f)f.checked=true})});</script>'
    return page("support.html", "Support Puberty101 — Donate & Sponsor", "Support free puberty education: donate monthly or one-time, sponsor school period kits, fund videos and tools, or donate products.", body, inline_js=js, no_modal=True)


def contests():
    cs = [("Healthy Me Poster Challenge", "Classrooms (grades 4–8)", "Students design a poster that teaches one puberty or hygiene fact. Teachers submit the class's best three.",
           "Classroom resource grant + featured gallery placement", "trophy", "brand"),
          ("Explain It in 60 Seconds", "Creators 16+ (under 18 via parent/guardian)", "Make a 60-second, family-friendly explainer on a puberty topic — animation, whiteboard or skit. No faces required.",
           "Cash prize + paid commission for a full video", "play", "coral"),
          ("Question of the Month", "Everyone (anonymous)", "Submit a question through Ask. Each month we answer the most-asked question in a featured guide.",
           "Your question shapes our next guide", "chat", "teal")]
    c_html = "".join(f'''<div class="card"><div class="ico bg-{c}" style="width:48px;height:48px;border-radius:14px;display:grid;place-items:center">{ICONS[i]}</div><h3 class="mt-2">{t}</h3><p class="muted" style="font-size:14px;margin:0 0 8px"><strong>Who:</strong> {w}</p><p>{d}</p><p style="font-size:15px"><strong>Prize:</strong> {p}</p></div>''' for t, w, d, p, i, c in cs)
    body = hero("Contests &amp; prizes", "Creative challenges that make health learning fun — for classrooms, creators and curious minds. Prizes are funded by supporters and sponsors.", "",
                [("Contests", None)], f'{ICONS["trophy"].replace("<svg", "<svg style=\"width:14px;height:14px\"")} Current challenges') + f'''
<section class="section-tight"><div class="container"><div class="grid g3">{c_html}</div></div></section>
<section class="bg-soft"><div class="container"><div class="grid g2" style="align-items:start">
<div class="tool-wrap"><h2 style="font-size:1.6rem">Enter or register interest</h2>
<form data-form="Contest entry / interest" data-success="You're registered! We'll email the brief, deadlines and upload instructions.">
  {honeypot()}<input type="hidden" name="Form" value="Contest entry">
  <div class="field"><label for="c-c">Contest</label><select id="c-c" name="Contest" required><option>Healthy Me Poster Challenge</option><option>Explain It in 60 Seconds</option></select></div>
  <div class="row"><div class="field"><label for="c-n">Your name (adult)</label><input id="c-n" name="name" required></div><div class="field"><label for="c-e">Email</label><input id="c-e" type="email" name="email" required></div></div>
  <div class="row"><div class="field"><label for="c-r">I am</label><select id="c-r" name="Entrant type"><option>Teacher entering a class</option><option>Parent/guardian entering for a minor</option><option>Creator 18+</option><option>Youth organization</option></select></div><div class="field"><label for="c-co">Country</label><input id="c-co" name="Country" required></div></div>
  <div class="field"><label for="c-l">Link to entry (optional — Drive, YouTube unlisted, etc.)</label><input id="c-l" type="url" name="Entry link" placeholder="https://"></div>
  <label class="check"><input type="checkbox" required> I'm 18+, I've read the official rules, and I have permission to submit this entry.</label>
  <button class="btn btn-primary btn-block" type="submit">Submit</button>{status()}
</form></div>
<div><div class="card"><h3>Official rules (summary)</h3><ul style="font-size:15px;color:var(--ink-2)">
<li>No purchase or donation necessary to enter or win. Void where prohibited.</li>
<li>Entries for anyone under 18 must be submitted by a parent, guardian or teacher. Never include a minor's full name, photo, school or contact details in public submissions.</li>
<li>Entries must be original, family-friendly and medically accurate. We may decline any entry.</li>
<li>Judging criteria: accuracy (40%), clarity (30%), creativity (30%). Winners are announced on this page and contacted by email.</li>
<li>Prize values and deadlines are announced with each round. Prizes are not transferable; winners are responsible for any taxes.</li>
<li>By entering you grant Puberty101.com a non-exclusive license to display the entry with credit. You keep ownership.</li></ul></div>
<div class="card mt-3" style="background:var(--tint-sun)"><h3>Sponsor a prize</h3><p>Put your brand behind classroom creativity. Prize sponsors are credited on the contest page and winners' gallery.</p><a class="btn btn-primary" href="advertise.html">Become a prize sponsor</a></div></div>
</div></div></section>'''
    return page("contests.html", "Puberty Education Contests & Prizes", "Classroom poster challenges, 60-second explainer contests and monthly question picks — creative health-education contests with sponsor-funded prizes.", body, no_modal=True)


def careers():
    roles = [("Medical reviewer", "MD, NP, RN, pediatric or adolescent health background. Review guides for accuracy (remote, paid per review).", "shield"),
             ("Health writer", "Plain-language writers with health-education experience for teen and parent audiences.", "book"),
             ("Illustrator / animator", "Friendly, inclusive, non-graphic illustration and short animated explainers.", "sparkle"),
             ("Video creator", "Script-to-screen explainers for YouTube and the site.", "play"),
             ("School outreach ambassador", "Educators who connect us with schools and run parent nights (commission + stipend).", "school"),
             ("Translator", "Spanish, French, Hindi and other languages to make every guide global.", "chat")]
    r_html = "".join(f'<div class="card"><div class="ico bg-brand" style="width:44px;height:44px;border-radius:12px;display:grid;place-items:center">{ICONS[i]}</div><h3 class="mt-2">{t}</h3><p class="muted">{d}</p></div>' for t, d, i in roles)
    opts = "".join(f"<option>{t}</option>" for t, _, _ in roles)
    body = hero("Join the team", "We're building the internet's most trusted, friendliest puberty resource — and we're hiring freelancers, reviewers and partners worldwide.", "",
                [("Careers", None)], "Remote · freelance · global") + f'''
<section class="section-tight"><div class="container"><div class="grid g3">{r_html}</div></div></section>
<section class="bg-soft"><div class="container narrow"><div class="tool-wrap"><h2 style="font-size:1.6rem">Apply or introduce yourself</h2>
<form data-form="Talent application" data-success="Thanks! We review every application and will reply if there's a fit.">
  {honeypot()}<input type="hidden" name="Form" value="Talent application">
  <div class="row"><div class="field"><label for="j-n">Full name</label><input id="j-n" name="name" required></div><div class="field"><label for="j-e">Email</label><input id="j-e" type="email" name="email" required></div></div>
  <div class="row"><div class="field"><label for="j-r">Role</label><select id="j-r" name="Role" required>{opts}<option>Something else</option></select></div><div class="field"><label for="j-l">Location / time zone</label><input id="j-l" name="Location"></div></div>
  <div class="row"><div class="field"><label for="j-p">Portfolio / LinkedIn</label><input id="j-p" type="url" name="Portfolio" placeholder="https://"></div><div class="field"><label for="j-c">Credentials (if any)</label><input id="j-c" name="Credentials" placeholder="e.g. RN, M.Ed., MPH"></div></div>
  <div class="field"><label for="j-m">Why you, in a few lines</label><textarea id="j-m" name="Message" required></textarea></div>
  <label class="check"><input type="checkbox" required> I'm 18 or older.</label>
  <button class="btn btn-primary btn-block" type="submit">Send application</button>{status()}
</form></div></div></section>'''
    return page("careers.html", "Careers: Writers, Medical Reviewers & Creators", "Join Puberty101.com: freelance medical reviewers, health writers, illustrators, video creators, school ambassadors and translators.", body, no_modal=True)


def advertise():
    pk = [("Starter", "Sponsored guide", ["One sponsored, clearly labeled guide", "Logo on related tool page", "Newsletter mention", "Monthly performance report"]),
          ("Partner", "Category sponsorship", ["Exclusive sponsor of a topic hub (e.g. Periods)", "Co-branded printable resource", "2 newsletter features", "Quarterly brand-lift review"]),
          ("Founding", "Program sponsorship", ["Fund a school kit program or video series", "Recognition on classroom materials", "Contest title sponsorship", "Custom research &amp; reporting"])]
    p_html = "".join(f'''<div class="card tier{' featured' if i == 1 else ''}"><h3>{n}</h3><p class="muted">{s}</p><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul><a class="btn {'btn-primary' if i == 1 else 'btn-ghost'} btn-block" href="#media-kit">Request pricing</a></div>''' for i, (n, s, xs) in enumerate(pk))
    body = hero("Advertise &amp; sponsor", "Reach parents, educators and older teens at the exact moment they're looking for trusted answers — in a brand-safe, education-first environment.", "",
                [("Advertise", None)], "Partnerships") + f'''
<section class="section-tight"><div class="container"><div class="grid g4">
<div class="fact"><b>3</b><span>Audiences: teens 13+, parents, educators</span></div>
<div class="fact"><b>18+</b><span>In-depth evergreen guides</span></div>
<div class="fact"><b>6</b><span>Interactive tools with high repeat use</span></div>
<div class="fact"><b>100%</b><span>Clearly labeled sponsorships</span></div>
</div></div></section>
<section class="section-tight"><div class="container"><div class="section-head"><h2>Sponsorship packages</h2><p>Ideal for period-care, personal-care, pediatric health, telehealth, education and youth-wellbeing brands.</p></div><div class="grid g3">{p_html}</div></div></section>
<section class="bg-soft" id="media-kit"><div class="container"><div class="grid g2" style="align-items:start">
<div class="tool-wrap"><h2 style="font-size:1.6rem">Request the media kit</h2>
<form data-form="Advertising / sponsorship inquiry" data-success="Thanks! The media kit and rate card are on their way within 1 business day.">
  {honeypot()}<input type="hidden" name="Form" value="Advertising inquiry">
  <div class="row"><div class="field"><label for="a-n">Name</label><input id="a-n" name="name" required></div><div class="field"><label for="a-e">Work email</label><input id="a-e" type="email" name="email" required></div></div>
  <div class="row"><div class="field"><label for="a-c">Company</label><input id="a-c" name="Company" required></div><div class="field"><label for="a-w">Website</label><input id="a-w" type="url" name="Website" placeholder="https://"></div></div>
  <div class="row"><div class="field"><label for="a-i">Interested in</label><select id="a-i" name="Interest"><option>Sponsored guide</option><option>Category sponsorship</option><option>School kit program</option><option>Video series</option><option>Contest sponsorship</option><option>Newsletter</option><option>Domain / site acquisition</option></select></div>
  <div class="field"><label for="a-b">Budget</label><select id="a-b" name="Budget"><option>Under $1,000</option><option>$1,000–$5,000</option><option>$5,000–$20,000</option><option>$20,000+</option></select></div></div>
  <div class="field"><label for="a-m">Goals</label><textarea id="a-m" name="Message" style="min-height:90px"></textarea></div>
  <button class="btn btn-primary btn-block" type="submit">Send me the media kit</button>{status()}
</form><p class="form-note">Interested in acquiring or partnering on this website or domain? <a href="{CONTACT_URL}" target="_blank" rel="noopener">Contact us here</a>.</p></div>
<div class="card"><h3>Brand-safety standards</h3><p class="muted">Our audience includes young people, so we hold partners to a high bar.</p><ul style="font-size:15px;color:var(--ink-2)">
<li>All sponsored content is clearly labeled "Sponsored" and editorially independent.</li>
<li>No ads or sponsorships for diet products, weight-loss, cosmetic procedures, dating, alcohol, tobacco/vaping, gambling or adult content.</li>
<li>No targeting of individual users under 18; no collection of minors' personal data for marketing.</li>
<li>Product mentions never replace medical guidance; sponsors can't edit health facts.</li>
<li>We reserve the right to decline any partner.</li></ul></div>
</div></div></section>'''
    return page("advertise.html", "Advertise & Sponsor Puberty Education", "Sponsor brand-safe puberty education: sponsored guides, category sponsorships, school period-kit programs, video series and contests.", body, no_modal=True)


def about():
    body = hero("About Puberty101.com", "We believe every young person deserves clear, kind and accurate answers about their changing body — and every parent and teacher deserves tools that make those conversations easier.", "",
                [("About", None)], "Our mission") + f'''
<section class="section-tight legal"><div class="container narrow prose">
<h2>Why we exist</h2><p>Puberty is universal, yet good information about it is surprisingly hard to find in one place. Teen resources rarely connect to parent resources, boys' puberty is under-covered, and many families still rely on a single awkward "big talk." Puberty101.com brings teen guides, parent conversation tools and classroom resources together, on every topic, in plain language.</p>
<h2>What we do</h2><ul><li><strong>Guides</strong> on body changes, periods, hygiene, feelings, body image and body safety.</li><li><strong>Interactive tools</strong> — a body-changes explorer, period predictor, quiz, kit builder and conversation starters.</li><li><strong>Resources for schools</strong> — lesson structure, parent-night materials and sponsored product kits.</li><li><strong>Anonymous Q&amp;A</strong> so nobody has to stay confused because a question felt too embarrassing.</li></ul>
<h2>Our principles</h2><ul><li>Accurate: written in line with guidance from pediatric and public-health bodies, with sources on every guide.</li><li>Age-appropriate: clinical, respectful language — never graphic.</li><li>Inclusive: every body, every family, every learner.</li><li>Independent: advertisers and sponsors never influence health content. See our <a href="editorial-policy.html">editorial &amp; advertising policy</a>.</li><li>Safe: we don't collect personal data from children, and our question box is anonymous.</li></ul>
<h2>How we're funded</h2><p>Puberty101.com is free to use. We're supported by display advertising (Google AdSense), clearly labeled sponsorships, and contributions from readers. <a href="support.html">Support our work</a>.</p>
<h2>Get in touch</h2><p>Questions, corrections or partnership ideas? <a href="contact.html">Contact us</a>.</p>
</div></section>'''
    return page("about.html", "About Puberty101.com", "Puberty101.com is an independent resource offering clear, accurate, age-appropriate puberty education for teens, parents and educators.", body)


def editorial():
    body = hero("Editorial &amp; advertising policy", "How we research, write, review and correct our content — and how we keep advertising separate from health information.", "", [("Editorial policy", None)]) + f'''
<section class="section-tight legal"><div class="container narrow prose">
<h2>Sources</h2><p>Every guide is written in line with current public guidance from recognized bodies such as the American Academy of Pediatrics (HealthyChildren.org), the NHS, the World Health Organization, the CDC, Nemours KidsHealth, the American Academy of Dermatology, and national child-safety organizations. Each guide lists its key sources.</p>
<h2>Writing standards</h2><ul><li>Plain language, short paragraphs and clear "when to see a doctor" guidance.</li><li>Clinical, respectful, age-appropriate language. We never publish sexualized or graphic content.</li><li>Inclusive wording that respects every body and family.</li></ul>
<h2>Review &amp; updates</h2><p>Guides show a "last updated" date and are re-checked at least every 12 months, or sooner when guidance changes. We are building a panel of credentialed reviewers (physicians, nurses and health educators); reviewed guides will display the reviewer's name and credentials.</p>
<h2>Corrections</h2><p>If you spot an error, <a href="contact.html">contact us</a>. We correct verified errors promptly and note significant corrections at the end of the affected guide.</p>
<h2>Advertising</h2><ul><li>We display ads served by Google AdSense. Ads are visually separated from content.</li><li>Sponsored content is always labeled "Sponsored." Sponsors cannot edit or approve health information.</li><li>We do not accept advertising for diet or weight-loss products, cosmetic procedures, dating, alcohol, tobacco or vaping, gambling or adult content.</li><li>Mentioning a product type (for example, "pads" or "antiperspirant") is never an endorsement of a brand.</li></ul>
<h2>Medical disclaimer</h2><p>Our content is educational and does not replace professional care. See our full <a href="disclaimer.html">disclaimer</a>.</p>
</div></section>'''
    return page("editorial-policy.html", "Editorial & Advertising Policy", "How Puberty101.com sources, writes, reviews and corrects puberty education content, and how we keep advertising separate.", body)


def contact():
    body = hero("Contact us", "Questions, corrections, school requests or partnership ideas — we read every message.", "", [("Contact", None)]) + f'''
<section class="section-tight"><div class="container"><div class="grid g2" style="align-items:start">
<div class="tool-wrap"><form data-form="Contact form" data-success="Thanks for reaching out! We'll reply within 2 business days.">
  {honeypot()}<input type="hidden" name="Form" value="Contact">
  <div class="row"><div class="field"><label for="ct-n">Name</label><input id="ct-n" name="name" required autocomplete="name"></div><div class="field"><label for="ct-e">Email</label><input id="ct-e" type="email" name="email" required autocomplete="email"></div></div>
  <div class="field"><label for="ct-t">Topic</label><select id="ct-t" name="Topic"><option>General question</option><option>Correction / feedback</option><option>School or organization</option><option>Sponsorship / advertising</option><option>Donation</option><option>Media / press</option><option>Website or domain acquisition</option><option>Partnership</option></select></div>
  <div class="field"><label for="ct-m">Message</label><textarea id="ct-m" name="Message" required></textarea></div>
  <label class="check"><input type="checkbox" required> I'm 18 or older. (Teens: please use our <a href="ask.html">anonymous question box</a>.)</label>
  <button class="btn btn-primary btn-block" type="submit">Send message</button>{status()}
</form></div>
<div>
<div class="card"><h3>Prefer email?</h3><p class="muted">Click below to open a pre-addressed email in your mail app.</p><a class="btn btn-ghost" href="#" data-mail data-subject="Puberty101.com enquiry">{ICONS["mail"]} Email us</a></div>
<div class="card mt-3"><h3>Website, domain, sponsorship &amp; partnership</h3><p class="muted">Interested in this website, the domain name, sponsorship, advertising or partnership?</p><a class="btn btn-sun" href="{CONTACT_URL}" target="_blank" rel="noopener">Contact via web.works</a></div>
<div class="card mt-3"><h3>Quick links</h3><ul class="ticks dark" style="font-size:15px;margin:6px 0 0"><li><a href="schools.html">School resource request</a></li><li><a href="advertise.html">Media kit</a></li><li><a href="support.html">Donate</a></li><li><a href="careers.html">Join the team</a></li></ul></div>
</div></div></div></section>'''
    return page("contact.html", "Contact Puberty101.com", "Contact Puberty101.com for questions, corrections, school requests, sponsorship, advertising or partnership enquiries.", body, no_modal=True)


def resources():
    lines = [("United States", [("988 Suicide &amp; Crisis Lifeline", "Call or text 988", "https://988lifeline.org"), ("Childhelp National Child Abuse Hotline", "1-800-422-4453", "https://www.childhelp.org")]),
             ("Canada", [("Kids Help Phone", "1-800-668-6868 or text 686868", "https://kidshelpphone.ca")]),
             ("United Kingdom", [("Childline", "0800 1111", "https://www.childline.org.uk"), ("NSPCC Helpline (adults)", "0808 800 5000", "https://www.nspcc.org.uk")]),
             ("Australia", [("Kids Helpline", "1800 55 1800", "https://kidshelpline.com.au")]),
             ("India", [("CHILDLINE India", "1098", "https://www.childlineindia.org")])]
    l_html = "".join(f'<div class="card"><h3>{c}</h3><ul style="padding-left:1.1em">' + "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a> — <strong>{p}</strong></li>' for n, p, u in xs) + "</ul></div>" for c, xs in lines)
    orgs = [("HealthyChildren.org (American Academy of Pediatrics)", "https://www.healthychildren.org"), ("Nemours KidsHealth", "https://kidshealth.org"),
            ("NHS — Puberty and health", "https://www.nhs.uk"), ("World Health Organization — Adolescent health", "https://www.who.int"),
            ("Center for Young Women's Health", "https://youngwomenshealth.org"), ("Young Men's Health", "https://youngmenshealthsite.org"),
            ("AMAZE (animated videos)", "https://amaze.org"), ("Raising Children Network (Australia)", "https://raisingchildren.net.au"),
            ("Common Sense Media (online safety)", "https://www.commonsensemedia.org")]
    o_html = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in orgs)
    body = hero("Helplines &amp; trusted resources", "If you need to talk to someone, help is available. In an emergency, call your local emergency number.", "", [("Resources", None)]) + f'''
<section class="section-tight"><div class="container"><div class="grid g3">{l_html}</div>
<div class="card mt-4"><h3>Trusted organizations</h3><p class="muted">We're not affiliated with these organizations; we list them because they publish reliable information.</p><ul class="ticks dark" style="font-size:15px">{o_html}</ul></div>
<p class="form-note">Numbers verified October 2026. Services and numbers can change — check each organization's website.</p>
</div></section>'''
    return page("resources.html", "Helplines & Trusted Puberty Resources", "Youth helplines in the US, Canada, UK, Australia and India, plus trusted puberty and adolescent-health organizations.", body)


def search():
    body = hero("Search", "Find guides, tools and answers.", "", [("Search", None)]) + '''
<section class="section-tight"><div class="container narrow">
<div class="field"><label for="sq" class="sr-only">Search</label><input type="search" id="sq" placeholder="Try: first period, voice, acne, deodorant…" autofocus></div>
<div class="search-results" id="sr"></div></div></section>'''
    js = r'''<script>(function(){var I=[],q=document.getElementById("sq"),o=document.getElementById("sr");fetch("search-index.json").then(function(r){return r.json()}).then(function(d){I=d;var p=new URLSearchParams(location.search).get("q");if(p){q.value=p;run()}});
function run(){var v=q.value.trim().toLowerCase();if(!v){o.innerHTML="";return}var w=v.split(/\s+/);var res=I.map(function(x){var h=(x.t+" "+x.d+" "+x.k).toLowerCase(),s=0;w.forEach(function(t){if(h.indexOf(t)>-1)s++;if(x.t.toLowerCase().indexOf(t)>-1)s+=2});return[s,x]}).filter(function(a){return a[0]>0}).sort(function(a,b){return b[0]-a[0]}).slice(0,15);
o.innerHTML=res.length?res.map(function(a){var x=a[1];var e=document.createElement("a");e.href=x.u;e.innerHTML="<strong></strong><br><small></small>";e.querySelector("strong").textContent=x.t;e.querySelector("small").textContent=x.d;return e.outerHTML}).join(""):'<p class="muted">No results. Try another word, or <a href="ask.html">ask anonymously</a>.</p>'}q.addEventListener("input",run)})();</script>'''
    return page("search.html", "Search Puberty101", "Search Puberty101.com guides, tools and answers.", body, inline_js=js, noindex=True, ads=False, no_modal=True)


def legal_pages():
    out = {}
    pp = f'''<p><strong>Last updated:</strong> {UPDATED}</p>
<p>This Privacy Policy explains how Puberty101.com ("we", "us") handles information when you use this website. Questions? Use our <a href="contact.html">contact form</a>.</p>
<h2>Information we collect</h2><ul><li><strong>Information you submit:</strong> when an adult fills in a form (starter kit, newsletter, school request, donation pledge, contest, careers, advertising or contact), we receive the details entered, such as name, email and message.</li><li><strong>Anonymous questions:</strong> our question box does not ask for a name or email. Please do not include personal details.</li><li><strong>Automatically collected data:</strong> like most websites, our host and advertising partners may collect technical data such as IP address, browser type, pages viewed and cookies.</li><li><strong>On-device tools:</strong> the period predictor, kit builder and other tools run in your browser. Data you enter is not sent to us; some tools save preferences in your browser's local storage, which you can clear at any time.</li></ul>
<h2>How we use information</h2><ul><li>To send resources you request and reply to enquiries.</li><li>To send our newsletter if you subscribe (unsubscribe any time).</li><li>To improve the site and keep it secure.</li><li>We never sell personal information.</li></ul>
<h2>Form processing</h2><p>Form submissions are delivered to our team using FormSubmit (formsubmit.co), a third-party form-delivery service, which processes submissions under its own privacy policy.</p>
<h2>Advertising and Google AdSense</h2><p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this site and/or other sites on the internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. Learn more at <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">How Google uses information from sites that use its services</a>.</p>
<h2>Embedded content</h2><p>Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. Once played, YouTube may set cookies under Google's privacy policy.</p>
<h2>Children's privacy</h2><p>Our content is written for teens aged 13 and older, parents and educators. The site is not directed to children under 13, and we do not knowingly collect personal information from children under 13. All forms that collect contact details require confirmation that the person is 18 or older. If you believe a child has sent us personal information, contact us and we will delete it.</p>
<h2>Your rights</h2><p>Depending on where you live (for example, under the GDPR, UK GDPR, CCPA/CPRA or PIPEDA), you may have rights to access, correct, delete or restrict use of your personal information, and to object to processing. Contact us to make a request. We respond within the time required by law.</p>
<h2>Data retention &amp; security</h2><p>We keep submitted information only as long as needed for the purpose it was collected and use reasonable safeguards. No method of transmission over the internet is 100% secure.</p>
<h2>International visitors</h2><p>Information may be processed in countries other than your own, including the United States.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above.</p>'''
    cp = f'''<p><strong>Last updated:</strong> {UPDATED}</p>
<h2>What are cookies?</h2><p>Cookies are small text files stored on your device. We also use similar technologies such as local storage.</p>
<h2>Cookies we use</h2><ul><li><strong>Essential / preference:</strong> remember your theme (light/dark), cookie choice and on-device tool data (local storage).</li><li><strong>Advertising:</strong> Google AdSense and its partners use cookies to serve and measure ads, including personalized ads where permitted.</li><li><strong>Embedded media:</strong> YouTube may set cookies after you press play on a video.</li></ul>
<h2>Managing cookies</h2><p>You can block or delete cookies in your browser settings, and opt out of personalized ads at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>. Visitors in the EEA, UK and Switzerland will see a consent message managed through Google's certified consent tools where required.</p>'''
    tm = f'''<p><strong>Last updated:</strong> {UPDATED}</p>
<h2>Acceptance</h2><p>By using Puberty101.com you agree to these Terms. If you don't agree, please don't use the site.</p>
<h2>Educational use only</h2><p>All content is for general education and is not medical advice. See our <a href="disclaimer.html">Disclaimer</a>.</p>
<h2>Intellectual property</h2><p>The site's original text, design, graphics and tools are owned by Puberty101.com and protected by copyright. You may print or share individual pages and the Starter Kit for personal, family or classroom use with attribution. Any other reproduction, republication or commercial use requires written permission.</p>
<h2>User submissions</h2><p>By submitting questions, contest entries or other content, you confirm you have the right to do so and grant us a non-exclusive, royalty-free license to use, adapt and publish it (anonymously for questions). Do not submit personal information about yourself or others.</p>
<h2>Acceptable use</h2><p>Don't misuse the site, attempt to disrupt it, submit spam, or post unlawful, abusive or inappropriate content.</p>
<h2>Donations &amp; pledges</h2><p>Pledges are voluntary and non-refundable once paid unless required by law. Puberty101.com is not a registered charity and contributions are not tax-deductible.</p>
<h2>Third-party links &amp; content</h2><p>We link to and embed third-party content (including YouTube videos) that we don't control and aren't responsible for.</p>
<h2>Disclaimer of warranties &amp; limitation of liability</h2><p>The site is provided "as is" without warranties of any kind. To the fullest extent permitted by law, we are not liable for any damages arising from your use of the site.</p>
<h2>Changes</h2><p>We may update these Terms at any time by posting a new version here.</p>'''
    dc = f'''<p><strong>Last updated:</strong> {UPDATED}</p>
<h2>Medical disclaimer</h2><p>Puberty101.com provides general educational information about puberty and adolescent health. It is not medical advice, diagnosis or treatment and does not create a clinician–patient relationship. Always seek the advice of a doctor, nurse or other qualified health professional with any questions about a medical condition. Never ignore professional advice or delay seeking it because of something you read here. If you think you or someone else may be in danger, call your local emergency number.</p>
<h2>Tool disclaimer</h2><p>Our interactive tools (including the Body Changes Explorer and Period Predictor) give general estimates based on typical ranges. They cannot predict individual development and must not be used for contraception or diagnosis.</p>
<h2>External links &amp; videos</h2><p>Links and embedded videos are provided for convenience. We don't control or endorse third-party sites, channels or products.</p>
<h2 id="trademark">Trademark &amp; copyright disclosure</h2>
<p>Puberty101.com is an independent educational publication operated as a website under the domain name puberty101.com. It is <strong>not affiliated with, endorsed by, sponsored by or otherwise connected to</strong> any company, organization, author, book, course, curriculum, program, app, product or registered or unregistered trademark that uses the name "Puberty 101", "Puberty101", "Puberty-101" or any similar name or mark. Any resemblance is coincidental and descriptive of the general subject ("an introduction to puberty").</p>
<p>All third-party names, brands, logos and trademarks mentioned on this site — including YouTube, Google, AMAZE, Mayo Clinic, the NHS, the American Academy of Pediatrics, Nemours KidsHealth and others — are the property of their respective owners and are used for identification and reference only. Their mention does not imply any affiliation or endorsement.</p>
<p>All original content on this site is &copy; Puberty101.com. Embedded videos remain the property of their creators and are displayed using YouTube's standard embedding features. If you believe any content infringes your rights, please <a href="contact.html">contact us</a> with details and we will review and respond promptly.</p>'''
    for f, t, d, c in [("privacy-policy.html", "Privacy Policy", "How Puberty101.com collects, uses and protects information, including Google AdSense cookies and children's privacy.", pp),
                       ("cookie-policy.html", "Cookie Policy", "How Puberty101.com and partners such as Google AdSense use cookies and local storage, and how to manage them.", cp),
                       ("terms.html", "Terms of Use", "The terms that govern use of Puberty101.com, including educational use, intellectual property and user submissions.", tm),
                       ("disclaimer.html", "Disclaimer & Trademark Notice", "Medical disclaimer, tool disclaimer and trademark and copyright disclosure for Puberty101.com.", dc)]:
        out[f] = page(f, t, d, hero(t, d, "", [(t, None)]) + f'<section class="section-tight legal"><div class="container narrow prose">{c}</div></section>')
    return out


def notfound():
    body = f'''<section class="hero"><div class="container center narrow"><span class="eyebrow">404</span><h1 class="mt-2">This page is still growing.</h1>
<p class="lead" style="margin:0 auto">We couldn't find that page — but we can help you find what you need.</p>
<div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="/index.html">Go home</a><a class="btn btn-ghost" href="/learn/">Browse guides</a><a class="btn btn-ghost" href="/search.html">Search</a></div></div></section>'''
    return page("404.html", "Page not found", "The page you were looking for could not be found.", body, noindex=True, ads=False, no_modal=True)
