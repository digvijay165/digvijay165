"""Draw the profile README's tiles: hero, buttons, section headers, project
cards, toolbox and footer, each in a dark and a light version.

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
ROLE = "Full-stack developer · CS student · Kota, India"
BIO = ["I build fast, friendly web apps, and lately the tools",
       "underneath them, starting with Redis in plain Java."]
NOW = "now: writing an HTTP server from scratch in Java"
STATUS = "Open to internships"
EMAIL = "digvijaysingh5360@gmail.com"

BUTTONS = [  # name, label, icon, icon colour (dark, light), filled
    ("portfolio", "Portfolio", "globe", ("#ffffff", "#ffffff"), True),
    ("email", "Email", "mail", ("#38bdf8", "#0284c7"), False),
    ("linkedin", "LinkedIn", "linkedin", ("#3b9be8", "#0a66c2"), False),
    ("leetcode", "LeetCode", "code", ("#ffa116", "#d97706"), False),
    ("instagram", "Instagram", "instagram", ("#f472b6", "#db2777"), False),
]

HEADERS = [  # slug, number, title, note
    ("work", "01", "Selected work", "live apps and systems I built"),
    ("more", "02", "Everything else", "web apps, Python, C++ and DSA"),
    ("toolbox", "03", "Toolbox", "what I reach for"),
    ("activity", "04", "Activity", "redrawn every day"),
]

PROJECTS = [  # slug, image, label, title, description, chips, accent (dark, light)
    ("himvoya", "himvoya.webp", "TRAVEL · LIVE", "Himvoya",
     "India-first travel planner: 106 destination guides, 30 Himalayan treks, live weather and a day-by-day trip planner.",
     ["React", "TypeScript", "Express", "SQLite"], ("#2dd4bf", "#0f766e")),
    ("shelfspace", "shelfspace.webp", "READING · LIVE", "Shelfspace",
     "A cozy book library with a 3D page-turning reader, soft paper sounds and an admin-approved community shelf.",
     ["JavaScript", "Node.js", "PostgreSQL", "Vercel"], ("#fbbf24", "#b45309")),
    ("mini-redis", "mini-redis.svg", "SYSTEMS · OPEN SOURCE", "mini-redis",
     "A Redis-compatible server in plain Java: one NIO event loop, RESP pipelining, 39 commands and crash-safe persistence.",
     ["Java 21", "NIO", "JUnit", "Maven"], ("#f87171", "#dc2626")),
    ("forgeflow", "forgeflow.webp", "BUSINESS · LIVE", "ForgeFlow",
     "GST billing, stock and reports for machine-parts workshops. Type a part number, press Enter, done. Works offline.",
     ["JavaScript", "Cloudflare D1", "Supabase Auth"], ("#a5b4fc", "#4f46e5")),
    ("little-lantern-cafe", "little-lantern-cafe.webp", "FOOD · LIVE", "Little Lantern Café",
     "Café site with menu, map and order-ahead pickup slots, plus a live staff dashboard for orders and sales.",
     ["React", "Node.js", "PostgreSQL", "Docker"], ("#fb7185", "#e11d48")),
    ("terra-trust", "terra-trust.webp", "SMART INDIA HACKATHON 2026", "Terra Trust",
     "AI-verified land records with khasra search, a GIS map pin, an application tracker, in English and Hindi.",
     ["React", "JavaScript"], ("#4ade80", "#15803d")),
]

TOOLBOX = [  # row label, [(tool, dot colour)]
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

THEMES = {
    "dark": {
        "tile": ("#0f172a", "#0b1120"), "border": "#1e293b", "dots": "#ffffff", "dots_opacity": "0.05",
        "primary": "#f8fafc", "secondary": "#cbd5e1", "muted": "#94a3b8",
        "accent": "#38bdf8", "accent2": "#a78bfa", "glow1": "#6366f1", "glow2": "#0ea5e9",
        "chip": "#1e293b", "chip_border": "#334155",
        "good": "#4ade80", "good_bg": "#22c55e",
    },
    "light": {
        "tile": ("#ffffff", "#f8fafc"), "border": "#e2e8f0", "dots": "#0f172a", "dots_opacity": "0.045",
        "primary": "#0f172a", "secondary": "#334155", "muted": "#64748b",
        "accent": "#4f46e5", "accent2": "#0284c7", "glow1": "#818cf8", "glow2": "#38bdf8",
        "chip": "#f1f5f9", "chip_border": "#e2e8f0",
        "good": "#15803d", "good_bg": "#22c55e",
    },
}

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"

ICONS = {  # 24x24 line icons; "fill" icons are drawn solid
    "globe": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/></g>',
    "mail": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/></g>',
    "linkedin": '<path fill="{c}" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 1 1 0-4.125 2.062 2.062 0 0 1 0 4.125zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
    "code": '<g fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4.5l-4 15"/></g>',
    "instagram": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6" fill="{c}"/></g>',
    "arrow": '<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></g>',
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
    return (f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 24 24">'
            + ICONS[name].format(c=colour) + "</svg>")


def data_uri(path):
    mime = "image/svg+xml" if path.endswith(".svg") else "image/webp"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def svg(width, height, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" '
            f'height="{height}" role="img" aria-label="{esc(label)}">\n{body}\n</svg>\n')


def tile_background(t, width, height, rx=28, glows=()):
    """Rounded card with a soft gradient, a dot grid and optional glows."""
    out = [f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["tile"][0]}"/><stop offset="1" stop-color="{t["tile"][1]}"/>
    </linearGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.2" fill="{t["dots"]}" fill-opacity="{t["dots_opacity"]}"/>
    </pattern>
    <clipPath id="card"><rect width="{width}" height="{height}" rx="{rx}"/></clipPath>''']
    for i, (colour, *_rest) in enumerate(glows):
        out.append(f'''    <radialGradient id="glow{i}" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{colour}" stop-opacity="0.28"/><stop offset="1" stop-color="{colour}" stop-opacity="0"/>
    </radialGradient>''')
    out.append("  </defs>")
    out.append(f'  <g clip-path="url(#card)">\n    <rect width="{width}" height="{height}" fill="url(#bg)"/>'
               f'\n    <rect width="{width}" height="{height}" fill="url(#dots)"/>')
    for i, (_colour, cx, cy, r) in enumerate(glows):
        out.append(f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#glow{i})"/>')
    out.append("  </g>")
    out.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="{rx}" fill="none" stroke="{t["border"]}"/>')
    return "\n".join(out)


def hero(t):
    w, h = 1200, 480
    character = data_uri(os.path.join(ROOT, "character.svg"))
    pill_w = 56 + text_width(STATUS, 17)
    body = [tile_background(t, w, h, glows=[(t["glow1"], 1000, 120, 380), (t["glow2"], 60, 520, 320)])]
    body.append(f'''  <g transform="translate(64 64)">
    <rect width="{pill_w:.0f}" height="40" rx="20" fill="{t["good_bg"]}" fill-opacity="0.12" stroke="{t["good_bg"]}" stroke-opacity="0.45"/>
    <circle cx="24" cy="20" r="6" fill="{t["good_bg"]}"/>
    <circle cx="24" cy="20" r="6" fill="none" stroke="{t["good_bg"]}" stroke-width="2">
      <animate attributeName="r" values="6;14" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0" dur="1.8s" repeatCount="indefinite"/>
    </circle>
    <text x="42" y="26" font-family="{SANS}" font-size="17" font-weight="600" fill="{t["good"]}">{esc(STATUS)}</text>
  </g>''')
    body.append(f'''  <defs>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t["accent"]}"/><stop offset="1" stop-color="{t["accent2"]}"/>
    </linearGradient>
  </defs>
  <text x="60" y="200" font-family="{SANS}" font-size="84" font-weight="800" fill="{t["primary"]}" letter-spacing="-2.5">{esc(NAME)}</text>
  <rect x="66" y="224" width="120" height="6" rx="3" fill="url(#ink)"/>
  <text x="64" y="280" font-family="{SANS}" font-size="27" font-weight="600" fill="{t["secondary"]}">{esc(ROLE)}</text>''')
    for i, line in enumerate(BIO):
        body.append(f'  <text x="64" y="{330 + i * 34}" font-family="{SANS}" font-size="22" fill="{t["muted"]}">{esc(line)}</text>')
    body.append(f'''  <text x="64" y="424" font-family="{MONO}" font-size="17" fill="{t["accent"]}">▸ <tspan fill="{t["secondary"]}">{esc(NOW)}</tspan><tspan fill="{t["accent"]}">▍<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></tspan></text>
  <circle cx="1000" cy="250" r="170" fill="{t["accent"]}" fill-opacity="0.06" stroke="{t["accent"]}" stroke-opacity="0.18"/>
  <circle cx="1000" cy="250" r="214" fill="none" stroke="{t["accent2"]}" stroke-opacity="0.16" stroke-dasharray="3 8"/>
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="6s" repeatCount="indefinite"/>
    <image x="840" y="40" width="320" height="400" href="{character}"/>
  </g>''')
    label = f"{NAME}. {ROLE}. {' '.join(BIO)} {STATUS}."
    return svg(w, h, label, "\n".join(body))


def button(t, theme, label, icon_name, icon_colours, filled):
    h, icon_size = 48, 20
    w = round(24 + icon_size + 10 + text_width(label, 16) + 24)
    colour = icon_colours[0] if theme == "dark" else icon_colours[1]
    if filled:
        face = f'''  <defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{t["accent2"] if theme == "light" else "#0ea5e9"}"/><stop offset="1" stop-color="{t["accent"] if theme == "light" else "#6366f1"}"/>
  </linearGradient></defs>
  <rect width="{w}" height="{h}" rx="24" fill="url(#b)"/>'''
        text_colour = "#ffffff"
    else:
        face = f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="23.5" fill="{t["tile"][0]}" stroke="{t["chip_border"]}"/>'
        text_colour = t["primary"]
    body = (face + "\n  " + icon(icon_name, colour, 24, 14, icon_size)
            + f'\n  <text x="{24 + icon_size + 10}" y="30" font-family="{SANS}" font-size="16" font-weight="600" fill="{text_colour}">{esc(label)}</text>')
    return svg(w, h, label, body)


def header(t, number, title, note):
    w, h = 1200, 96
    body = f'''  <defs><linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{t["accent"]}" stop-opacity="0.9"/><stop offset="0.35" stop-color="{t["accent2"]}" stop-opacity="0.45"/><stop offset="1" stop-color="{t["border"]}" stop-opacity="0"/>
  </linearGradient></defs>
  <text x="2" y="62" font-family="{MONO}" font-size="20" font-weight="600" fill="{t["accent"]}">{esc(number)}</text>
  <text x="44" y="64" font-family="{SANS}" font-size="40" font-weight="800" fill="{t["primary"]}" letter-spacing="-1">{esc(title)}</text>
  <text x="1198" y="62" text-anchor="end" font-family="{MONO}" font-size="16" fill="{t["muted"]}">{esc(note)}</text>
  <rect x="2" y="84" width="1196" height="2" rx="1" fill="url(#rule)"/>'''
    return svg(w, h, f"{number}. {title}: {note}", body)


def project(t, theme, image, label, title, description, chips, accents):
    w, h = 560, 640
    accent = accents[0] if theme == "dark" else accents[1]
    shot_w, shot_h, pad = 528, 330, 16
    body = [tile_background(t, w, h, glows=[(accent, w, h, 300)])]
    body.append(f'''  <defs><clipPath id="shot"><rect x="{pad}" y="{pad}" width="{shot_w}" height="{shot_h}" rx="18"/></clipPath></defs>
  <image x="{pad}" y="{pad}" width="{shot_w}" height="{shot_h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#shot)" href="{data_uri(os.path.join(ASSETS, "projects", image))}"/>
  <rect x="{pad + 0.5}" y="{pad + 0.5}" width="{shot_w - 1}" height="{shot_h - 1}" rx="17.5" fill="none" stroke="{t["border"]}"/>
  <text x="32" y="{pad + shot_h + 46}" font-family="{MONO}" font-size="15" font-weight="600" fill="{accent}" letter-spacing="1.5">{esc(label)}</text>
  <circle cx="{w - 50}" cy="{pad + shot_h + 41}" r="20" fill="{accent}" fill-opacity="0.14" stroke="{accent}" stroke-opacity="0.5"/>
  {icon("arrow", accent, w - 61, pad + shot_h + 30, 22)}
  <text x="30" y="{pad + shot_h + 94}" font-family="{SANS}" font-size="36" font-weight="800" fill="{t["primary"]}" letter-spacing="-0.8">{esc(title)}</text>''')
    y = pad + shot_h + 130
    for line in wrap(description, 19, w - 64)[:3]:
        body.append(f'  <text x="32" y="{y}" font-family="{SANS}" font-size="19" fill="{t["secondary"]}">{esc(line)}</text>')
        y += 28
    x, cy = 32, h - 56
    for chip in chips:
        cw = text_width(chip, 15) + 28
        body.append(f'  <rect x="{x}" y="{cy}" width="{cw:.0f}" height="32" rx="16" fill="{t["chip"]}" stroke="{t["chip_border"]}"/>'
                    f'\n  <text x="{x + 14}" y="{cy + 21}" font-family="{SANS}" font-size="15" font-weight="600" fill="{t["secondary"]}">{esc(chip)}</text>')
        x += cw + 8
    return svg(w, h, f"{title}: {description} Built with {', '.join(chips)}.", "\n".join(body))


def toolbox(t):
    w, row_h, top = 1200, 64, 44
    h = top * 2 + row_h * len(TOOLBOX) - 20
    body = [tile_background(t, w, h, glows=[(t["glow1"], 1200, 0, 300)])]
    for r, (group, tools) in enumerate(TOOLBOX):
        y = top + r * row_h
        body.append(f'  <text x="56" y="{y + 27}" font-family="{MONO}" font-size="14" font-weight="600" fill="{t["muted"]}" letter-spacing="2">{esc(group.upper())}</text>')
        x = 250
        for tool, dot in tools:
            cw = text_width(tool, 17) + 52
            body.append(f'  <rect x="{x}" y="{y}" width="{cw:.0f}" height="42" rx="21" fill="{t["chip"]}" stroke="{t["chip_border"]}"/>'
                        f'\n  <circle cx="{x + 22}" cy="{y + 21}" r="5" fill="{dot}"/>'
                        f'\n  <text x="{x + 36}" y="{y + 27}" font-family="{SANS}" font-size="17" font-weight="600" fill="{t["primary"]}">{esc(tool)}</text>')
            x += cw + 10
    label = "Toolbox. " + " ".join(f"{g}: {', '.join(n for n, _ in tools)}." for g, tools in TOOLBOX)
    return svg(w, h, label, "\n".join(body))


def footer(t):
    w, h = 1200, 300
    body = [tile_background(t, w, h, glows=[(t["glow1"], 300, 0, 360), (t["glow2"], 900, 300, 360)])]
    pill_w = text_width(EMAIL, 19, mono=True) + 64
    body.append(f'''  <text x="600" y="110" text-anchor="middle" font-family="{SANS}" font-size="46" font-weight="800" fill="{t["primary"]}" letter-spacing="-1.2">Let's build something together.</text>
  <text x="600" y="156" text-anchor="middle" font-family="{SANS}" font-size="21" fill="{t["secondary"]}">Open to internships and collaborations. Say hi:</text>
  <rect x="{600 - pill_w / 2:.0f}" y="190" width="{pill_w:.0f}" height="54" rx="27" fill="{t["accent"]}" fill-opacity="0.1" stroke="{t["accent"]}" stroke-opacity="0.5"/>
  {icon("mail", t["accent"], 600 - pill_w / 2 + 24, 205, 24)}
  <text x="{600 - pill_w / 2 + 58:.0f}" y="224" font-family="{MONO}" font-size="19" font-weight="600" fill="{t["primary"]}">{esc(EMAIL)}</text>''')
    return svg(w, h, f"Let's build something together. Open to internships and collaborations. Email {EMAIL}", "\n".join(body))


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def main():
    for theme, t in THEMES.items():
        write(os.path.join(ASSETS, f"hero-{theme}.svg"), hero(t))
        write(os.path.join(ASSETS, f"toolbox-{theme}.svg"), toolbox(t))
        write(os.path.join(ASSETS, f"footer-{theme}.svg"), footer(t))
        for name, label, icon_name, colours, filled in BUTTONS:
            write(os.path.join(ASSETS, "buttons", f"{name}-{theme}.svg"), button(t, theme, label, icon_name, colours, filled))
        for slug, number, title, note in HEADERS:
            write(os.path.join(ASSETS, "headers", f"{slug}-{theme}.svg"), header(t, number, title, note))
        for slug, image, label, title, description, chips, accents in PROJECTS:
            write(os.path.join(ASSETS, "cards", f"{slug}-{theme}.svg"),
                  project(t, theme, image, label, title, description, chips, accents))
    print("assets written")


if __name__ == "__main__":
    main()
