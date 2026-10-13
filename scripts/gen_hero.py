"""Generate assets/hero.svg: a MacBook 'About Me' screen next to an animated cyber dragon."""
import random
import sys

random.seed(7)
OUT = sys.argv[1]

W, H = 900, 372
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Menlo, Consolas, 'Courier New', monospace"

parts = []
add = parts.append

# ---------------------------------------------------------------- dragon shape
# Local dragon space (~0..320 x 0..360), facing left towards the MacBook.
DRAGON = (
    "M30,118 C60,104 95,96 125,92 C140,90 150,80 160,72 L175,70 "
    "C205,50 240,30 285,8 C245,40 215,62 198,84 L204,88 "
    "C230,78 255,72 290,70 C255,84 232,96 214,104 "
    "C222,112 226,122 228,132 L252,127 L234,143 "
    "C236,160 240,172 244,182 L270,172 L252,198 "
    "C256,208 260,216 264,224 L292,218 L274,243 "
    "C278,250 282,256 285,262 L313,262 L292,282 "
    "C296,292 299,300 301,310 L326,316 L303,330 "
    "C304,350 304,375 302,400 "
    "L236,400 "
    "C252,340 236,288 210,256 C186,226 172,202 165,178 "
    "C156,182 150,183 146,184 L140,199 L130,185 C118,186 108,186 100,185 L91,198 L84,183 C80,182 77,181 75,180 L52,172 "
    "C75,162 105,156 140,150 L150,140 "
    "C120,136 80,134 40,132 L30,127 Z"
)
DETAILS = [
    "M108,99 C125,93 142,89 158,84",               # brow ridge
    "M168,112 C182,124 186,142 178,162",           # cheek
    "M196,206 C210,214 222,222 232,236",           # neck scales
    "M214,246 C228,254 240,264 250,280",
    "M232,290 C246,300 256,312 262,330",
    "M80,170 C100,166 122,164 150,160",            # jaw line
]
EYE = "M126,108 L144,97 L165,98 L151,110 Z"
UPPER_TEETH = [(56, 133), (76, 134), (96, 135), (116, 136), (134, 138)]
LOWER_TEETH = [(66, 165), (86, 160), (106, 157), (126, 153)]


def teeth():
    out = []
    for x, y in UPPER_TEETH:
        out.append(f"M{x - 4},{y} L{x},{y + 8} L{x + 4},{y + 1} Z")
    for x, y in LOWER_TEETH:
        out.append(f"M{x - 4},{y} L{x},{y - 8} L{x + 4},{y - 1} Z")
    return " ".join(out)


DX, DY, DS = 566, 6, 0.96  # dragon placement

# ---------------------------------------------------------------- styles
css = f"""
.sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
.draw{{stroke-dasharray:1.01;stroke-dashoffset:1.01;animation:draw 2.4s cubic-bezier(.6,.05,.3,1) forwards}}
.d2{{animation-delay:1.6s;animation-duration:1.4s}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
.fillin{{opacity:0;animation:fadein 1.2s ease-out 1.9s forwards}}
@keyframes fadein{{to{{opacity:1}}}}
.glow{{opacity:0;animation:fadein 1s ease-out 2.4s forwards, pulse 3.2s ease-in-out 3.4s infinite}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:.85}}}}
.eye{{opacity:0;animation:fadein .4s ease-out 2.6s forwards}}
.eyeglow{{animation:eyeglow 1.8s ease-in-out infinite}}
@keyframes eyeglow{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.scan{{animation:scan 3.6s linear 3s infinite;opacity:0}}
@keyframes scan{{0%{{transform:translateY(-40px);opacity:0}}8%{{opacity:1}}92%{{opacity:1}}100%{{transform:translateY(380px);opacity:0}}}}
.rain{{animation:rain linear infinite}}
@keyframes rain{{from{{transform:translateY(-180px)}}to{{transform:translateY(0)}}}}
.bit{{opacity:0;animation:breath 2.6s ease-out infinite}}
@keyframes breath{{0%{{opacity:0;transform:translate(0,0) scale(.6)}}12%{{opacity:1}}100%{{opacity:0;transform:translate(var(--tx),var(--ty)) scale(1.25)}}}}
.ch{{fill-opacity:0;animation:fadein-ch .01s linear forwards}}
@keyframes fadein-ch{{to{{fill-opacity:1}}}}
.row{{opacity:0;animation:rowin .5s ease-out forwards}}
@keyframes rowin{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}
.blob{{animation:drift 12s ease-in-out infinite alternate}}
.blob2{{animation:drift 15s ease-in-out infinite alternate-reverse}}
@keyframes drift{{from{{transform:translate(0,0)}}to{{transform:translate(40px,-14px)}}}}
.cur{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.dot{{animation:pulse 2s ease-in-out infinite}}
"""

