"""Interactive tools."""
import json
from layout import page, hero, ICONS, esc, help_strip, SITE

R = "../"

TOOLS = [
    ("stage-explorer.html", "Body Changes Explorer", "Slide to any age and see which puberty changes are typical for girls or boys right now.", "sprout", "brand"),
    ("period-calculator.html", "Period Predictor", "Estimate upcoming periods from the last start date. Private — nothing leaves your device.", "calendar", "coral"),
    ("puberty-quiz.html", "Myth or Fact? Quiz", "12 quick questions to test what you really know about puberty.", "quiz", "sun"),
    ("period-kit-builder.html", "First-Period Kit Builder", "Build, check off and print a school-bag period kit.", "gift", "mint"),
    ("conversation-starters.html", "Conversation Starters", "Age-matched, low-pressure openers for parents and caregivers.", "chat", "teal"),
    ("glossary.html", "Puberty Glossary", "60+ puberty and health terms explained in plain language.", "book", "brand"),
]


def tool_page(fname, title, desc, body, js, schema_name):
    schema = {"@context": "https://schema.org", "@type": "WebApplication", "name": schema_name, "url": f"{SITE}/tools/{fname}",
              "applicationCategory": "HealthApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    return page(f"tools/{fname}", title, desc, body, active="Tools", schema=schema, inline_js=f"<script>{js}</script>")


def hub():
    cards = "".join(f'''<a class="path" href="{f}"><div class="ico bg-{c}">{ICONS[i]}</div><h3>{esc(t)}</h3><p>{esc(d)}</p><span class="go">Open tool →</span></a>''' for f, t, d, i, c in TOOLS)
    body = hero("Interactive puberty tools", "Free, private tools that make puberty easier to understand — no sign-up, no data stored on our servers.", R,
                [("Tools", None)], "6 free tools") + f'<section class="section-tight"><div class="container"><div class="paths">{cards}</div></div></section>'
    return page("tools/index.html", "Free Interactive Puberty Tools", "Free puberty tools: body changes explorer, period predictor, myth-or-fact quiz, first-period kit builder, conversation starters and glossary.", body, active="Tools")


# ---------------- Body Changes Explorer ----------------
STAGES = {
    "girls": [
        ["Breast budding (often the first sign)", 8, 13, "Small, sometimes tender bumps under one or both nipples. One side can start first — that's normal."],
        ["Body odour and more sweat", 8, 13, "Sweat glands become more active. Daily showers and deodorant help."],
        ["Pubic and underarm hair", 9, 14, "Starts fine and sparse, then gets darker and thicker over a few years."],
        ["Growth spurt", 9, 14, "Height can increase quickly for 2–3 years, often peaking around 11–12."],
        ["Wider hips and body-shape changes", 10, 15, "Natural fat distribution changes are a healthy part of growing."],
        ["Vaginal discharge", 9, 14, "Clear or white discharge often appears 6–12 months before the first period."],
        ["First period", 10, 15, "Usually about 2–3 years after breast budding; average around age 12."],
        ["Acne and oilier skin", 10, 17, "Hormones boost oil production. Gentle daily cleansing helps."],
        ["Bigger emotions and mood swings", 9, 17, "Brain changes plus hormones can make feelings more intense. Talking helps."],
    ],
    "boys": [
        ["Testicles get larger (usually the first sign)", 9, 14, "Often unnoticed, this is the typical first change, followed by other signs."],
        ["Body odour and more sweat", 9, 14, "Daily showers, clean clothes and deodorant become important."],
        ["Pubic and underarm hair", 10, 15, "Begins sparse and fine, then thickens."],
        ["Growth spurt", 11, 16, "Often later than girls, peaking around 13–14, and can last several years."],
        ["Voice deepening ('breaking')", 12, 16, "The voice box grows; cracks and squeaks are normal and temporary."],
        ["Some breast tissue swelling", 11, 15, "Common and usually goes away on its own within 1–2 years."],
        ["Acne and oilier skin", 11, 18, "Very common. See a doctor if it's painful or affecting confidence."],
        ["Facial and body hair", 13, 18, "Usually starts on the upper lip and grows in over several years."],
        ["Broader shoulders and more muscle", 13, 18, "Muscle mass increases in later puberty."],
        ["Bigger emotions and mood swings", 10, 17, "Hormones and brain development can intensify feelings. Talking helps."],
    ],
}


def explorer():
    body = hero("Body Changes Explorer", "Pick a body and slide to an age to see which changes are typical right now. Every body runs on its own schedule — this shows common ranges, not deadlines.", R,
                [("Tools", "tools/"), ("Body Changes Explorer", None)], "Interactive") + f'''
<section class="section-tight"><div class="container narrow">
<div class="tool-wrap">
  <div class="seg" role="tablist" aria-label="Choose body"><button class="on" data-body="girls">Girls</button><button data-body="boys">Boys</button></div>
  <div class="range-row mt-3"><label for="age" class="label" style="margin:0">Age</label><input id="age" type="range" min="7" max="18" value="11" aria-valuetext="11 years"><div class="age-badge" id="ageOut">11</div></div>
  <p class="muted" id="summary" style="margin-top:8px"></p>
  <div class="stage-list" id="list" aria-live="polite"></div>
  <p class="form-note mt-2">Ranges reflect typical timing described by pediatric organizations. Signs before age 8 (girls) or 9 (boys), or no signs by 13 (girls) or 14 (boys), are worth discussing with a doctor — see our <a href="../learn/early-or-late-puberty.html">early or late puberty guide</a>.</p>
</div>
<div class="grid g2 mt-3"><a class="card" href="../learn/puberty-changes-girls.html"><h3>Puberty for girls →</h3><p class="muted">Every change, explained.</p></a><a class="card" href="../learn/puberty-changes-boys.html"><h3>Puberty for boys →</h3><p class="muted">Every change, explained.</p></a></div>
</div></section>'''
    js = "var D=" + json.dumps(STAGES) + r''';
var body="girls",age=document.getElementById("age"),out=document.getElementById("ageOut"),list=document.getElementById("list"),sum=document.getElementById("summary");
function draw(){var a=+age.value;out.textContent=a;age.setAttribute("aria-valuetext",a+" years");var n=0;
list.innerHTML=D[body].map(function(s){var mid=(s[1]+s[2])/2,lvl,lab;
if(a<s[1]){lvl="later";lab="Usually later"}else if(a<mid){lvl="maybe";lab="May be starting";n++}else if(a<=s[2]+1){lvl="likely";lab="Often underway";n++}else{lvl="likely";lab="Usually well along";n++}
return '<div class="stage-item"><span class="lvl '+lvl+'">'+lab+'</span><div><strong>'+s[0]+'</strong><div class="muted" style="font-size:14.5px">'+s[3]+' <span style="white-space:nowrap">Typical start: '+s[1]+'–'+s[2]+'.</span></div></div></div>'}).join("");
sum.textContent="At "+a+", "+n+" of "+D[body].length+" changes could be starting or underway for "+body+". Starting earlier or later than friends is completely normal.";}
document.querySelectorAll("[data-body]").forEach(function(b){b.addEventListener("click",function(){body=b.getAttribute("data-body");document.querySelectorAll("[data-body]").forEach(function(x){x.classList.toggle("on",x===b)});draw()})});
age.addEventListener("input",draw);draw();'''
    return tool_page("stage-explorer.html", "Body Changes Explorer: What Happens at Each Age", "Interactive puberty timeline: slide to any age to see which body changes are typical for girls and boys, with healthy age ranges.", body, js, "Body Changes Explorer")


# ---------------- Period predictor ----------------
def period():
    body = hero("Period Predictor", "Enter the first day of the last period to estimate the next few. In the first couple of years, cycles are often irregular — use this as a rough guide for packing your kit, not a promise.", R,
                [("Tools", "tools/"), ("Period Predictor", None)], "Private · on-device") + '''
<section class="section-tight"><div class="container narrow"><div class="tool-wrap">
<div class="row" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px">
  <div class="field"><label for="last">First day of last period</label><input type="date" id="last"></div>
  <div class="field"><label for="cyc">Usual cycle length (days)</label><input type="number" id="cyc" min="21" max="45" value="28"></div>
  <div class="field"><label for="len">Period length (days)</label><input type="number" id="len" min="2" max="8" value="5"></div>
</div>
<button class="btn btn-primary" id="go">Predict my next periods</button>
<div id="res" aria-live="polite"></div>
<p class="form-note mt-2">🔒 Everything is calculated in your browser. Nothing you type is sent or saved. For teens, cycles between 21 and 45 days are common. If periods last more than 7 days, soak a pad or tampon every 1–2 hours, or stop for 3+ months after becoming regular, talk to a doctor.</p>
</div>
<div class="grid g2 mt-3"><a class="card" href="../learn/first-period-guide.html"><h3>First period guide →</h3><p class="muted">What to expect and how to get ready.</p></a><a class="card" href="period-kit-builder.html"><h3>Build a period kit →</h3><p class="muted">Checklist you can print.</p></a></div>
</div></section>'''
    js = r'''var l=document.getElementById("last");l.valueAsDate=new Date();
document.getElementById("go").addEventListener("click",function(){var d=l.valueAsDate,c=+document.getElementById("cyc").value||28,n=+document.getElementById("len").value||5,res=document.getElementById("res");
if(!d){res.innerHTML='<p class="form-status err">Please choose a date.</p>';return}
c=Math.min(45,Math.max(21,c));var o={month:"short",day:"numeric",year:"numeric"},h='<div class="cal">';
for(var i=1;i<=6;i++){var s=new Date(d.getTime()+i*c*864e5),e=new Date(s.getTime()+(n-1)*864e5);h+='<div><small class="muted">Period '+i+'</small><b>'+s.toLocaleDateString(undefined,o)+'</b><span class="muted" style="font-size:13px">to '+e.toLocaleDateString(undefined,o)+'</span></div>'}
res.innerHTML=h+'</div><p class="muted mt-2" style="font-size:14px">Tip: put a kit in your bag a few days before each estimate — early cycles can arrive a week early or late.</p>'});'''
    return tool_page("period-calculator.html", "Period Predictor for Teens (Private Period Calculator)", "Free private period predictor for teens: estimate your next six periods from your last start date. Nothing is stored or sent.", body, js, "Period Predictor")


# ---------------- Quiz ----------------
QUIZ = [
    ["Everyone starts puberty at about the same age.", False, "Puberty can normally begin anywhere from about 8 to 13 for girls and 9 to 14 for boys."],
    ["For many girls, breast budding is the first sign of puberty.", True, "Breast buds are usually the first visible change, often 2–3 years before the first period."],
    ["You can't go swimming during your period.", False, "You can swim with a tampon or menstrual cup, or with period swimwear."],
    ["Acne is caused by not washing your face enough.", False, "Hormones increase oil production; washing helps but isn't the cause. Effective treatments exist."],
    ["Voice changes for boys usually happen all at once, overnight.", False, "The voice deepens gradually over months; cracks and squeaks are part of it."],
    ["Some breast swelling in boys during puberty is common.", True, "Many boys get mild breast tissue swelling that usually fades within 1–2 years."],
    ["Teens need more sleep than adults.", True, "Teens generally need about 8–10 hours a night for healthy growth and mood."],
    ["Periods in the first year are often irregular.", True, "It can take a year or two for cycles to settle into a regular pattern."],
    ["Mood swings during puberty mean something is wrong with you.", False, "Changing hormones and a developing brain make feelings more intense. It's normal — and talking helps."],
    ["Deodorant and antiperspirant are exactly the same thing.", False, "Deodorant masks odour; antiperspirant reduces sweat. Many products do both."],
    ["Growth spurts can cause temporary clumsiness.", True, "Bones can grow faster than coordination adjusts, so a little clumsiness is common."],
    ["If puberty hasn't started by 14 in a boy, it's worth seeing a doctor.", True, "No signs by 14 (boys) or 13 (girls) is a good reason for a check-up."],
]


def quiz():
    body = hero("Myth or Fact? The Puberty Quiz", "12 quick questions. No sign-up. See how much you really know — and learn something along the way.", R,
                [("Tools", "tools/"), ("Puberty Quiz", None)], "2-minute quiz") + '''
<section class="section-tight"><div class="container narrow"><div class="tool-wrap">
<div class="meter"><i id="bar"></i></div><p class="muted mt-1" id="count" style="font-size:14px"></p>
<div id="qbox"><div class="quiz-q" id="q"></div>
<div class="quiz-opts"><button data-a="1">Fact</button><button data-a="0">Myth</button></div>
<div class="quiz-explain" id="ex"></div>
<button class="btn btn-primary mt-2" id="next" style="display:none">Next question →</button></div>
<div id="done" style="display:none" class="center"><h2 id="score"></h2><p class="muted" id="msg"></p><div class="hero-actions" style="justify-content:center"><button class="btn btn-primary" id="again">Try again</button><a class="btn btn-ghost" href="../learn/puberty-myths-vs-facts.html">Read 15 myths vs facts</a><button class="btn btn-ghost" data-share>Share the quiz</button></div></div>
</div></div></section>'''
    js = "var Q=" + json.dumps(QUIZ) + r''';var i=0,s=0,lock=false,qe=document.getElementById("q"),ex=document.getElementById("ex"),nx=document.getElementById("next"),bs=document.querySelectorAll(".quiz-opts button");
function show(){lock=false;qe.textContent=Q[i][0];ex.classList.remove("show");nx.style.display="none";bs.forEach(function(b){b.className=""});document.getElementById("count").textContent="Question "+(i+1)+" of "+Q.length+" · Score "+s;document.getElementById("bar").style.width=(i/Q.length*100)+"%"}
bs.forEach(function(b){b.addEventListener("click",function(){if(lock)return;lock=true;var ans=b.getAttribute("data-a")==="1",ok=ans===Q[i][1];if(ok)s++;b.className=ok?"right":"wrong";bs.forEach(function(x){if((x.getAttribute("data-a")==="1")===Q[i][1])x.className="right"});ex.innerHTML="<strong>"+(Q[i][1]?"Fact. ":"Myth. ")+"</strong>"+Q[i][2];ex.classList.add("show");nx.style.display="inline-flex";nx.textContent=i===Q.length-1?"See my score →":"Next question →"})});
nx.addEventListener("click",function(){i++;if(i>=Q.length){document.getElementById("qbox").style.display="none";document.getElementById("done").style.display="block";document.getElementById("bar").style.width="100%";document.getElementById("score").textContent=s+" / "+Q.length;document.getElementById("msg").textContent=s>=10?"Puberty pro! You could teach this.":s>=7?"Nice work — you know the basics well.":"Good start — our guides will fill in the rest.";return}show()});
document.getElementById("again").addEventListener("click",function(){i=0;s=0;document.getElementById("qbox").style.display="";document.getElementById("done").style.display="none";show()});show();'''
    schema_q = {"@context": "https://schema.org", "@type": "Quiz", "name": "Puberty Myth or Fact Quiz", "about": "Puberty",
                "hasPart": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ("Fact. " if a else "Myth. ") + e}} for q, a, e in QUIZ]}
    p = tool_page("puberty-quiz.html", "Puberty Quiz: Myth or Fact? (12 Questions)", "Take the free 12-question puberty quiz. Separate myths from facts about periods, voice changes, acne, growth spurts and moods.", body, js, "Puberty Quiz")
    return p.replace("</head>", f'<script type="application/ld+json">{json.dumps(schema_q)}</script></head>')


