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
LEETCODE_USER = "DIGVIJAY5360"
TOP_LANGUAGES = 6          # rows in the languages panel; the rest fold into "Other"
RECENT_REPOS = 4           # rows in the "Recently pushed" list
EXCLUDE = {"digvijay165", "priv"}                        # repos never listed
SKIP_LANGUAGES = {"Batchfile", "Dockerfile", "PLpgSQL"}  # build/config files, not code I write
# ---------------------------------------------------------------------------

# Colours match the other tiles drawn by build_design.py.
THEMES = {
    "dark": {
        "bg": ("#161b22", "#0d1117"),
        "glow": "#6366f1",
        "dots": "#ffffff",
        "border": "#30363d",
        "tile": "#21262d", "tile_opacity": "0.6",
        "primary": "#f0f6fc",
        "secondary": "#c9d1d9",
        "muted": "#8b949e",
        "accent": "#a5b4fc",
        "track": "#21262d",
        "rule": "#21262d",
    },
    "light": {
        "bg": ("#ffffff", "#f6f8fa"),
        "glow": "#818cf8",
        "dots": "#1f2328",
        "border": "#d0d7de",
        "tile": "#f6f8fa", "tile_opacity": "1",
        "primary": "#1f2328",
        "secondary": "#424a53",
        "muted": "#656d76",
        "accent": "#4f46e5",
        "track": "#eaeef2",
        "rule": "#eaeef2",
    },
}

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Inter', 'Helvetica Neue', Arial, sans-serif"
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


def leetcode():
    """Solved counts by difficulty, e.g. {"All": 57, "Easy": 14, ...}.

    LeetCode sometimes blocks CI runners, so fall back to the counts the last
    successful run saved on the output branch. None if neither is available.
    """
    try:
        request = urllib.request.Request(
            "https://leetcode.com/graphql",
            data=json.dumps({
                "query": "query($u: String!) { matchedUser(username: $u) "
                         "{ submitStats { acSubmissionNum { difficulty count } } } }",
                "variables": {"u": LEETCODE_USER},
            }).encode(),
            headers={"Content-Type": "application/json", "Referer": "https://leetcode.com",
                     "User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            solved = json.load(response)["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
        return {row["difficulty"]: row["count"] for row in solved}
    except Exception as error:
        print("LeetCode unavailable, using the last saved counts:", error)
    try:
        url = f"https://raw.githubusercontent.com/{USER}/{USER}/output/leetcode.json"
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.load(response)
    except Exception as error:
        print("No saved LeetCode counts either:", error)
        return None


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


def card(theme, data, solved, now):
    t = THEMES[theme]
    repos = data["repositories"]
    langs = top_languages(repos["nodes"])
    recent = [r for r in repos["nodes"] if r["name"] not in EXCLUDE][:RECENT_REPOS]
    contributions = data["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    commits = data["contributionsCollection"]["totalCommitContributions"]
    merged = data["pullRequests"]["totalCount"]
    if solved:
        last_tile = (f"{solved['All']:,}", "LeetCode solved",
                     f"{solved['Easy']}E · {solved['Medium']}M · {solved['Hard']}H")
        last_label = f"{solved['All']} LeetCode problems solved"
    else:
        last_tile = (f"{repos['totalCount']:,}", "repositories", "public")
        last_label = f"{repos['totalCount']} public repositories"

    out = []
    add = out.append
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 410" width="1200" height="410" '
        f'role="img" aria-label="GitHub activity for {USER}: {contributions} contributions and {commits} commits '
        f'in the last year, {merged} pull requests merged, {last_label}. '
        f'Top languages: {esc(", ".join(f"{n} {p:.0%}" for n, p in langs))}.">')
    add(f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["bg"][0]}"/><stop offset="1" stop-color="{t["bg"][1]}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{t["glow"]}" stop-opacity="0.16"/><stop offset="1" stop-color="{t["glow"]}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="card"><rect width="1200" height="410" rx="20"/></clipPath>
  </defs>
  <g clip-path="url(#card)">
    <rect width="1200" height="410" fill="url(#bg)"/>
    <circle cx="1080" cy="0" r="320" fill="url(#glow)"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="409" rx="19.5" fill="none" stroke="{t["border"]}"/>''')

    add(f'  <text x="56" y="62" font-family="{MONO}" font-size="16" fill="{t["accent"]}">~/{USER} '
        f'<tspan fill="{t["muted"]}">$ git log --stat</tspan></text>')
    add(f'  <text x="1144" y="62" text-anchor="end" font-family="{SANS}" font-size="13" fill="{t["muted"]}">'
        f'Updated {now.day} {now.strftime("%b %Y")}</text>')

    # Stat tiles
    tiles = [
        (f"{contributions:,}", "contributions", "in the last year"),
        (f"{commits:,}", "commits", "in the last year"),
        (f"{merged:,}", "pull requests", "merged"),
        last_tile,
    ]
    tile_w, gap, x0 = 162, 12, 56
    for i, (value, label, detail) in enumerate(tiles):
        x = x0 + i * (tile_w + gap)
        add(f'  <rect x="{x}" y="88" width="{tile_w}" height="100" rx="12" fill="{t["tile"]}" '
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
    solved = leetcode()
    now = datetime.datetime.now(datetime.timezone.utc)
    for theme in THEMES:
        path = os.path.join(folder, f"activity-{theme}.svg")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(card(theme, data, solved, now))
        print("wrote", path)
    if solved:
        with open(os.path.join(folder, "leetcode.json"), "w", encoding="utf-8") as f:
            json.dump(solved, f)


if __name__ == "__main__":
    main()