add(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" role="img" aria-label="MacBook screen showing Ahmet Ege Baykoz, BSc Computer Science '
    f'with Cyber Security at the University of York, next to an animated cyber dragon">')
add(f"<style>{css}</style>")

# ---------------------------------------------------------------- defs
add("<defs>")
add('<linearGradient id="wall" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#081028"/>'
    '<stop offset=".55" stop-color="#0d2650"/><stop offset="1" stop-color="#123a6b"/></linearGradient>')
add('<linearGradient id="dragonFill" x1="0" y1="0" x2=".6" y2="1"><stop offset="0" stop-color="#7fd8ff"/>'
    '<stop offset=".45" stop-color="#3b8cf0"/><stop offset="1" stop-color="#1b3f9e"/></linearGradient>')
add('<linearGradient id="icon" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5dc9f2"/>'
    '<stop offset="1" stop-color="#2a5fd6"/></linearGradient>')
add('<linearGradient id="base" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a4f59"/>'
    '<stop offset="1" stop-color="#1c1f24"/></linearGradient>')
add('<linearGradient id="scanband" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity="0"/>'
    '<stop offset=".5" stop-color="#d8f6ff" stop-opacity=".75"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>')
add('<filter id="blur30" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>')
add('<filter id="blur8" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="8"/></filter>')
add('<filter id="blur3" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.5"/></filter>')
add('<clipPath id="screen"><rect x="72" y="36" width="446" height="276" rx="6"/></clipPath>')
add(f'<clipPath id="dclip"><path d="{DRAGON}"/></clipPath>')
add('<clipPath id="panel"><rect width="900" height="372" rx="12"/></clipPath>')
add("</defs>")

# ---------------------------------------------------------------- panel
add('<rect width="900" height="372" rx="12" fill="#0b1120"/>')
add('<g clip-path="url(#panel)">')

# matrix rain behind the dragon
chars = "01アイウエカキクケサシ/{}#$"
for i, x in enumerate(range(600, 900, 20)):
    dur = random.uniform(5, 11)
    delay = -random.uniform(0, dur)
    col = "".join(random.choice(chars) for _ in range(40))
    tsp = "".join(f'<tspan x="{x}" dy="15">{c}</tspan>' for c in col)
    add(f'<text class="mono rain" y="-420" font-size="11" fill="#1a3d63" opacity=".55" '
        f'style="animation-duration:{dur:.1f}s;animation-delay:{delay:.1f}s">{tsp}</text>')
# fade the rain into the panel at the left edge
add('<linearGradient id="fadeL" x1="0" x2="1"><stop offset="0" stop-color="#0b1120"/>'
    '<stop offset="1" stop-color="#0b1120" stop-opacity="0"/></linearGradient>')
add('<rect x="580" y="0" width="60" height="372" fill="url(#fadeL)"/>')