# ---------------- Kit builder ----------------
KIT = {
    "Essentials": ["2–3 pads (regular absorbency)", "1–2 panty liners", "A clean pair of underwear", "Small zip or wet bag for used items", "Unscented wipes"],
    "Comfort": ["Pain relief your parent or doctor has OK'd", "Small snack", "Hair tie", "Spare dark leggings or shorts"],
    "Confidence": ["A note with a trusted adult's number", "Small hand sanitizer", "Lip balm", "Mini deodorant"],
    "Optional extras": ["Period underwear", "Tampons (if you've learned to use them)", "Heat patch", "Small mirror"],
}


def kit_builder():
    groups = ""
    k = 0
    for g, items in KIT.items():
        lis = ""
        for it in items:
            k += 1
            lis += f'<label><input type="checkbox" data-k="{k}"><span>{esc(it)}</span></label>'
        groups += f'<h3 class="mt-3">{esc(g)}</h3><div class="checklist">{lis}</div>'
    body = hero("First-Period Kit Builder", "Check off what you've packed. Your list is saved in this browser only, and you can print it for your bag or a shopping trip.", R,
                [("Tools", "tools/"), ("Period Kit Builder", None)], "Printable") + f'''
<section class="section-tight"><div class="container narrow"><div class="tool-wrap">
<div class="meter"><i id="bar"></i></div><p class="muted mt-1" id="cnt"></p>
{groups}
<div class="hero-actions no-print"><button class="btn btn-primary" data-print>{ICONS["print"]} Print checklist</button><button class="btn btn-ghost" id="reset">Reset</button></div>
</div>
<p class="mt-3">Want the full family version? <a href="../learn/first-period-kit-checklist.html">Read the first-period kit guide</a> or <a href="#" data-open-kit>get the free printable starter kit</a>.</p>
</div></section>'''
    js = r'''var bx=document.querySelectorAll("[data-k]"),K="p101-kit";var st={};try{st=JSON.parse(localStorage.getItem(K)||"{}")}catch(e){}
function up(){var n=0;bx.forEach(function(b){if(b.checked)n++});document.getElementById("bar").style.width=(n/bx.length*100)+"%";document.getElementById("cnt").textContent=n+" of "+bx.length+" items packed"+(n===bx.length?" — you're ready! 🎉":"")}
bx.forEach(function(b){b.checked=!!st[b.getAttribute("data-k")];b.addEventListener("change",function(){st[b.getAttribute("data-k")]=b.checked;try{localStorage.setItem(K,JSON.stringify(st))}catch(e){}up()})});
document.getElementById("reset").addEventListener("click",function(){st={};try{localStorage.removeItem(K)}catch(e){}bx.forEach(function(b){b.checked=false});up()});up();'''
    return tool_page("period-kit-builder.html", "First-Period Kit Builder (Printable Checklist)", "Build a first-period kit for school with this free interactive, printable checklist: pads, spare underwear, comfort items and more.", body, js, "First-Period Kit Builder")


