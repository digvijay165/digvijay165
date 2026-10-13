const root = document.documentElement;
const themeButton = document.querySelector("#theme-toggle");
const announcement = document.querySelector("#announcement");

function applyTheme(theme) {
  const dark = theme === "dark";
  root.dataset.theme = dark ? "dark" : "light";
  themeButton.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  themeButton.title = dark ? "Switch to light theme" : "Switch to dark theme";
  document.querySelector('meta[name="theme-color"]').content = dark ? "#151a17" : "#f6f5f0";
}

try {
  applyTheme(localStorage.getItem("digvijay-theme") || "light");
} catch {
  applyTheme("light");
}

themeButton.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
  applyTheme(nextTheme);
  try { localStorage.setItem("digvijay-theme", nextTheme); } catch { /* Theme still works for this visit. */ }
});

document.querySelectorAll(".filter-button").forEach((button) => {
  button.addEventListener("click", () => {
    const selected = button.dataset.filter;
    document.querySelectorAll(".filter-button").forEach((filter) => {
      const active = filter === button;
      filter.classList.toggle("is-active", active);
      filter.setAttribute("aria-pressed", String(active));
    });
    document.querySelectorAll(".project-card").forEach((card) => {
      card.hidden = selected !== "all" && card.dataset.category !== selected;
    });
    announcement.textContent = selected === "all" ? "Showing all projects." : `Showing ${selected === "civic" ? "civic technology" : "web tool"} projects.`;
  });
});

document.querySelector("#year").textContent = new Date().getFullYear();

async function loadGithubStats() {
  const count = document.querySelector("#repo-count");
  const stars = document.querySelector("#star-count");
  try {
    const response = await fetch("https://api.github.com/users/digvijay165/repos?per_page=100&sort=updated", {
      headers: { Accept: "application/vnd.github+json" },
      cache: "no-store",
    });
    if (!response.ok) throw new Error("GitHub profile is temporarily unavailable.");
    const repos = await response.json();
    count.textContent = new Intl.NumberFormat().format(repos.length);
    stars.textContent = new Intl.NumberFormat().format(repos.reduce((total, repo) => total + (repo.stargazers_count || 0), 0));
  } catch {
    count.textContent = "—";
    stars.textContent = "—";
  }
}

loadGithubStats();

