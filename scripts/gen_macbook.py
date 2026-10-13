"""Generate assets/macbook.svg: a MacBook whose 'About Me' window types out my name and details.

Usage: python3 scripts/gen_macbook.py assets/macbook.svg
"""
import sys

OUT = sys.argv[1]

W, H = 590, 356
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Menlo, Consolas, 'Courier New', monospace"

NAME = "Ahmet Ege Baykoz"
SUBTITLE = "BSc (Hons) Computer Science with Cyber Security"
ROWS = [
    ("University", "University of York"),
    ("Year", "Second year · Class of 2029"),
    ("Learning", "Networking, Linux &amp; Wireshark"),
    ("Goal", "Application &amp; cloud security"),
    ("Status", "Open to a 2027–28 placement"),
]
LINK = "e26180.github.io"
DOCK = [  # background, glyph, glyph colour
    ("#111418", "&gt;_", "#3ddc84"),
    ("#306998", "Py", "#ffd43b"),
    ("#e76f00", "J", "#ffffff"),
    ("#1679a7", "◢", "#ffffff"),
    ("#c51a4a", "π", "#ffffff"),
    ("#5dc9f2", "✎", "#0b1120"),
]

parts = []
add = parts.append

css = f"""
.sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
.ch{{fill-opacity:0;animation:show .01s linear forwards}}
@keyframes show{{to{{fill-opacity:1}}}}
.row{{opacity:0;animation:rowin .5s ease-out forwards}}
@keyframes rowin{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}
.blob{{animation:drift 12s ease-in-out infinite alternate}}
.blob2{{animation:drift 15s ease-in-out infinite alternate-reverse}}
@keyframes drift{{from{{transform:translate(0,0)}}to{{transform:translate(40px,-14px)}}}}
.dot{{animation:pulse 2s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.ch{{fill-opacity:1}}.row{{opacity:1}}}}
"""

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
    f'aria-label="MacBook screen showing {NAME}, {SUBTITLE} at the University of York">')
add(f"<style>{css}</style>")

add("<defs>")
add('<linearGradient id="wall" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#081028"/>'
    '<stop offset=".55" stop-color="#0d2650"/><stop offset="1" stop-color="#123a6b"/></linearGradient>')
add('<linearGradient id="icon" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5dc9f2"/>'
    '<stop offset="1" stop-color="#2a5fd6"/></linearGradient>')
add('<linearGradient id="base" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a4f59"/>'
    '<stop offset="1" stop-color="#1c1f24"/></linearGradient>')
add('<filter id="blur30" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>')
add('<filter id="blur3" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.5"/></filter>')
add('<clipPath id="screen"><rect x="72" y="36" width="446" height="276" rx="6"/></clipPath>')
add("</defs>")

# lid, bezel and wallpaper
add('<ellipse cx="295" cy="345" rx="260" ry="6" fill="#000" opacity=".45" filter="url(#blur3)"/>')
add('<rect x="60" y="24" width="470" height="300" rx="16" fill="#15171c" stroke="#3b404c" stroke-width="1.5"/>')
add('<rect x="72" y="36" width="446" height="276" rx="6" fill="url(#wall)"/>')
add('<g clip-path="url(#screen)">')
add('<ellipse class="blob" cx="150" cy="280" rx="170" ry="60" fill="#5dc9f2" opacity=".35" filter="url(#blur30)"/>')
add('<ellipse class="blob2" cx="470" cy="90" rx="130" ry="55" fill="#e8384f" opacity=".28" filter="url(#blur30)"/>')
add('<ellipse class="blob" cx="420" cy="300" rx="120" ry="40" fill="#7b5cff" opacity=".25" filter="url(#blur30)"/>')

# menu bar and notch
add('<rect x="72" y="36" width="446" height="13" fill="#000" opacity=".35"/>')
add('<text class="sans" x="82" y="45.5" font-size="8" fill="#fff"><tspan font-weight="700">◆ ahmet</tspan>'
    '<tspan dx="10">File</tspan><tspan dx="9">Edit</tspan><tspan dx="9">View</tspan><tspan dx="9">Security</tspan></text>')