# ---------------- Conversation starters ----------------
STARTERS = {
    "7–9": [
        "I read that bodies start changing in the next few years. Have you heard anything about that at school?",
        "Did you know everyone's body grows on its own timetable? What do you think 'growing up' means?",
        "If you ever have a question about your body, you can always ask me — even the silly ones. Anything you've been wondering?",
        "Let's learn the proper names for body parts together — doctors use them, and so can we.",
        "What's the difference between a surprise and a secret? Let's talk about which ones are OK.",
        "Some kids your age start to notice body smell after sports. Want to pick out a deodorant together?",
    ],
    "10–11": [
        "Some kids in your class might be starting puberty already. Has anyone talked about it?",
        "When I was your age, nobody explained puberty to me. What would you want to know?",
        "Want to put together a 'just in case' kit for your school bag together?",
        "Your feelings might feel bigger lately — that's partly hormones. How have things been?",
        "I found a short video about body changes — want to watch it together and then ask me anything?",
        "If you'd rather write a question than say it out loud, you can leave a note on my pillow anytime.",
    ],
    "12–13": [
        "No lecture, I promise — is there anything about growing up you've been wondering about?",
        "Some things online about bodies aren't true. Seen anything that made you curious or confused?",
        "What do your friends say about puberty? Sometimes rumours go around — want to fact-check together?",
        "How's your sleep been? Teens actually need more of it than adults.",
        "If something ever made you uncomfortable — online or in person — I'd never be mad at you for telling me.",
        "Want to pick your own skincare or hygiene products this time? I'll cover it.",
    ],
    "14+": [
        "You're handling a lot of change. What's one thing that would make this year easier?",
        "Would you prefer to talk to a doctor alone at your next check-up? That's completely fine.",
        "Is there anything about your body or health you'd want to look up together — or on your own?",
        "How are you feeling about how you look these days? Social media can make that hard.",
        "You don't have to tell me everything — but who are the trusted adults you'd go to if you needed help?",
        "Is there anything you wish I'd explained better when you were younger?",
    ],
}


