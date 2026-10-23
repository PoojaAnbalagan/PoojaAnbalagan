import os
from xml.sax.saxutils import escape as esc

OUT = "/mnt/user-data/outputs/profile/assets"
os.makedirs(OUT, exist_ok=True)

BG1, BG2 = "#0C1329", "#080D1B"
CYAN, INDIGO = "#67E8F9", "#818CF8"
CHIP, TXT, MUTED, SOFT = "#111A33", "#E2E8F0", "#94A3B8", "#CBD5E1"
SANS = "'Segoe UI','Inter','Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"

CSS = f"""
.s{{font-family:{SANS}}} .m{{font-family:{MONO}}}
@keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
@keyframes role{{0%{{opacity:0;transform:translateY(10px)}}4%,22%{{opacity:1;transform:translateY(0)}}27%,100%{{opacity:0;transform:translateY(-6px)}}}}
.up{{opacity:0;animation:up .7s ease-out forwards}}
.pl{{animation:pulse 2.4s ease-in-out infinite}}
.role{{opacity:0;animation:role 12s ease-in-out infinite backwards}}
@media (prefers-reduced-motion:reduce){{.up{{opacity:1;animation:none}}.pl,.role{{animation:none}}.role:first-of-type{{opacity:1}}}}
"""


def svg(w, h, body, label, rx=20):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">
<title>{esc(label)}</title>
<defs>
<style>{CSS}</style>
<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{INDIGO}"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="orb" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="{CYAN}" stop-opacity=".55"/><stop offset=".55" stop-color="{INDIGO}" stop-opacity=".18"/><stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#fff" stroke-opacity=".045"/></pattern>
<radialGradient id="gc"><stop offset="0" stop-color="{CYAN}" stop-opacity="1"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<radialGradient id="gi"><stop offset="0" stop-color="{INDIGO}" stop-opacity="1"/><stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
<clipPath id="fr"><rect width="{w}" height="{h}" rx="{rx}"/></clipPath>
</defs>
<g clip-path="url(#fr)">
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#grid)"/>
{body}
<rect width="{w}" height="3" fill="url(#acc)"/>
<rect width="260" height="3" fill="url(#sh)"><animateTransform attributeName="transform" type="translate" from="-260 0" to="{w} 0" dur="5s" repeatCount="indefinite"/></rect>
</g>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="{rx}" fill="none" stroke="url(#acc)" stroke-opacity=".35"/>
</svg>
'''


def save(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)


def orb(cx, cy, r, color, op, dur, dy=14):
    g = "gc" if color == CYAN else "gi"
    return (f'<circle cx="{cx}" cy="{cy}" r="{int(r*1.9)}" fill="url(#{g})" opacity="{op}">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -{dy};0 0" dur="{dur}s" repeatCount="indefinite"/></circle>')


def sphere(cx, cy, scale=1.0):
    return f'''<g transform="translate({cx} {cy}) scale({scale})">
