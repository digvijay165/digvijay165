"""Draw the "GitHub activity" card for the profile README.

Writes activity-dark.svg and activity-light.svg into the folder given on the
command line (default: dist). Replaces the hosted stats cards, which are often
rate-limited and then show as broken images. Runs in GitHub Actions. Uses only
the Python standard library.
"""

import datetime
import json
import os
import sys
import urllib.request

# ---- Edit these -----------------------------------------------------------
USER = "digvijay165"
TOP_LANGUAGES = 6          # rows in the languages panel; the rest fold into "Other"
RECENT_REPOS = 4           # rows in the "Recently pushed" list
EXCLUDE = {"digvijay165", "priv"}                        # repos never listed
SKIP_LANGUAGES = {"Batchfile", "Dockerfile", "PLpgSQL"}  # build/config files, not code I write
# ---------------------------------------------------------------------------

THEMES = {
    "dark": {
        "bg": ("#0b1020", "#131c3a"),
        "glow": "#6366f1",
        "dots": "#ffffff",
        "border": "#1e293b",
        "tile": "#ffffff", "tile_opacity": "0.04",
        "primary": "#f8fafc",
        "secondary": "#cbd5e1",
        "muted": "#94a3b8",
        "accent": "#38bdf8",
        "track": "#1e293b",
        "rule": "#1e293b",
    },
    "light": {
        "bg": ("#f8fafc", "#eef2ff"),
        "glow": "#818cf8",
        "dots": "#0f172a",
        "border": "#e2e8f0",
        "tile": "#ffffff", "tile_opacity": "0.75",
        "primary": "#0f172a",
        "secondary": "#334155",
        "muted": "#64748b",
        "accent": "#4f46e5",
        "track": "#e0e7ff",
        "rule": "#e2e8f0",
    },
}

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"


def graphql(query, **variables):
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "User-Agent": USER},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = json.load(response)
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body["data"]


def load():
    return graphql("""
      query($login: String!) {
        user(login: $login) {
          contributionsCollection {
            totalCommitContributions
            contributionCalendar { totalContributions }
          }
          pullRequests(states: MERGED) { totalCount }
          repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100,
                       orderBy: {field: PUSHED_AT, direction: DESC}) {
            totalCount
            nodes {
              name
              pushedAt
              primaryLanguage { name }
              languages(first: 20, orderBy: {field: SIZE, direction: DESC}) {
                edges { size node { name } }
              }
            }
          }
        }
      }""", login=USER)["user"]


def top_languages(repos):
    sizes = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name not in SKIP_LANGUAGES:
                sizes[name] = sizes.get(name, 0) + edge["size"]
    total = sum(sizes.values()) or 1
    ranked = sorted(sizes.items(), key=lambda item: item[1], reverse=True)
    rows = [(name, size / total) for name, size in ranked[:TOP_LANGUAGES]]
    other = sum(size for _, size in ranked[TOP_LANGUAGES:])
    if other:
        rows.append(("Other", other / total))
    return rows