def starters():
    opts = "".join(f'<button class="{"on" if i == 1 else ""}" data-age="{esc(a)}">{esc(a)}</button>' for i, a in enumerate(STARTERS))
    body = hero("Conversation Starters for Parents", "The hardest part is the first sentence. Pick your child's age and get a low-pressure opener — then let them lead.", R,
                [("Tools", "tools/"), ("Conversation Starters", None)], "For parents & caregivers") + f'''
<section class="section-tight"><div class="container narrow"><div class="tool-wrap center">
<div class="seg" role="tablist" aria-label="Child age">{opts}</div>
<blockquote id="line" style="font-family:var(--display);font-size:1.5rem;line-height:1.35;margin:28px auto;max-width:620px;min-height:120px" aria-live="polite"></blockquote>
<div class="hero-actions" style="justify-content:center"><button class="btn btn-primary" id="new">{ICONS["sparkle"]} Give me another</button><button class="btn btn-ghost" id="copy">Copy</button></div>
<p class="form-note">Tips: talk side-by-side (car rides, walks, cooking), keep it short, and end with "you can always ask me."</p>
</div>
<div class="lead-box mt-4"><div class="pitch"><span class="eyebrow">Free download</span><h3 class="mt-2">Want the full script library?</h3><ul class="ticks"><li>Age-by-age talk scripts (7 to 14+)</li><li>"What to say if…" quick answers</li><li>40 printable question-jar cards</li></ul></div><div class="form-side">{__import__("layout").kit_form(R, "cs", compact=True)}</div></div>
</div></section>'''
    js = "var S=" + json.dumps(STARTERS) + r''';var age="10–11",last=-1,line=document.getElementById("line");
function pick(){var a=S[age],k;do{k=Math.floor(Math.random()*a.length)}while(k===last&&a.length>1);last=k;line.textContent="“"+a[k]+"”"}
document.querySelectorAll("[data-age]").forEach(function(b){b.addEventListener("click",function(){age=b.getAttribute("data-age");document.querySelectorAll("[data-age]").forEach(function(x){x.classList.toggle("on",x===b)});last=-1;pick()})});
document.getElementById("new").addEventListener("click",pick);document.getElementById("copy").addEventListener("click",function(){if(navigator.clipboard)navigator.clipboard.writeText(line.textContent.replace(/[“”]/g,"")).then(function(){P101.toast("Copied")})});pick();'''
    return tool_page("conversation-starters.html", "Puberty Conversation Starters for Parents (By Age)", "Free generator of age-appropriate puberty conversation starters for parents and caregivers of kids aged 7 to 14+.", body, js, "Puberty Conversation Starters")