# ---------------------------------------------------------------- MacBook
add('<ellipse cx="295" cy="346" rx="260" ry="6" fill="#000" opacity=".55" filter="url(#blur3)"/>')
add('<rect x="60" y="24" width="470" height="300" rx="16" fill="#15171c" stroke="#3b404c" stroke-width="1.5"/>')
add('<rect x="72" y="36" width="446" height="276" rx="6" fill="url(#wall)"/>')
add('<g clip-path="url(#screen)">')
add('<ellipse class="blob" cx="150" cy="280" rx="170" ry="60" fill="#5dc9f2" opacity=".35" filter="url(#blur30)"/>')
add('<ellipse class="blob2" cx="470" cy="90" rx="130" ry="55" fill="#e8384f" opacity=".28" filter="url(#blur30)"/>')
add('<ellipse class="blob" cx="420" cy="300" rx="120" ry="40" fill="#7b5cff" opacity=".25" filter="url(#blur30)"/>')
# menu bar
add('<rect x="72" y="36" width="446" height="13" fill="#000" opacity=".35"/>')
add(f'<text class="sans" x="82" y="45.5" font-size="8" fill="#fff"><tspan font-weight="700">◆ ahmet</tspan>'
    f'<tspan dx="10">File</tspan><tspan dx="9">Edit</tspan><tspan dx="9">View</tspan><tspan dx="9">Security</tspan></text>')
add('<text class="sans" x="508" y="45.5" font-size="8" fill="#fff" text-anchor="end">York, UK   ◔ 09:41</text>')
add('<rect x="277" y="36" width="36" height="9" rx="3" fill="#000"/>')

# About window
add('<rect x="108" y="60" width="374" height="218" rx="10" fill="#1b2030" fill-opacity=".97" stroke="#3a4462"/>')
for i, c in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    add(f'<circle cx="{122 + i * 13}" cy="73" r="4.2" fill="{c}"/>')
# app icon with shield
add('<rect x="273" y="78" width="44" height="44" rx="10" fill="url(#icon)"/>')
add('<path d="M295,86 L307,91 V100 C307,108 302,113 295,116 C288,113 283,108 283,100 V91 Z" fill="none" '
    'stroke="#fff" stroke-width="2" stroke-linejoin="round"/>')
add('<path d="M289.5,100.5 L293.5,104.5 L301,96.5" fill="none" stroke="#fff" stroke-width="2.2" '
    'stroke-linecap="round" stroke-linejoin="round"/>')

# name typed letter by letter
name = "Ahmet Ege Baykoz"
t0, step = 0.5, 0.09
spans = "".join(
    f'<tspan class="ch" style="animation-delay:{t0 + i * step:.2f}s">{c if c != " " else "&#160;"}</tspan>'
    for i, c in enumerate(name)
)
add(f'<text class="sans" x="295" y="146" font-size="19" font-weight="700" fill="#ffffff" text-anchor="middle">{spans}</text>')
t_name = t0 + len(name) * step

rows = [
    ("University", "University of York"),
    ("Year", "Second year · Class of 2029"),
    ("Focus", "Application &amp; cloud security"),
    ("Location", "York, United Kingdom"),
    ("Status", "Open to a 2027–28 placement"),
]
add(f'<g class="row" style="animation-delay:{t_name + .1:.2f}s"><text class="sans" x="295" y="163" font-size="10.5" '
    f'fill="#8f9bbb" text-anchor="middle">BSc (Hons) Computer Science with Cyber Security</text></g>')
for i, (k, v) in enumerate(rows):
    y = 185 + i * 15
    delay = t_name + 0.3 + i * 0.18
    colour = "#5dc9f2" if k == "Status" else "#e6e9f2"
    dot = (f'<circle class="dot" cx="{275 + 3}" cy="{y - 3.5}" r="2.6" fill="#3ddc84"/>' if k == "Status" else "")
    vx = 285 if k == "Status" else 276
    add(f'<g class="row" style="animation-delay:{delay:.2f}s">'
        f'<text class="sans" x="268" y="{y}" font-size="10" fill="#7f8aa6" text-anchor="end">{k}</text>{dot}'
        f'<text class="sans" x="{vx}" y="{y}" font-size="10" fill="{colour}">{v}</text></g>')
btn_delay = t_name + 0.3 + len(rows) * 0.18
add(f'<g class="row" style="animation-delay:{btn_delay:.2f}s">'
    f'<rect x="243" y="257" width="104" height="15" rx="4" fill="#2b3350" stroke="#46527c"/>'
    f'<text class="sans" x="295" y="267.5" font-size="9" fill="#e6e9f2" text-anchor="middle">e26180.github.io</text></g>')