def ago(timestamp, now):
    days = (now - datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))).days
    if days < 1:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 30:
        return f"{days} days ago"
    months = days // 30
    return "1 month ago" if months == 1 else f"{months} months ago"


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def card(theme, data, now):
    t = THEMES[theme]
    repos = data["repositories"]
    langs = top_languages(repos["nodes"])
    recent = [r for r in repos["nodes"] if r["name"] not in EXCLUDE][:RECENT_REPOS]
    contributions = data["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    commits = data["contributionsCollection"]["totalCommitContributions"]
    merged = data["pullRequests"]["totalCount"]

    out = []
    add = out.append
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 410" width="1200" height="410" '
        f'role="img" aria-label="GitHub activity for {USER}: {contributions} contributions and {commits} commits '
        f'in the last year, {merged} pull requests merged, {repos["totalCount"]} public repositories. '
        f'Top languages: {esc(", ".join(f"{n} {p:.0%}" for n, p in langs))}.">')
    add(f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["bg"][0]}"/><stop offset="1" stop-color="{t["bg"][1]}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{t["glow"]}" stop-opacity="0.22"/><stop offset="1" stop-color="{t["glow"]}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.2" fill="{t["dots"]}" fill-opacity="0.05"/>
    </pattern>
    <clipPath id="card"><rect width="1200" height="410" rx="24"/></clipPath>
  </defs>
  <g clip-path="url(#card)">
    <rect width="1200" height="410" fill="url(#bg)"/>
    <rect width="1200" height="410" fill="url(#dots)"/>
    <circle cx="1080" cy="0" r="320" fill="url(#glow)"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="409" rx="24" fill="none" stroke="{t["border"]}"/>''')

    add(f'  <text x="56" y="62" font-family="{MONO}" font-size="16" fill="{t["accent"]}">~/{USER} '
        f'<tspan fill="{t["muted"]}">$ git log --stat</tspan></text>')
    add(f'  <text x="1144" y="62" text-anchor="end" font-family="{SANS}" font-size="13" fill="{t["muted"]}">'
        f'Updated {now.day} {now.strftime("%b %Y")}</text>')

    # Stat tiles
    tiles = [
        (f"{contributions:,}", "contributions", "in the last year"),
        (f"{commits:,}", "commits", "in the last year"),
        (f"{merged:,}", "pull requests", "merged"),
        (f"{repos['totalCount']:,}", "repositories", "public"),
    ]
    tile_w, gap, x0 = 162, 12, 56
    for i, (value, label, detail) in enumerate(tiles):
        x = x0 + i * (tile_w + gap)
        add(f'  <rect x="{x}" y="88" width="{tile_w}" height="100" rx="14" fill="{t["tile"]}" '
            f'fill-opacity="{t["tile_opacity"]}" stroke="{t["border"]}"/>')
        add(f'  <text x="{x + 18}" y="130" font-family="{SANS}" font-size="34" font-weight="700" '
            f'fill="{t["primary"]}">{esc(value)}</text>')
        add(f'  <text x="{x + 18}" y="154" font-family="{SANS}" font-size="14" fill="{t["secondary"]}">'
            f'{esc(label)}</text>')
        add(f'  <text x="{x + 18}" y="172" font-family="{SANS}" font-size="12" fill="{t["muted"]}">'
            f'{esc(detail)}</text>')

    # Recently pushed repositories
    left, right = 56, 740
    add(f'  <text x="{left}" y="230" font-family="{SANS}" font-size="15" font-weight="600" '
        f'fill="{t["primary"]}">Recently pushed</text>')
    y = 262
    for repo in recent:
        language = repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else ""
        add(f'  <circle cx="{left + 5}" cy="{y - 5}" r="4" fill="{t["accent"]}"/>')
        add(f'  <text x="{left + 20}" y="{y}" font-family="{SANS}" font-size="15" font-weight="600" '
            f'fill="{t["primary"]}">{esc(repo["name"])}'
            + (f'<tspan font-weight="400" fill="{t["muted"]}">  ·  {esc(language)}</tspan>' if language else "")
            + "</text>")
        add(f'  <text x="{right}" y="{y}" text-anchor="end" font-family="{SANS}" font-size="13" '
            f'fill="{t["muted"]}">{ago(repo["pushedAt"], now)}</text>')
        y += 36
        if repo is not recent[-1]:
            add(f'  <line x1="{left}" y1="{y - 18.5}" x2="{right}" y2="{y - 18.5}" stroke="{t["rule"]}"/>')

    # Top languages: share of all code in public repos, one row each
    px, pw = 800, 344
    add(f'  <text x="{px}" y="108" font-family="{SANS}" font-size="15" font-weight="600" '
        f'fill="{t["primary"]}">Top languages</text>')
    add(f'  <text x="{px + pw}" y="108" text-anchor="end" font-family="{SANS}" font-size="13" '
        f'fill="{t["muted"]}">share of code</text>')
    y, last = 142, 362
    step = (last - y) / (len(langs) - 1) if len(langs) > 1 else 0
    for name, share in langs:
        add(f'  <text x="{px}" y="{y:.1f}" font-family="{SANS}" font-size="14" fill="{t["secondary"]}">{esc(name)}</text>')
        add(f'  <text x="{px + pw}" y="{y:.1f}" text-anchor="end" font-family="{SANS}" font-size="14" '
            f'font-weight="600" fill="{t["primary"]}">{share * 100:.1f}%</text>')
        add(f'  <rect x="{px}" y="{y + 8:.1f}" width="{pw}" height="6" rx="3" fill="{t["track"]}"/>')
        add(f'  <rect x="{px}" y="{y + 8:.1f}" width="{max(6, share * pw):.1f}" height="6" rx="3" fill="{t["accent"]}"/>')
        y += step

    add("</svg>")
    return "\n".join(out) + "\n"


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else "dist"
    os.makedirs(folder, exist_ok=True)
    data = load()
    now = datetime.datetime.now(datetime.timezone.utc)
    for theme in THEMES:
        path = os.path.join(folder, f"activity-{theme}.svg")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(card(theme, data, now))
        print("wrote", path)


if __name__ == "__main__":
    main()