# ---------------- Glossary ----------------
GLOSSARY = [
    ("Acne", "Pimples, blackheads and whiteheads caused when oil and dead skin clog pores; very common during puberty."),
    ("Adolescence", "The life stage between childhood and adulthood, roughly ages 10–19, which includes puberty."),
    ("Adam's apple", "The bump at the front of the throat that becomes more visible as the voice box grows, especially in boys."),
    ("Androgens", "Hormones such as testosterone that drive many puberty changes in all bodies, including body hair and oil production."),
    ("Antiperspirant", "A product that reduces how much you sweat. Different from deodorant, which masks odour."),
    ("Areola", "The darker skin around the nipple, which may get larger and darker during puberty."),
    ("Body autonomy", "The idea that you have the right to decide what happens to your own body."),
    ("Body image", "How you see, think and feel about your body."),
    ("Breast buds", "Small, sometimes tender lumps under the nipple — usually the first sign of puberty in girls."),
    ("Cervix", "The lower, narrow part of the uterus that connects to the vagina."),
    ("Cramps", "Aches in the lower belly or back around a period, caused by the uterus contracting."),
    ("Delayed puberty", "When puberty hasn't started by about 13 in girls or 14 in boys; worth a doctor's check."),
    ("Deodorant", "A product that reduces or covers body odour."),
    ("Discharge", "Clear or white fluid from the vagina that keeps it healthy; often starts before the first period."),
    ("Endocrine system", "The system of glands that make hormones, including the pituitary gland, ovaries and testes."),
    ("Erection", "When the penis temporarily fills with blood and becomes firm; can happen unexpectedly during puberty and is normal."),
    ("Estrogen", "A hormone made mainly by the ovaries that drives breast development and the menstrual cycle."),
    ("Fallopian tubes", "Two narrow tubes that connect the ovaries to the uterus."),
    ("Follicle", "A tiny pocket in the skin that a hair grows from; or a small sac in the ovary that holds an egg."),
    ("Growth plate", "Areas of growing cartilage near the ends of long bones; they close after puberty when growth stops."),
    ("Growth spurt", "A period of rapid increase in height and weight during puberty."),
    ("Gynecomastia", "Swelling of breast tissue in boys; common during puberty and usually temporary."),
    ("Hormones", "Chemical messengers carried in the blood that tell the body what to do."),
    ("Hygiene", "Habits that keep your body clean and healthy, like showering and brushing your teeth."),
    ("Hypothalamus", "A part of the brain that starts puberty by signalling the pituitary gland."),
    ("Labia", "The folds of skin around the opening of the vagina."),
    ("Menarche", "The medical name for a person's very first period."),
    ("Menstrual cup", "A flexible reusable cup worn inside the vagina to collect period blood."),
    ("Menstrual cycle", "The monthly cycle of changes that prepares the body for a possible pregnancy, counted from the first day of one period to the next."),
    ("Menstruation", "Another word for a period: the monthly shedding of the uterus lining through the vagina."),
    ("Mood swings", "Quick changes in feelings, common during puberty because of hormones and brain development."),
    ("Nocturnal emission", "Also called a wet dream: a release of semen during sleep. Normal and not something you can control."),
    ("Ovaries", "Two small organs that store eggs and make estrogen and progesterone."),
    ("Ovulation", "When an ovary releases an egg, usually about two weeks before a period."),
    ("Pad", "An absorbent strip worn in underwear to collect period blood."),
    ("Panty liner", "A thin pad for light flow or discharge."),
    ("Penis", "The external male reproductive organ, which also carries urine out of the body."),
    ("Period underwear", "Absorbent, washable underwear that can be worn instead of or with pads or tampons."),
    ("Pituitary gland", "A pea-sized gland in the brain that releases hormones that start puberty."),
    ("PMS", "Premenstrual syndrome: physical and emotional symptoms in the days before a period, like bloating or irritability."),
    ("Precocious puberty", "Puberty that starts unusually early — before about 8 in girls or 9 in boys."),
    ("Progesterone", "A hormone made by the ovaries that helps regulate the menstrual cycle."),
    ("Puberty", "The years when a child's body develops into an adult body, driven by hormones."),
    ("Pubic hair", "Hair that grows around the genitals during puberty."),
    ("Scrotum", "The pouch of skin that holds the testicles."),
    ("Sebaceous glands", "Skin glands that make oil (sebum); they become more active in puberty."),
    ("Self-esteem", "How much you value and respect yourself."),
    ("Semen", "Fluid containing sperm, released from the penis."),
    ("Sperm", "Male reproductive cells made in the testicles after puberty starts."),
    ("Stretch marks", "Thin lines on the skin from fast growth; very common and fade over time."),
    ("Sweat glands", "Glands in the skin that make sweat; the ones under the arms become active in puberty."),
    ("Tampon", "A small plug of absorbent material worn inside the vagina to collect period blood."),
    ("Tanner stages", "A five-stage scale doctors use to describe how far along puberty is."),
    ("Testicles (testes)", "Two organs in the scrotum that make sperm and testosterone."),
    ("Testosterone", "The main androgen hormone, made mainly in the testicles; drives voice deepening and facial hair."),
    ("Trusted adult", "A grown-up you feel safe with and can go to for help, like a parent, teacher, coach or school nurse."),
    ("Urethra", "The tube that carries urine out of the body."),
    ("Uterus", "A hollow, muscular organ (also called the womb) whose lining sheds during a period."),
    ("Vagina", "The muscular passage that connects the uterus to the outside of the body."),
    ("Vulva", "The external genitals of the female body, including the labia and the opening of the vagina."),
    ("Voice breaking", "The deepening and cracking of the voice as the voice box grows during puberty."),
]


