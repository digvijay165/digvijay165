"""Draw the profile README's tiles: hero, buttons, focus strip, section headers,
project cards, toolbox and footer, each in a dark and a light version.

Edit the content below and run:  python .github/scripts/build_design.py
The SVGs land in assets/ and are committed. (The activity card is drawn
separately, every day, by build_stats.py.) Uses only the Python standard library.
"""

import base64
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ASSETS = os.path.join(ROOT, "assets")

# ---- Content --------------------------------------------------------------
NAME = "Digvijay Singh"
ROLE = ("Full-stack developer", " & CS student")       # second part is drawn plainer
BIO = ["I build fast, friendly web apps end to end, and",
       "lately the systems underneath them, in plain Java."]
META = [  # icon, text
    ("pin", "Kota, India"),
    ("rocket", "12 live apps"),
    ("terminal", "now: an HTTP server in Java"),
]
STATUS = "Open to internships"
EMAIL = "digvijaysingh5360@gmail.com"

CODE = [  # the editor in the hero: one list of (text, kind) per line
    [("const ", "kw"), ("digvijay", "fn"), (" = {", "p")],
    [("  role", "key"), (": ", "p"), ('"Full-stack dev"', "str"), (",", "p")],
    [("  based", "key"), (": ", "p"), ('"Kota, India"', "str"), (",", "p")],
    [("  stack", "key"), (": [", "p"), ('"React"', "str"), (", ", "p"), ('"Node"', "str"), (", ", "p"), ('"Java"', "str"), ("],", "p")],
    [("  liveApps", "key"), (": ", "p"), ("12", "num"), (",", "p")],
    [("  building", "key"), (": ", "p"), ('"HTTP server"', "str"), (",", "p")],
    [("  openTo", "key"), (": ", "p"), ('"internships"', "str"), (",", "p")],
    [("};", "p")],
]

BUTTONS = [  # name, label, icon, icon colour (dark, light), primary
    ("portfolio", "Portfolio", "globe", None, True),
    ("email", "Email", "mail", ("#7dd3fc", "#0369a1"), False),
    ("linkedin", "LinkedIn", "linkedin", ("#60a5fa", "#0a66c2"), False),
    ("leetcode", "LeetCode", "code", ("#fbbf24", "#b45309"), False),
    ("instagram", "Instagram", "instagram", ("#f9a8d4", "#be185d"), False),
]

FOCUS = [  # icon, title, text
    ("layers", "Product engineering",
     "Complete web apps, shipped and live: React front ends, Node and Express APIs, PostgreSQL."),
    ("cpu", "Systems from scratch",
     "A Redis-compatible server in plain Java: one NIO event loop, RESP pipelining, crash-safe persistence."),
    ("target", "Problem solving",
     "Data structures and algorithms in C++ and Java, and a Smart India Hackathon 2026 prototype."),
]

HEADERS = [  # slug, number, title, note
    ("work", "01", "Selected work", "live apps and systems I built"),
    ("more", "02", "More projects", "web apps, Python, C++ and DSA"),
    ("toolbox", "03", "Toolbox", "what I reach for"),
    ("activity", "04", "Activity", "redrawn every day"),
]

PROJECTS = [  # slug, image, label, title, description, tags, accent (dark, light)
    ("himvoya", "himvoya.webp", "TRAVEL", "Himvoya",
     "India-first travel planner: 106 destination guides, 30 Himalayan treks, live weather and a day-by-day trip planner.",
     ["React", "TypeScript", "Express", "SQLite"], ("#5eead4", "#0f766e")),
    ("shelfspace", "shelfspace.webp", "READING", "Shelfspace",
     "A cozy book library with a 3D page-turning reader, soft paper sounds and an admin-approved community shelf.",
     ["JavaScript", "Node.js", "PostgreSQL", "Vercel"], ("#fcd34d", "#b45309")),
    ("mini-redis", "mini-redis.svg", "SYSTEMS · OPEN SOURCE", "mini-redis",
     "A Redis-compatible server in plain Java: one NIO event loop, RESP pipelining, 39 commands and crash-safe persistence.",
     ["Java 21", "NIO", "JUnit", "Maven"], ("#fca5a5", "#dc2626")),
    ("forgeflow", "forgeflow.webp", "BUSINESS", "ForgeFlow",
     "GST billing, stock and reports for machine-parts workshops. Type a part number, press Enter, done. Works offline.",
     ["JavaScript", "Cloudflare D1", "Supabase Auth"], ("#a5b4fc", "#4f46e5")),
    ("resumeiq", "resumeiq.webp", "CAREER · AI", "ResumeIQ",
     "Resume analyzer and builder: explainable score, ATS checks, job matching, skill gaps and a learning roadmap.",
     ["React", "TypeScript", "Vite", "Cloudflare"], ("#c4b5fd", "#6d28d9")),
    ("terra-trust", "terra-trust.webp", "SMART INDIA HACKATHON 2026", "Terra Trust",
     "AI-verified land records with khasra search, a GIS map pin and an application tracker, in English and Hindi.",
     ["React", "JavaScript"], ("#86efac", "#15803d")),
]

