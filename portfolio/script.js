"use strict";
const root = document.documentElement;
function getRequiredElement(selector) {
    const element = document.querySelector(selector);
    if (!element)
        throw new Error(`Portfolio element is missing: ${selector}`);
    return element;
}
const themeButton = getRequiredElement("#theme-toggle");
const announcement = getRequiredElement("#announcement");
const themeColor = getRequiredElement('meta[name="theme-color"]');
function applyTheme(theme) {
    const isDark = theme === "dark";
    root.dataset.theme = theme;
    themeButton.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
    themeButton.title = isDark ? "Switch to light theme" : "Switch to dark theme";
    themeColor.content = isDark ? "#151a17" : "#f6f5f0";
}
function readSavedTheme() {
    try {
        return window.localStorage.getItem("digvijay-theme") === "dark" ? "dark" : "light";
    }
    catch {
        return "light";
    }
}
applyTheme(readSavedTheme());
themeButton.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
    applyTheme(nextTheme);
    try {
        window.localStorage.setItem("digvijay-theme", nextTheme);
    }
    catch {
        // The selected theme still applies for the current visit.
    }
});
function isProjectFilter(value) {
    return value === "all" || value === "civic" || value === "tools";
}
const filterButtons = document.querySelectorAll(".filter-button");
const projectCards = document.querySelectorAll(".project-card");
filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const selectedFilter = button.dataset.filter;
        if (!isProjectFilter(selectedFilter))
            return;
        filterButtons.forEach((filterButton) => {
            const isSelected = filterButton === button;
            filterButton.classList.toggle("is-active", isSelected);
            filterButton.setAttribute("aria-pressed", String(isSelected));
        });
        projectCards.forEach((card) => {
            card.hidden = selectedFilter !== "all" && card.dataset.category !== selectedFilter;
        });
        const announcementText = selectedFilter === "all"
            ? "Showing all projects."
            : `Showing ${selectedFilter === "civic" ? "civic technology" : "web tool"} projects.`;
        announcement.textContent = announcementText;
    });
});
const year = document.querySelector("#year");
if (year)
    year.textContent = String(new Date().getFullYear());
async function loadGitHubStats() {
    const repositoryCount = document.querySelector("#repo-count");
    const starCount = document.querySelector("#star-count");
    if (!repositoryCount || !starCount)
        return;
    try {
        const response = await fetch("https://api.github.com/users/digvijay165/repos?per_page=100&sort=updated", {
            headers: { Accept: "application/vnd.github+json" },
            cache: "no-store",
        });
        if (!response.ok)
            throw new Error("GitHub profile is temporarily unavailable.");
        const repositories = await response.json();
        repositoryCount.textContent = new Intl.NumberFormat().format(repositories.length);
        const stars = repositories.reduce((total, repository) => total + (repository.stargazers_count ?? 0), 0);
        starCount.textContent = new Intl.NumberFormat().format(stars);
    }
    catch {
        repositoryCount.textContent = "—";
        starCount.textContent = "—";
    }
}
void loadGitHubStats();