def glossary():
    items = "".join(f'<div data-term="{esc(t.lower())} {esc(d.lower())}"><dt id="{esc(t.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(chr(39), ""))}">{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in GLOSSARY)
    body = hero("Puberty Glossary", f"{len(GLOSSARY)} puberty and health words explained in plain, medically accurate language. Using correct names helps kids ask questions and stay safe.", R,
                [("Tools", "tools/"), ("Glossary", None)], "A–Z") + f'''
<section class="section-tight"><div class="container narrow">
<div class="field"><label for="gq" class="sr-only">Search the glossary</label><input type="search" id="gq" placeholder="Search a word, e.g. hormones"></div>
<dl class="glossary-list" id="gl">{items}</dl>
<p class="muted mt-3" id="gn" style="display:none">No matches. Try another word or <a href="../ask.html">ask us anonymously</a>.</p>
</div></section>'''
    js = r'''var q=document.getElementById("gq"),rows=document.querySelectorAll("#gl [data-term]");q.addEventListener("input",function(){var v=q.value.trim().toLowerCase(),n=0;rows.forEach(function(r){var ok=!v||r.getAttribute("data-term").indexOf(v)>-1;r.style.display=ok?"":"none";if(ok)n++});document.getElementById("gn").style.display=n?"none":"block"});'''
    schema = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Puberty Glossary",
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSSARY]}
    p = tool_page("glossary.html", "Puberty Glossary: Body & Health Terms Explained", "A plain-language A–Z glossary of 60+ puberty and health terms, from acne and hormones to menarche and voice breaking.", body, js, "Puberty Glossary")
    return p.replace("</head>", f'<script type="application/ld+json">{json.dumps(schema)}</script></head>')


def all_tools():
    return {"tools/index.html": hub(), "tools/stage-explorer.html": explorer(), "tools/period-calculator.html": period(),
            "tools/puberty-quiz.html": quiz(), "tools/period-kit-builder.html": kit_builder(),
            "tools/conversation-starters.html": starters(), "tools/glossary.html": glossary()}