TOOLBOX = [  # row label, [(tool, colour)]
    ("Languages", [("TypeScript", "#3178c6"), ("JavaScript", "#f7df1e"), ("Python", "#3776ab"),
                   ("Java", "#ed8b00"), ("C++", "#00599c"), ("SQL", "#94a3b8")]),
    ("Front-end", [("React", "#61dafb"), ("HTML & CSS", "#e34f26"), ("Tailwind", "#38bdf8"),
                   ("Bootstrap", "#7952b3"), ("Three.js", "#94a3b8"), ("Vite", "#a855f7")]),
    ("Back-end", [("Node.js", "#5fa04e"), ("Express", "#94a3b8"), ("Django", "#44b78b"),
                  ("Flask", "#94a3b8"), ("REST APIs", "#38bdf8")]),
    ("Data", [("PostgreSQL", "#4169e1"), ("Neon", "#00e599"), ("SQLite", "#0f80cc"),
              ("Supabase", "#3ecf8e"), ("Cloudflare D1", "#f38020"), ("IndexedDB", "#f59e0b")]),
    ("Tools", [("Git", "#f05032"), ("GitHub Actions", "#2088ff"), ("Docker", "#2496ed"),
               ("Vercel", "#94a3b8"), ("Render", "#46e3b7"), ("Maven", "#c71a36")]),
]
# ---------------------------------------------------------------------------

# Colours sit close to GitHub's own, so the tiles feel native on the page.
THEMES = {
    "dark": {
        "tile": ("#161b22", "#0d1117"), "border": "#30363d", "edge": "#ffffff", "edge_opacity": "0.08",
        "primary": "#f0f6fc", "secondary": "#c9d1d9", "muted": "#8b949e",
        "accent": "#a5b4fc", "accent2": "#67e8f9", "glow": "#6366f1", "glow2": "#0891b2",
        "chip": "#21262d", "chip_border": "#30363d", "grid": "#ffffff", "grid_opacity": "0.035",
        "good": "#3fb950", "editor": "#0d1117", "bar": "#161b22",
        "solid": "#f0f6fc", "on_solid": "#0d1117",
        "syntax": {"kw": "#ff7b72", "fn": "#d2a8ff", "key": "#79c0ff", "str": "#a5d6ff",
                   "num": "#ffa657", "p": "#c9d1d9"},
    },
    "light": {
        "tile": ("#ffffff", "#f6f8fa"), "border": "#d0d7de", "edge": "#ffffff", "edge_opacity": "0",
        "primary": "#1f2328", "secondary": "#424a53", "muted": "#656d76",
        "accent": "#4f46e5", "accent2": "#0891b2", "glow": "#818cf8", "glow2": "#22d3ee",
        "chip": "#f6f8fa", "chip_border": "#d0d7de", "grid": "#1f2328", "grid_opacity": "0.04",
        "good": "#1a7f37", "editor": "#ffffff", "bar": "#f6f8fa",
        "solid": "#1f2328", "on_solid": "#ffffff",
        "syntax": {"kw": "#cf222e", "fn": "#8250df", "key": "#0550ae", "str": "#0a3069",
                   "num": "#953800", "p": "#1f2328"},
    },
}

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Inter', 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Code', Consolas, 'Liberation Mono', Menlo, monospace"