<circle r="72" fill="url(#orb)"/>
<circle r="72" fill="none" stroke="#fff" stroke-opacity=".14"/>
<ellipse cx="-22" cy="-30" rx="26" ry="12" fill="#fff" opacity=".12" transform="rotate(-30 -22 -30)"/>
<g transform="rotate(-22)"><ellipse rx="112" ry="36" fill="none" stroke="{CYAN}" stroke-opacity=".45" stroke-dasharray="3 7"/>
<circle r="5" fill="{CYAN}"><animateMotion dur="7s" repeatCount="indefinite" path="M-112,0 a112,36 0 1,0 224,0 a112,36 0 1,0 -224,0"/></circle></g>
<g transform="rotate(38)"><ellipse rx="100" ry="30" fill="none" stroke="{INDIGO}" stroke-opacity=".5" stroke-dasharray="3 7"/>
<circle r="4.5" fill="{INDIGO}"><animateMotion dur="9s" repeatCount="indefinite" path="M100,0 a100,30 0 1,1 -200,0 a100,30 0 1,1 200,0"/></circle></g>
<g transform="rotate(100)"><ellipse rx="88" ry="26" fill="none" stroke="#fff" stroke-opacity=".18" stroke-dasharray="2 8"/>
<circle r="3.5" fill="#fff"><animateMotion dur="11s" repeatCount="indefinite" path="M-88,0 a88,26 0 1,0 176,0 a88,26 0 1,0 -176,0"/></circle></g>
<circle r="6" fill="url(#acc)"><animate attributeName="r" values="5;8;5" dur="3s" repeatCount="indefinite"/></circle>
</g>'''


def particles(w, h, n=10, xmin=20):
    import random
    random.seed(7)
    out = ""
    for i in range(n):
        x, y = random.randint(xmin, w - 20), random.randint(20, h - 20)
        c = CYAN if i % 2 == 0 else INDIGO
        out += (f'<circle cx="{x}" cy="{y}" r="{random.choice([1.2,1.6,2])}" fill="{c}" class="pl" '
                f'style="animation-delay:{random.random()*3:.1f}s"/>')
    return out


# ---------------------------------------------------------------- HEADER
def header():
    w, h = 1000, 360
    roles = ["Machine Learning", "NLP &amp; Transformers", "MLOps &amp; Deployment", "Full-Stack ML Apps"]
    role_svg = "".join(
        f'<text x="56" y="214" class="s role" style="animation-delay:{i*3}s" font-size="26" font-weight="600" fill="{CYAN}">{r}</text>'
        for i, r in enumerate(roles))
    body = (orb(820, 100, 90, CYAN, .28, 8) + orb(720, 290, 110, INDIGO, .32, 10, 18) + particles(w, h, 14, 520)
            + sphere(820, 180)
            + f'<text x="56" y="86" class="m" font-size="13" letter-spacing="3" fill="{MUTED}">DATA SCIENCE  /  ML ENGINEERING</text>'
            + f'<circle cx="40" cy="82" r="4" fill="{CYAN}" class="pl"/>'
            + '<text x="56" y="160" class="s up" font-size="58" font-weight="800" fill="url(#acc)" style="animation-delay:.1s">Pooja Anbalagan</text>'
            + role_svg
            + f'<text x="56" y="256" class="m" font-size="13" fill="{MUTED}">BSc (Hons) Data Science · Sabaragamuwa University of Sri Lanka · 2024–2028</text>'
            + f'<text x="56" y="298" class="s" font-size="15" fill="{SOFT}">Data Science undergraduate building practical ML applications,</text>'
            + f'<text x="56" y="320" class="s" font-size="15" fill="{SOFT}">from data and evaluation to APIs, containers, and deployment.</text>')
    save("header.svg", svg(w, h, body, "Pooja Anbalagan, Data Science undergraduate and ML engineer"))


# ---------------------------------------------------------------- FOOTER
def footer():
    w, h = 1000, 190
    waves = ""
    for i, (op, dur, col) in enumerate([(.5, 9, CYAN), (.4, 13, INDIGO)]):
        d = "M0,0 " + " ".join(f"q125,{-18 if k%2==0 else 18} 250,0" for k in range(10))
        waves += (f'<g transform="translate(0 {150+i*10})"><path d="{d}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="1.6">'
                  f'<animateTransform attributeName="transform" type="translate" from="{0 if i==0 else -500} 0" to="{-500 if i==0 else 0} 0" dur="{dur}s" repeatCount="indefinite"/></path></g>')
    body = (orb(180, 60, 70, CYAN, .25, 8) + orb(840, 120, 90, INDIGO, .3, 10) + particles(w, h, 10, 260)
            + sphere(120, 85, .55) + sphere(880, 85, .55)
            + f'<text x="500" y="66" text-anchor="middle" class="s" font-size="24" font-weight="800" fill="url(#acc)">Pooja Anbalagan</text>'
            + f'<text x="500" y="98" text-anchor="middle" class="m" font-size="12" letter-spacing="2.5" fill="{SOFT}">BETTER QUESTIONS · EVIDENCE-BASED MODELS</text>'
            + f'<text x="500" y="118" text-anchor="middle" class="m" font-size="12" letter-spacing="2.5" fill="{SOFT}">USEFUL SYSTEMS · CONTINUOUS LEARNING</text>'
            + waves)
    save("footer.svg", svg(w, h, body, "Footer: better questions, evidence-based models, useful systems, continuous learning"))


# ---------------------------------------------------------------- SECTION BANNERS
def section(n, title):
    w, h = 1000, 84
    col = CYAN if n % 2 else INDIGO
    body = (orb(900, 40, 50, col, .18, 8, 8)
            + f'<circle cx="54" cy="42" r="27" fill="none" stroke="{col}" stroke-opacity=".6" stroke-dasharray="4 7"><animateTransform attributeName="transform" type="rotate" from="0 54 42" to="360 54 42" dur="14s" repeatCount="indefinite"/></circle>'
            + f'<circle cx="54" cy="42" r="21" fill="{CHIP}" stroke="{col}" stroke-opacity=".8"/>'
            + f'<text x="54" y="48" text-anchor="middle" class="m" font-size="16" font-weight="700" fill="{col}">{n:02d}</text>'
            + f'<text x="104" y="48" class="s" font-size="22" font-weight="800" letter-spacing="2" fill="#fff">{esc(title)}</text>'
            + f'<text x="960" y="40" text-anchor="end" class="m" font-size="11" letter-spacing="2" fill="{MUTED}">SECTION {n:02d} / 07</text>'
            + ''.join(f'<circle cx="{948+i*0}" cy="0" r="0"/>' for i in range(0))
            + ''.join(f'<circle cx="{930+i*12}" cy="56" r="2.5" fill="{col}" class="pl" style="animation-delay:{i*.4}s"/>' for i in range(3))
            + f'<rect x="104" y="66" width="760" height="1" fill="url(#acc)" opacity=".3"/>'
            + f'<rect x="104" y="65" width="120" height="3" rx="1.5" fill="url(#acc)"><animateTransform attributeName="transform" type="translate" values="0 0;640 0;0 0" dur="6s" repeatCount="indefinite"/></rect>')
    save(f"section-{n:02d}.svg", svg(w, h, body, f"Section {n}: {title}", rx=16))


# ---------------------------------------------------------------- CHIPS (skills)
def chip(x, y, text, i):
    tl = len(text) * 7.2
    cw = tl + 33
    col = CYAN if i % 2 == 0 else INDIGO
    g = (f'<g class="up" style="animation-delay:{.15+i*.04:.2f}s"><rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="30" rx="9" fill="{CHIP}" stroke="{col}" stroke-opacity=".35"/>'
         f'<circle cx="{x+12:.1f}" cy="{y+15}" r="3" fill="{col}"/>'
         f'<text x="{x+23:.1f}" y="{y+19.5}" class="m" font-size="12" fill="{TXT}" textLength="{tl:.1f}" lengthAdjust="spacingAndGlyphs">{esc(text)}</text></g>')
    return g, cw


def chip_row(items, x0, y, maxw, start_i=0):
    x, out, i = x0, "", start_i
    for t in items:
        g, cw = chip(x, y, t, i)
        if x + cw > x0 + maxw:
            x, y = x0, y + 38
            g, cw = chip(x, y, t, i)
        out += g
        x += cw + 8
        i += 1
    return out, y + 30


def skills():
    groups = [
        ("PROGRAMMING & DATA ANALYSIS", ["Python", "SQL", "R", "JavaScript", "Pandas", "NumPy"]),
        ("MACHINE LEARNING, DEEP LEARNING & NLP", ["scikit-learn", "PyTorch", "TensorFlow", "DistilBERT", "MobileNetV3", "ONNX", "TF-IDF", "VADER", "Computer Vision"]),
        ("BACKEND, FRONTEND & DATABASES", ["FastAPI", "Django REST Framework", "React", "Next.js", "Express.js", "PostgreSQL", "MySQL", "SQLite"]),
        ("ENGINEERING, ANALYTICS & TOOLS", ["Git", "Docker", "Docker Compose", "Kubernetes", "GitHub Actions", "AWS Fundamentals", "Amazon S3", "AWS Lambda", "CloudWatch", "Linux", "Power BI", "Jupyter"]),
    ]
    y, body, k = 40, "", 0
    for gi, (name, items) in enumerate(groups):
        col = CYAN if gi % 2 == 0 else INDIGO
        body += f'<rect x="32" y="{y-9}" width="3" height="12" rx="1.5" fill="{col}"/><text x="44" y="{y+1}" class="m" font-size="11" letter-spacing="2" fill="{MUTED}">{esc(name)}</text>'
        row, yend = chip_row(items, 32, y + 16, 936, k)
        k += len(items)
        body += row
        y = yend + 34
    h = y - 6
    body = orb(900, h // 2, 80, INDIGO, .18, 9) + body
    save("skills.svg", svg(1000, h, body, "Technical skills grouped by programming, ML, backend and engineering"))


# ---------------------------------------------------------------- TILE GRID
def tiles(name, items, cols, label, th=92):
    w, gap, pad = 1000, 14, 32
    tw = (w - 2 * pad - gap * (cols - 1)) / cols
    rows = (len(items) + cols - 1) // cols
    h = pad * 2 - 4 + rows * th + (rows - 1) * gap
    body = orb(900, h // 2, 90, INDIGO, .16, 9)
    for i, (tag, title, detail) in enumerate(items):
        r, c = divmod(i, cols)
        x, y = pad + c * (tw + gap), pad - 2 + r * (th + gap)
        col = CYAN if (r + c) % 2 == 0 else INDIGO
        body += (f'<g class="up" style="animation-delay:{.1+i*.1:.1f}s"><rect x="{x:.0f}" y="{y}" width="{tw:.0f}" height="{th}" rx="14" fill="{CHIP}" stroke="{col}" stroke-opacity=".35"/>'
                 f'<rect x="{x:.0f}" y="{y+16}" width="3" height="{th-32}" rx="1.5" fill="{col}"/>'
                 f'<text x="{x+24:.0f}" y="{y+28}" class="m" font-size="11" font-weight="700" letter-spacing="2" fill="{col}">{esc(tag)}</text>'
                 f'<text x="{x+24:.0f}" y="{y+53}" class="s" font-size="16" font-weight="700" fill="#fff">{esc(title)}</text>'
                 f'<text x="{x+24:.0f}" y="{y+74}" class="s" font-size="12.5" fill="{MUTED}">{esc(detail)}</text></g>')
    save(name, svg(w, int(h), body, label))


# ---------------------------------------------------------------- PROJECT CARD
def card(name, idx, category, title, badge, desc, metrics, stack):
    w = 1000
    _row, _yend = chip_row(stack, 40, 256, 920, idx)
    h = _yend + 20
    body = orb(900, 60, 70, CYAN if idx % 2 else INDIGO, .2, 9)
    body += f'<circle cx="44" cy="42" r="4" fill="{CYAN}" class="pl"/>'
    body += f'<text x="58" y="46" class="m" font-size="11" letter-spacing="2" fill="{MUTED}">PROJECT {idx:02d}  ·  {esc(category)}</text>'
    body += f'<text x="40" y="86" class="s" font-size="27" font-weight="800" fill="#fff">{esc(title)}</text>'
    if badge:
        bw = len(badge) * 7.1 + 28
        body += (f'<rect x="{960-bw:.0f}" y="26" width="{bw:.0f}" height="26" rx="13" fill="{CHIP}" stroke="url(#acc)"/>'
                 f'<text x="{960-bw/2:.0f}" y="43" text-anchor="middle" class="m" font-size="11" font-weight="700" fill="{CYAN}">{esc(badge)}</text>')
    for i, line in enumerate(desc):
        body += f'<text x="40" y="{118+i*22}" class="s" font-size="14" fill="{SOFT}">{esc(line)}</text>'
    n, gap = len(metrics), 14
    mw = (920 - gap * (n - 1)) / n
    for i, (v, l) in enumerate(metrics):
        x = 40 + i * (mw + gap)
        col = CYAN if i % 2 == 0 else INDIGO
        body += (f'<g class="up" style="animation-delay:{.15+i*.12:.2f}s"><rect x="{x:.0f}" y="168" width="{mw:.0f}" height="70" rx="12" fill="{CHIP}" stroke="{col}" stroke-opacity=".3"/>'
                 f'<text x="{x+18:.0f}" y="201" class="m" font-size="23" font-weight="700" fill="url(#acc)">{esc(v)}</text>'
                 f'<text x="{x+18:.0f}" y="223" class="s" font-size="12" fill="{MUTED}">{esc(l)}</text></g>')
    body += _row
    save(name, svg(w, h, body, f"{title}: {category.title()}"))


# ---------------------------------------------------------------- WORKFLOW
def workflow():
    w, h = 1000, 250
    nodes = [("DATA", "Prepare · EDA · features"), ("EVALUATE", "Benchmarks · metrics"),
             ("SERVE", "FastAPI · REST endpoints"), ("DEPLOY", "Docker · Kubernetes · CI")]
    nw, nh, y = 190, 104, 70
    gap = (w - 2 * 48 - 4 * nw) / 3
    body = orb(500, 125, 120, INDIGO, .16, 10)
    cy = y + nh / 2
    body += f'<line x1="48" y1="{cy}" x2="{w-48}" y2="{cy}" stroke="url(#acc)" stroke-opacity=".35" stroke-dasharray="4 8"><animate attributeName="stroke-dashoffset" from="0" to="-24" dur="1.2s" repeatCount="indefinite"/></line>'
    for i, (t, d) in enumerate(nodes):
        x = 48 + i * (nw + gap)
        col = CYAN if i % 2 == 0 else INDIGO
        body += (f'<g><rect x="{x:.0f}" y="{y}" width="{nw}" height="{nh}" rx="16" fill="{CHIP}" stroke="{col}" stroke-opacity=".5"/>'
                 f'<rect x="{x:.0f}" y="{y}" width="{nw}" height="{nh}" rx="16" fill="none" stroke="{col}" stroke-width="2" class="pl" style="animation-delay:{i*.6}s"/>'
                 f'<text x="{x+22:.0f}" y="{y+32}" class="m" font-size="11" letter-spacing="2" fill="{col}">STEP {i+1}</text>'
                 f'<text x="{x+22:.0f}" y="{y+60}" class="s" font-size="20" font-weight="800" fill="#fff">{t}</text>'
                 f'<text x="{x+22:.0f}" y="{y+82}" class="s" font-size="12.5" fill="{MUTED}">{esc(d)}</text></g>')
    body += (f'<circle r="6" fill="{CYAN}"><animateMotion dur="5s" repeatCount="indefinite" path="M48,{cy} L{w-48},{cy}"/>'
             f'<animate attributeName="opacity" values="0;1;1;0" dur="5s" repeatCount="indefinite"/></circle>')
    body += f'<text x="500" y="214" text-anchor="middle" class="m" font-size="12" letter-spacing="2.5" fill="{SOFT}">MEASURABLE · REPRODUCIBLE · TESTABLE · USEFUL BEYOND A NOTEBOOK</text>'
    save("ml-workflow.svg", svg(w, h, body, "Workflow: data, evaluate, serve, deploy"))


# ---------------------------------------------------------------- BUTTONS
def button(name, glyph, small, big, col):
    w, h = 236, 58
    body = (f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="29" fill="{CHIP}" stroke="{col}" stroke-opacity=".35"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="29" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="40 {2*(w+h)}" stroke-linecap="round">'
            f'<animate attributeName="stroke-dashoffset" from="0" to="-{2*(w+h)-80}" dur="4s" repeatCount="indefinite"/></rect>'
            f'<circle cx="32" cy="29" r="18" fill="{BG2}" stroke="{col}" stroke-opacity=".6"/>'
            f'<text x="32" y="33" text-anchor="middle" class="m" font-size="11" font-weight="700" fill="{col}">{esc(glyph)}</text>'
            f'<text x="62" y="25" class="m" font-size="10" letter-spacing="2" fill="{MUTED}">{small}</text>'
            f'<text x="62" y="44" class="s" font-size="16" font-weight="800" fill="#fff">{big}</text>')
    s = (f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{small} {big}">'
         f'<title>{small} {big}</title><defs><style>{CSS}</style></defs>{body}</svg>\n')
    save(name, s)


header()
footer()
titles = ["ABOUT ME", "TECHNICAL SKILLS", "FEATURED PROJECTS", "FROM DATA TO DEPLOYMENT", "ACHIEVEMENTS", "LEADERSHIP & VOLUNTEERING", "GITHUB & CONTACT"]
for i, t in enumerate(titles, 1):
    section(i, t)
skills()

tiles("about.svg", [
    ("MACHINE LEARNING", "Models you can trust", "Classification, clustering, transfer learning, transformers"),
    ("DATA SCIENCE", "From raw data to insight", "Data prep, EDA, feature engineering, statistics, dashboards"),
    ("APPLICATIONS", "Models people can use", "REST APIs, full-stack integration, inference workflows"),
    ("ML ENGINEERING", "Reproducible and deployable", "Docker, Compose, Kubernetes manifests, GitHub Actions, ONNX"),
], 2, "Focus areas: machine learning, data science, applications, ML engineering")

tiles("achievements.svg", [
    ("1ST PRIZE", "IEEE WIE AURELIYA 2.0 Innovation Competition", "With the RelaunchHer team"),
    ("2ND PLACE", "CodeRally 7.0", "24-hour hackathon"),
    ("FINALIST", "CodeArena ’26", "With AgroGuard-AI, a crop-disease detection system"),
    ("FINALIST", "CryptX Hackathon", "Hackathon finalist"),
    ("FINALIST", "J’puraXtreme 3.0", "24-hour hackathon"),
    ("SHORTLIST", "HackElite 3.0", "Phase 2 · documentation contribution for CrowdVibe"),
], 2, "Achievements and hackathon results")

tiles("leadership.svg", [
    ("CHAIRPERSON · 2026/2027", "VisionVibe Magazine", "Rotaract Club of SUSL · leading the magazine team"),
    ("CO-CHAIRPERSON", "Event Coordinator", "Rotaract Club of SUSL · event planning and coordination"),
    ("ANNOUNCER", "Event host", "Rotaract Club, IEEE, and Computer Society events"),
    ("CREATIVE", "Content Writer & Graphic Designer", "Written and visual content for club activities"),
], 2, "Leadership and volunteering roles")

card("project-01.svg", 1, "FULL-STACK ML · NLP · DEPLOYMENT", "Customer Review Sentiment Analytics Platform", None,
     ["An end-to-end sentiment analytics platform serving predictions from a trained text-classification pipeline",
      "through a FastAPI backend and React/Vite frontend, with Docker, Kubernetes manifests and GitHub Actions CI."],
     [("90.93%", "DistilBERT accuracy"), ("0.8906", "DistilBERT macro-F1"), ("0.5539 → 0.8906", "Macro-F1: VADER → DistilBERT")],
     ["Python", "FastAPI", "scikit-learn", "DistilBERT", "React", "Vite", "Docker", "Kubernetes", "GitHub Actions"])
card("project-02.svg", 2, "COMPUTER VISION · TRANSFER LEARNING", "AgroGuard-AI", None,
     ["Multi-crop plant disease classifier using MobileNetV3-Small transfer learning across 112 plant pathology",
      "classes, exported to ONNX for CPU inference with a standalone CLI and a Node.js integration bridge."],
     [("95.28%", "Top-1 accuracy"), ("99.15%", "Top-3 accuracy"), ("94.23%", "Macro-F1"), ("~18.5 ms", "ONNX CPU latency / sample")],
     ["Python", "PyTorch", "MobileNetV3-Small", "ONNX", "Node.js"])
card("project-03.svg", 3, "TEAM PROJECT · REAL-TIME SYSTEMS", "CrowdVibe: Real-Time AI Crowd-Safety Platform", "TEAM PROJECT",
     ["Crowd-safety platform concept combining a FastAPI backend, React/Vite frontend, WebSockets and DBSCAN",
      "spatial clustering to flag crowd-density risks, with rule-based alerts and safe-route suggestions."],
     [("DBSCAN", "Spatial clustering of crowd density"), ("WebSockets", "Real-time snapshot broadcast"), ("My role", "Technical docs & project comms")],
     ["Python", "FastAPI", "scikit-learn", "DBSCAN", "WebSockets", "React", "Vite", "Vercel"])
card("project-04.svg", 4, "AWS · DATA ENGINEERING · MONITORING", "AWS Customer Churn Prediction Pipeline", "IN PROGRESS",
     ["Cloud data workflow for a customer-churn prediction group project: S3 storage, a Lambda CSV validator",
      "triggered on upload, and CloudWatch logs for debugging. Being refined, not a finished production deployment."],
     [("S3", "Project data & prediction outputs"), ("Lambda", "CSV validation on upload"), ("CloudWatch", "Logs for troubleshooting")],
     ["AWS S3", "AWS Lambda", "CloudWatch", "Python", "CSV", "IAM"])
card("project-05.svg", 5, "SOCIAL IMPACT · FULL-STACK WEB APP", "RelaunchHer", "1ST PRIZE · IEEE WIE AURELIYA 2.0",
     ["Platform helping Sri Lankan women returning from career breaks upskill and connect with partner tech",
      "employers. Team-built MVP with REST APIs, JWT authentication and a Prisma schema designed for PostgreSQL."],
     [("1st", "IEEE WIE AURELIYA 2.0"), ("JWT", "Auth + role-based route guards"), ("2 roles", "Returner & Employer experiences")],
     ["Next.js", "React", "Express", "TypeScript", "Prisma", "PostgreSQL", "JWT"])
card("project-06.svg", 6, "FULL-STACK DEVELOPMENT · REST APIS", "Barking Shelter", None,
     ["A pet-adoption platform intended to connect pets with potential adopters, built with a React frontend",
      "styled in Tailwind CSS and a Django REST Framework backend."],
     [("React", "Tailwind CSS frontend"), ("Django REST", "Backend API"), ("SQLite · MySQL", "Database integration & migration")],
     ["React", "Tailwind CSS", "Django REST Framework", "SQLite", "MySQL"])
card("project-07.svg", 7, "DATA ANALYTICS · POWER BI", "Tourist Analysis Dashboard", None,
     ["An interactive dashboard analysing tourism data from 2019–2023, transforming and exploring the data",
      "to find trends, with KPIs and visuals designed to support decision-making."],
     [("2019–2023", "Tourism data analysed"), ("Power BI", "Interactive dashboard"), ("KPIs", "Trends & decision support")],
     ["Power BI", "Data transformation", "KPI design", "Visualization"])

workflow()
button("btn-projects.svg", "</>", "EXPLORE", "PROJECTS", CYAN)
button("btn-linkedin.svg", "in", "CONNECT", "LINKEDIN", INDIGO)
button("btn-email.svg", "@", "CONTACT", "EMAIL", CYAN)
button("btn-github.svg", "{ }", "GITHUB", "REPOSITORIES", INDIGO)
print(sorted(os.listdir(OUT)))