add('<text class="sans" x="508" y="45.5" font-size="8" fill="#fff" text-anchor="end">York, UK   ◔ 09:41</text>')
add('<rect x="277" y="36" width="36" height="9" rx="3" fill="#000"/>')

# "About Me" window
add('<rect x="108" y="60" width="374" height="218" rx="10" fill="#1b2030" fill-opacity=".97" stroke="#3a4462"/>')
for i, c in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    add(f'<circle cx="{122 + i * 13}" cy="73" r="4.2" fill="{c}"/>')
add('<rect x="273" y="78" width="44" height="44" rx="10" fill="url(#icon)"/>')
add('<path d="M295,86 L307,91 V100 C307,108 302,113 295,116 C288,113 283,108 283,100 V91 Z" fill="none" '
    'stroke="#fff" stroke-width="2" stroke-linejoin="round"/>')
add('<path d="M289.5,100.5 L293.5,104.5 L301,96.5" fill="none" stroke="#fff" stroke-width="2.2" '
    'stroke-linecap="round" stroke-linejoin="round"/>')

# name, typed letter by letter
t0, step = 0.5, 0.09
spans = "".join(
    f'<tspan class="ch" style="animation-delay:{t0 + i * step:.2f}s">{c if c != " " else "&#160;"}</tspan>'
    for i, c in enumerate(NAME)
)
add(f'<text class="sans" x="295" y="146" font-size="19" font-weight="700" fill="#ffffff" text-anchor="middle">{spans}</text>')
t_name = t0 + len(NAME) * step

add(f'<g class="row" style="animation-delay:{t_name + .1:.2f}s"><text class="sans" x="295" y="163" font-size="10.5" '
    f'fill="#8f9bbb" text-anchor="middle">{SUBTITLE}</text></g>')
for i, (label, value) in enumerate(ROWS):
    y = 185 + i * 15
    delay = t_name + 0.3 + i * 0.18
    status = label == "Status"
    dot = f'<circle class="dot" cx="278" cy="{y - 3.5}" r="2.6" fill="#3ddc84"/>' if status else ""
    add(f'<g class="row" style="animation-delay:{delay:.2f}s">'
        f'<text class="sans" x="268" y="{y}" font-size="10" fill="#7f8aa6" text-anchor="end">{label}</text>{dot}'
        f'<text class="sans" x="{285 if status else 276}" y="{y}" font-size="10" '
        f'fill="{"#5dc9f2" if status else "#e6e9f2"}">{value}</text></g>')
btn_delay = t_name + 0.3 + len(ROWS) * 0.18
add(f'<g class="row" style="animation-delay:{btn_delay:.2f}s">'
    f'<rect x="243" y="257" width="104" height="15" rx="4" fill="#2b3350" stroke="#46527c"/>'
    f'<text class="sans" x="295" y="267.5" font-size="9" fill="#e6e9f2" text-anchor="middle">{LINK}</text></g>')

# dock
add('<rect x="221" y="284" width="148" height="24" rx="7" fill="#ffffff" fill-opacity=".13" stroke="#ffffff" stroke-opacity=".2"/>')
for i, (bg, glyph, fg) in enumerate(DOCK):
    x = 228 + i * 23
    add(f'<rect x="{x}" y="287" width="18" height="18" rx="4.5" fill="{bg}"/>')
    add(f'<text class="mono" x="{x + 9}" y="299.5" font-size="8.5" font-weight="700" fill="{fg}" text-anchor="middle">{glyph}</text>')
add("</g>")

# base
add('<path d="M28,324 H562 V330 Q562,338 549,338 H41 Q28,338 28,330 Z" fill="url(#base)"/>')
add('<rect x="264" y="324" width="62" height="4" rx="2" fill="#121418"/>')
add("</svg>")

with open(OUT, "w") as f:
    f.write("\n".join(parts))
print("wrote", OUT)