ICONS = {  # 24x24 line icons
    "globe": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/></g>',
    "mail": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/></g>',
    "linkedin": '<path fill="{c}" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 1 1 0-4.125 2.062 2.062 0 0 1 0 4.125zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
    "code": '<g fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4.5l-4 15"/></g>',
    "instagram": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6" fill="{c}"/></g>',
    "arrow": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></g>',
    "pin": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></g>',
    "rocket": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 15c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1z"/><path d="M12 15l-3-3a22 22 0 0 1 2-4A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22 22 0 0 1-4 2z"/><path d="M9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/></g>',
    "terminal": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 17l6-5-6-5M12 19h8"/></g>',
    "layers": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/></g>',
    "cpu": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6" rx="1"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></g>',
    "target": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2" fill="{c}"/></g>',
    "lock": '<g fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></g>',
}


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def text_width(text, size, mono=False):
    """A generous estimate of rendered width; fonts differ between systems."""
    if mono:
        return len(text) * size * 0.61
    wide = sum(1 for ch in text if ch.isupper() or ch in "mwMW@")
    return (len(text) * 0.53 + wide * 0.12) * size


def wrap(text, size, width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if line and text_width(trial, size) > width:
            lines.append(line)
            line = word
        else:
            line = trial
    return lines + [line]


def icon(name, colour, x, y, size):
    return (f'<svg x="{x:.0f}" y="{y:.0f}" width="{size}" height="{size}" viewBox="0 0 24 24">'
            + ICONS[name].format(c=colour) + "</svg>")


def data_uri(path):
    mime = "image/svg+xml" if path.endswith(".svg") else "image/webp"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def svg(width, height, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" '
            f'height="{height}" role="img" aria-label="{esc(label)}">\n{body}\n</svg>\n')


def tile_background(t, width, height, rx=20, glows=(), grid=False, strength=0.22):
    """Rounded tile: soft gradient, optional fine grid and glows, hairline border."""
    out = [f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.4" y2="1">
      <stop offset="0" stop-color="{t["tile"][0]}"/><stop offset="1" stop-color="{t["tile"][1]}"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t["edge"]}" stop-opacity="0"/><stop offset="0.5" stop-color="{t["edge"]}" stop-opacity="{t["edge_opacity"]}"/><stop offset="1" stop-color="{t["edge"]}" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="{t["grid"]}" stroke-opacity="{t["grid_opacity"]}"/>
    </pattern>
    <radialGradient id="fade" cx="0.75" cy="0.35" r="0.75">
      <stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
    </radialGradient>
    <mask id="gridmask"><rect width="{width}" height="{height}" fill="url(#fade)"/></mask>
    <clipPath id="card"><rect width="{width}" height="{height}" rx="{rx}"/></clipPath>''']
    for i, (colour, *_rest) in enumerate(glows):
        out.append(f'''    <radialGradient id="glow{i}" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{colour}" stop-opacity="{strength}"/><stop offset="1" stop-color="{colour}" stop-opacity="0"/>
    </radialGradient>''')
    out.append("  </defs>")
    out.append(f'  <g clip-path="url(#card)">\n    <rect width="{width}" height="{height}" fill="url(#bg)"/>')
    if grid:
        out.append(f'    <rect width="{width}" height="{height}" fill="url(#grid)" mask="url(#gridmask)"/>')
    for i, (_colour, cx, cy, r) in enumerate(glows):
        out.append(f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#glow{i})"/>')
    out.append(f'    <rect x="{rx}" y="0" width="{width - 2 * rx}" height="1" fill="url(#edge)"/>')
    out.append("  </g>")
    out.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{rx - 0.5}" fill="none" stroke="{t["border"]}"/>')
    return "\n".join(out)


def window_dots(x, y):
    return "".join(f'<circle cx="{x + i * 18}" cy="{y}" r="5.5" fill="{c}"/>'
                   for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")))


def hero(t):
    w, h = 1200, 500
    body = [tile_background(t, w, h, glows=[(t["glow"], 930, 230, 420), (t["glow2"], 40, 540, 260)], grid=True,
                           strength=0.22 if t["editor"] == "#0d1117" else 0.14)]

    # Left column: status, name, role, bio, meta
    pill_w = 52 + text_width(STATUS.upper(), 13, mono=True) * 1.12
    body.append(f'''  <g transform="translate(64 64)">
    <rect width="{pill_w:.0f}" height="34" rx="17" fill="{t["good"]}" fill-opacity="0.1" stroke="{t["good"]}" stroke-opacity="0.4"/>
    <circle cx="21" cy="17" r="4.5" fill="{t["good"]}"/>
    <circle cx="21" cy="17" r="4.5" fill="none" stroke="{t["good"]}" stroke-width="2">
      <animate attributeName="r" values="4.5;11" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0" dur="1.8s" repeatCount="indefinite"/>
    </circle>
    <text x="36" y="22" font-family="{MONO}" font-size="13" font-weight="600" letter-spacing="1.2" fill="{t["good"]}">{esc(STATUS.upper())}</text>
  </g>
  <defs>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t["accent"]}"/><stop offset="1" stop-color="{t["accent2"]}"/>
    </linearGradient>
  </defs>
  <text x="60" y="184" font-family="{SANS}" font-size="76" font-weight="800" fill="{t["primary"]}" letter-spacing="-2.4">{esc(NAME)}</text>
  <text x="63" y="236" font-family="{SANS}" font-size="29" font-weight="700" letter-spacing="-0.4"><tspan fill="url(#ink)">{esc(ROLE[0])}</tspan><tspan fill="{t["secondary"]}" font-weight="600">{esc(ROLE[1])}</tspan></text>''')
    for i, line in enumerate(BIO):
        body.append(f'  <text x="64" y="{288 + i * 32}" font-family="{SANS}" font-size="20" fill="{t["muted"]}">{esc(line)}</text>')
    body.append(f'  <rect x="64" y="358" width="560" height="1" fill="{t["border"]}"/>')
    x = 64
    for i, (name, text) in enumerate(META):
        y = 398 + (i // 2) * 40
        x = 64 if i % 2 == 0 else 64 + 230
        if i == 2:
            x, y = 64, 438
        body.append("  " + icon(name, t["accent"], x, y - 15, 18))
        body.append(f'  <text x="{x + 28}" y="{y}" font-family="{MONO}" font-size="15" fill="{t["secondary"]}">{esc(text)}</text>')

    # Right column: a small code editor
    ex, ey, ew, eh = 676, 78, 460, 344
    body.append(f'''  <defs>
    <clipPath id="editor"><rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" rx="14"/></clipPath>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity="{0.45 if t["editor"] == "#0d1117" else 0.12}"/>
    </filter>
  </defs>
  <rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" rx="14" fill="{t["editor"]}" filter="url(#shadow)"/>
  <g clip-path="url(#editor)">
    <rect x="{ex}" y="{ey}" width="{ew}" height="42" fill="{t["bar"]}"/>
    <rect x="{ex}" y="{ey + 42}" width="{ew}" height="1" fill="{t["border"]}"/>
    {window_dots(ex + 22, ey + 21)}
    <rect x="{ex + 86}" y="{ey + 42}" width="130" height="2" fill="url(#ink)"/>
    <text x="{ex + 100}" y="{ey + 26}" font-family="{MONO}" font-size="13" fill="{t["primary"]}">digvijay.ts</text>
    <text x="{ex + ew - 20}" y="{ey + 26}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{t["muted"]}">TypeScript</text>
  </g>
  <rect x="{ex + 0.5}" y="{ey + 0.5}" width="{ew - 1}" height="{eh - 1}" rx="13.5" fill="none" stroke="{t["border"]}"/>''')
    syn = t["syntax"]
    top, lh = ey + 80, 32
    for n, tokens in enumerate(CODE):
        y = top + n * lh
        spans = "".join(f'<tspan fill="{syn[kind]}">{esc(text)}</tspan>' for text, kind in tokens)
        body.append(f'  <text x="{ex + 40}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="14" fill="{t["muted"]}" fill-opacity="0.7">{n + 1}</text>')
        body.append(f'  <text x="{ex + 58}" y="{y}" font-family="{MONO}" font-size="16" xml:space="preserve">{spans}</text>')
    last = top + (len(CODE) - 1) * lh
    cursor_x = ex + 58 + text_width("};", 16, mono=True) + 4
    body.append(f'''  <rect x="{cursor_x:.0f}" y="{last - 15}" width="9" height="19" fill="{t["accent"]}">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>''')
    label = f"{NAME}. {''.join(ROLE)}. {' '.join(BIO)} {', '.join(m for _, m in META)}. {STATUS}."
    return svg(w, h, label, "\n".join(body))


def button(t, theme, label, icon_name, icon_colours, primary):
    h, icon_size = 44, 18
    w = round(20 + icon_size + 10 + text_width(label, 15) + 22)
    if primary:
        face = f'  <rect width="{w}" height="{h}" rx="10" fill="{t["solid"]}"/>'
        text_colour = icon_colour = t["on_solid"]
    else:
        face = (f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="9.5" fill="{t["chip"]}" stroke="{t["chip_border"]}"/>')
        text_colour = t["primary"]
        icon_colour = icon_colours[0] if theme == "dark" else icon_colours[1]
    body = (face + "\n  " + icon(icon_name, icon_colour, 20, 13, icon_size)
            + f'\n  <text x="{20 + icon_size + 10}" y="28" font-family="{SANS}" font-size="15" font-weight="600" fill="{text_colour}">{esc(label)}</text>')
    return svg(w, h, label, body)


def focus(t):
    w, h, pad, gap = 1200, 252, 40, 20
    col = (w - 2 * pad - 2 * gap) / 3
    body = [tile_background(t, w, h)]
    for i, (name, title, text) in enumerate(FOCUS):
        x = pad + i * (col + gap)
        if i:
            body.append(f'  <rect x="{x - gap / 2:.0f}" y="40" width="1" height="{h - 80}" fill="{t["border"]}"/>')
        body.append(f'  <rect x="{x:.0f}" y="40" width="44" height="44" rx="11" fill="{t["accent"]}" fill-opacity="0.1" stroke="{t["accent"]}" stroke-opacity="0.35"/>')
        body.append("  " + icon(name, t["accent"], x + 11, 51, 22))
        body.append(f'  <text x="{x:.0f}" y="124" font-family="{SANS}" font-size="22" font-weight="700" fill="{t["primary"]}" letter-spacing="-0.3">{esc(title)}</text>')
        for j, line in enumerate(wrap(text, 17, col - 24)[:3]):
            body.append(f'  <text x="{x:.0f}" y="{158 + j * 26}" font-family="{SANS}" font-size="17" fill="{t["muted"]}">{esc(line)}</text>')
    label = "What I do. " + " ".join(f"{title}: {text}" for _, title, text in FOCUS)
    return svg(w, h, label, "\n".join(body))


def header(t, number, title, note):
    w, h = 1200, 100
    body = f'''  <text x="2" y="58" font-family="{MONO}" font-size="16" font-weight="600" fill="{t["accent"]}" letter-spacing="1">{esc(number)}</text>
  <text x="40" y="60" font-family="{SANS}" font-size="36" font-weight="800" fill="{t["primary"]}" letter-spacing="-0.9">{esc(title)}</text>
  <text x="1198" y="58" text-anchor="end" font-family="{MONO}" font-size="15" fill="{t["muted"]}">{esc(note)}</text>
  <rect x="0" y="82" width="1200" height="1" fill="{t["border"]}"/>
  <rect x="0" y="81" width="72" height="3" rx="1.5" fill="{t["accent"]}"/>'''
    return svg(w, h, f"{number}. {title}: {note}", body)


def project(t, theme, image, label, title, description, tags, accents):
    w, h = 560, 612
    accent = accents[0] if theme == "dark" else accents[1]
    fx, fy, fw, fh = 14, 14, 532, 330
    body = [tile_background(t, w, h, glows=[(accent, w - 40, h + 40, 240)], strength=0.12 if theme == "dark" else 0.16)]
    body.append(f'''  <defs><clipPath id="frame"><rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="12"/></clipPath></defs>
  <image x="{fx}" y="{fy}" width="{fw}" height="{fh}" preserveAspectRatio="xMidYMid slice" clip-path="url(#frame)" href="{data_uri(os.path.join(ASSETS, "projects", image))}"/>
  <rect x="{fx + 0.5}" y="{fy + 0.5}" width="{fw - 1}" height="{fh - 1}" rx="11.5" fill="none" stroke="{t["border"]}"/>
  <circle cx="34" cy="{fy + fh + 40}" r="4" fill="{accent}"/>
  <text x="46" y="{fy + fh + 45}" font-family="{MONO}" font-size="13" font-weight="600" fill="{accent}" letter-spacing="1.4">{esc(label)}</text>
  <rect x="{w - 64}" y="{fy + fh + 22}" width="36" height="36" rx="10" fill="{t["chip"]}" stroke="{t["chip_border"]}"/>
  {icon("arrow", t["primary"], w - 55, fy + fh + 31, 18)}
  <text x="28" y="{fy + fh + 92}" font-family="{SANS}" font-size="32" font-weight="800" fill="{t["primary"]}" letter-spacing="-0.8">{esc(title)}</text>''')
    y = fy + fh + 126
    for line in wrap(description, 18, w - 60)[:3]:
        body.append(f'  <text x="30" y="{y}" font-family="{SANS}" font-size="18" fill="{t["muted"]}">{esc(line)}</text>')
        y += 27
    x, ty = 30, h - 52
    for tag in tags:
        tw = text_width(tag, 13, mono=True) + 22
        body.append(f'  <rect x="{x}" y="{ty}" width="{tw:.0f}" height="28" rx="7" fill="{t["chip"]}" stroke="{t["chip_border"]}"/>'
                    f'\n  <text x="{x + 11}" y="{ty + 18.5}" font-family="{MONO}" font-size="13" fill="{t["secondary"]}">{esc(tag)}</text>')
        x += tw + 8
    return svg(w, h, f"{title}: {description} Built with {', '.join(tags)}.", "\n".join(body))


def toolbox(t):
    w, row_h, top = 1200, 62, 40
    h = top * 2 + row_h * len(TOOLBOX) - 22
    body = [tile_background(t, w, h)]
    for r, (group, tools) in enumerate(TOOLBOX):
        y = top + r * row_h
        if r:
            body.append(f'  <rect x="40" y="{y - 11}" width="{w - 80}" height="1" fill="{t["border"]}" fill-opacity="0.6"/>')
        body.append(f'  <text x="44" y="{y + 25}" font-family="{MONO}" font-size="13" font-weight="600" fill="{t["muted"]}" letter-spacing="1.8">{esc(group.upper())}</text>')
        x = 220
        for tool, colour in tools:
            cw = text_width(tool, 16) + 44
            body.append(f'  <rect x="{x}" y="{y}" width="{cw:.0f}" height="40" rx="10" fill="{t["chip"]}" stroke="{t["chip_border"]}"/>'
                        f'\n  <rect x="{x + 15}" y="{y + 16}" width="8" height="8" rx="2" fill="{colour}"/>'
                        f'\n  <text x="{x + 32}" y="{y + 26}" font-family="{SANS}" font-size="16" font-weight="600" fill="{t["primary"]}">{esc(tool)}</text>')
            x += cw + 10
    label = "Toolbox. " + " ".join(f"{g}: {', '.join(n for n, _ in tools)}." for g, tools in TOOLBOX)
    return svg(w, h, label, "\n".join(body))


def footer(t):
    w, h = 1200, 300
    body = [tile_background(t, w, h, glows=[(t["glow"], 600, 330, 460)], grid=True)]
    pill_w = text_width(EMAIL, 18, mono=True) + 72
    px = 600 - pill_w / 2
    body.append(f'''  <text x="600" y="104" text-anchor="middle" font-family="{SANS}" font-size="44" font-weight="800" fill="{t["primary"]}" letter-spacing="-1.3">Let's build something together.</text>
  <text x="600" y="148" text-anchor="middle" font-family="{SANS}" font-size="20" fill="{t["muted"]}">Open to internships and collaborations. The fastest way to reach me:</text>
  <rect x="{px:.0f}" y="184" width="{pill_w:.0f}" height="54" rx="12" fill="{t["solid"]}"/>
  {icon("mail", t["on_solid"], px + 24, 200, 22)}
  <text x="{px + 58:.0f}" y="217" font-family="{MONO}" font-size="18" font-weight="600" fill="{t["on_solid"]}">{esc(EMAIL)}</text>''')
    return svg(w, h, f"Let's build something together. Open to internships and collaborations. Email {EMAIL}", "\n".join(body))


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def main():
    for theme, t in THEMES.items():
        write(os.path.join(ASSETS, f"hero-{theme}.svg"), hero(t))
        write(os.path.join(ASSETS, f"focus-{theme}.svg"), focus(t))
        write(os.path.join(ASSETS, f"toolbox-{theme}.svg"), toolbox(t))
        write(os.path.join(ASSETS, f"footer-{theme}.svg"), footer(t))
        for name, label, icon_name, colours, primary in BUTTONS:
            write(os.path.join(ASSETS, "buttons", f"{name}-{theme}.svg"), button(t, theme, label, icon_name, colours, primary))
        for slug, number, title, note in HEADERS:
            write(os.path.join(ASSETS, "headers", f"{slug}-{theme}.svg"), header(t, number, title, note))
        for slug, image, label, title, description, tags, accents in PROJECTS:
            write(os.path.join(ASSETS, "cards", f"{slug}-{theme}.svg"),
                  project(t, theme, image, label, title, description, tags, accents))
    print("assets written")


if __name__ == "__main__":
    main()