# dock
add('<rect x="221" y="284" width="148" height="24" rx="7" fill="#ffffff" fill-opacity=".13" stroke="#ffffff" stroke-opacity=".2"/>')
dock = [
    ("#111418", "&gt;_", "#3ddc84"),
    ("#306998", "Py", "#ffd43b"),
    ("#e76f00", "J", "#ffffff"),
    ("#1679a7", "◢", "#ffffff"),
    ("#c51a4a", "π", "#ffffff"),
    ("#5dc9f2", "✎", "#0b1120"),
]
for i, (bg, glyph, fg) in enumerate(dock):
    x = 228 + i * 23
    add(f'<rect x="{x}" y="287" width="18" height="18" rx="4.5" fill="{bg}"/>')
    add(f'<text class="mono" x="{x + 9}" y="299.5" font-size="8.5" font-weight="700" fill="{fg}" text-anchor="middle">{glyph}</text>')
add("</g>")  # end screen clip
# base
add('<path d="M28,324 H562 V330 Q562,338 549,338 H41 Q28,338 28,330 Z" fill="url(#base)"/>')
add('<rect x="264" y="324" width="62" height="4" rx="2" fill="#121418"/>')

# ---------------------------------------------------------------- dragon
add(f'<g transform="translate({DX},{DY}) scale({DS})">')
add(f'<path d="{DRAGON}" fill="#3b8cf0" filter="url(#blur8)" class="glow"/>')
add(f'<path d="{DRAGON}" fill="url(#dragonFill)" class="fillin"/>')
add(f'<g clip-path="url(#dclip)"><rect class="scan" x="0" y="0" width="340" height="34" fill="url(#scanband)"/></g>')
add(f'<path d="{DRAGON}" fill="none" stroke="#a8ecff" stroke-width="2" stroke-linejoin="round" pathLength="1" class="draw"/>')
add('<path d="M42,116 C72,103 100,96 128,92" fill="none" stroke="#e4f9ff" stroke-opacity=".7" stroke-width="1.6" stroke-linecap="round" pathLength="1" class="draw d2"/>')
for d in DETAILS:
    add(f'<path d="{d}" fill="none" stroke="#0b1a3a" stroke-opacity=".55" stroke-width="2" stroke-linecap="round" pathLength="1" class="draw d2"/>')
add(f'<path d="{teeth()}" fill="#eaf8ff" class="fillin"/>')
add(f'<path d="M40,118 q4,-4 9,-2" fill="none" stroke="#0b1a3a" stroke-width="2" stroke-linecap="round" class="fillin"/>')
add(f'<g class="eye"><path class="eyeglow" d="{EYE}" fill="#ff2e4d" filter="url(#blur3)" transform="translate(145 104) scale(1.6) translate(-145 -104)"/>'
    f'<path d="{EYE}" fill="#ff3352" stroke="#0b1a3a" stroke-width="1.4" stroke-linejoin="round"/>'
    f'<path d="M148,98.5 Q145,103.5 147,109" stroke="#14070a" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    f'<circle cx="156" cy="101" r="1.4" fill="#fff"/></g>')

# binary breath, drifting left towards the MacBook
for i in range(14):
    bit = random.choice("01")
    colour = random.choice(["#5dc9f2", "#e8384f", "#ff8a5c", "#a8ecff"])
    tx = -random.randint(18, 52)
    ty = random.randint(-46, 40)
    delay = 3.0 + i * 0.19
    size = random.choice([11, 12, 13, 14])
    add(f'<text class="mono bit" x="34" y="{150 + random.randint(-6, 8)}" font-size="{size}" font-weight="700" '
        f'fill="{colour}" style="--tx:{tx}px;--ty:{ty}px;animation-delay:{delay:.2f}s">{bit}</text>')
add("</g>")

add("</g>")  # panel clip
add("</svg>")

with open(OUT, "w") as f:
    f.write("\n".join(parts))
print("wrote", OUT)
