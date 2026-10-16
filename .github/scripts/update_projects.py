"""Refresh the "Latest projects" section of the profile README.

Lists public, non-fork repositories that the README doesn't already feature as
cards, newest first. Only the text
between the PROJECTS markers is rewritten; the rest of the README is untouched.
Runs in GitHub Actions. Uses only the Python standard library.
"""

import datetime
import json
import os
import urllib.parse
import urllib.request

# ---- Edit these -----------------------------------------------------------
USER = "digvijay165"
EXCLUDE = {"digvijay165", "priv"}  # repos never shown in the section
MAX_PROJECTS = 0                   # 0 = show all
SKIP_FEATURED = True               # skip repos already linked elsewhere in the README
# A repo can also be hidden by giving it the topic "hide-from-profile".
# ---------------------------------------------------------------------------

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
README = os.path.join(ROOT, "README.md")
START = "<!-- PROJECTS:START -->"
END = "<!-- PROJECTS:END -->"
INSERT_BEFORE = "## 🎓 What I'm learning"

# language -> (badge colour, simple-icons logo, logo colour)
LANGUAGE_BADGES = {
    "JavaScript": ("F7DF1E", "javascript", "111"),
    "TypeScript": ("3178C6", "typescript", "white"),
    "HTML": ("E34F26", "html5", "white"),
    "CSS": ("1572B6", "css3", "white"),
    "Python": ("3776AB", "python", "white"),
    "C++": ("00599C", "cplusplus", "white"),
    "C": ("A8B9CC", "c", "111"),
    "C#": ("512BD4", "dotnet", "white"),
    "Java": ("ED8B00", "openjdk", "white"),
    "Go": ("00ADD8", "go", "white"),
    "Rust": ("000000", "rust", "white"),
    "Kotlin": ("7F52FF", "kotlin", "white"),
    "Swift": ("F05138", "swift", "white"),
    "PHP": ("777BB4", "php", "white"),
    "Ruby": ("CC342D", "ruby", "white"),
    "Dart": ("0175C2", "dart", "white"),
    "Shell": ("4EAA25", "gnubash", "white"),
    "Jupyter Notebook": ("F37626", "jupyter", "white"),
    "Vue": ("4FC08D", "vuedotjs", "white"),
}


def api(path):
    request = urllib.request.Request(
        "https://api.github.com" + path,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def load_repos(featured=""):
    repos, page = [], 1
    while True:
        batch = api(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    repos = [
        r for r in repos
        if not r["fork"] and not r["archived"] and not r["private"]
        and r["name"] not in EXCLUDE
        and "hide-from-profile" not in r.get("topics", [])
        and not (SKIP_FEATURED and links_to(featured, r["name"]))
    ]
    repos.sort(key=lambda r: r["created_at"], reverse=True)
    return repos[:MAX_PROJECTS] if MAX_PROJECTS else repos


def links_to(text, name):
    """True if text links to this repo (or its GitHub Pages site)."""
    text = text.lower()
    name = name.lower()
    for prefix in (f"github.com/{USER.lower()}/{name}", f"{USER.lower()}.github.io/{name}"):
        at = text.find(prefix)
        while at != -1:
            nxt = text[at + len(prefix):at + len(prefix) + 1]
            if not (nxt.isalnum() or nxt in "-_."):
                return True
            at = text.find(prefix, at + 1)
    return False


def languages(repo):
    """Up to three main languages of a repo, largest first."""
    try:
        langs = api(f"/repos/{USER}/{repo['name']}/languages")
        return list(langs)[:3]
    except Exception:
        return [repo["language"]] if repo["language"] else []


def live_url(repo):
    if repo.get("homepage"):
        url = repo["homepage"].strip()
        return url if url.startswith("http") else "https://" + url
    if repo.get("has_pages"):
        return f"https://{USER}.github.io/{repo['name']}/"
    return ""


def esc(text):
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def badge(lang):
    color, logo, logo_color = LANGUAGE_BADGES.get(lang, ("0f172a", "", "white"))
    label = urllib.parse.quote(lang.replace("-", "--").replace(" ", "_"))
    logo_part = f"&logo={logo}&logoColor={logo_color}" if logo else ""
    return (f'<img src="https://img.shields.io/badge/{label}-{color}'
            f'?style=flat-square{logo_part}" alt="{esc(lang)}" />')


def card(repo):
    name = repo["name"]
    words = name.replace("-", " ").replace("_", " ")
    title = words if any(c.isupper() for c in name) else words.title()
    source = repo["html_url"]
    live = live_url(repo)
    created = datetime.datetime.strptime(repo["created_at"][:10], "%Y-%m-%d").strftime("%b %Y")
    description = esc(repo["description"]) or "<i>No description yet.</i>"
    stars = repo["stargazers_count"]

    links = []
    if live:
        links.append(f'<a href="{esc(live)}"><b>Live demo →</b></a>')
    links.append(f'<a href="{source}"><b>Source →</b></a>')
    meta = f"🗓️ {created}" + (f" &nbsp;·&nbsp; ⭐ {stars}" if stars else "")

    return f"""    <td width="50%" valign="top">
      <h3>📁 <a href="{source}">{esc(title)}</a></h3>
      <p>{description}</p>
      <p>
        {chr(10).join("        " + badge(l) for l in languages(repo)).strip()}
      </p>
      <p><sub>{meta}</sub></p>
      {" &nbsp;·&nbsp; ".join(links)}
    </td>"""


def section(repos):
    if not repos:
        return START + "\n" + END
    rows = []
    for i in range(0, len(repos), 2):
        cells = [card(r) for r in repos[i:i + 2]]
        if len(cells) == 1:
            cells.append('    <td width="50%"></td>')
        rows.append("  <tr>\n" + "\n".join(cells) + "\n  </tr>")
    return f"""{START}
## 🆕 Latest projects

<p align="center"><sub>Updated automatically whenever I publish a new repository. Newest first.</sub></p>

<table>
{chr(10).join(rows)}
</table>

<p align="center">
  <a href="https://github.com/{USER}?tab=repositories"><b>📂 Browse all repositories →</b></a>
</p>

---

{END}"""


def main():
    with open(README, encoding="utf-8") as f:
        current = f.read()
    start, end = current.find(START), current.find(END)
    featured = current[:start] + current[end:] if start != -1 and end != -1 else current
    block = section(load_repos(featured))

    if start != -1 and end != -1:
        new = current[:start] + block + current[end + len(END):]
    elif INSERT_BEFORE in current:
        at = current.index(INSERT_BEFORE)
        new = current[:at] + block + "\n\n" + current[at:]
    else:
        new = current.rstrip() + "\n\n---\n\n" + block + "\n"

    if new != current:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
        print("README.md updated")
    else:
        print("README.md already up to date")


if __name__ == "__main__":
    main()
