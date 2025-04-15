document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = document.getElementById("theme-icon");

    let currentTheme = localStorage.getItem("theme") || "light";

    function applyTheme(theme) {
        document.documentElement.setAttribute("data-bs-theme", theme);
        localStorage.setItem("theme", theme);
        themeIcon.textContent = theme === "dark" ? "☀️" : "🌙";
    }

    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            currentTheme = currentTheme === "dark" ? "light" : "dark";
            applyTheme(currentTheme);
        });
    }

    applyTheme(currentTheme);
});
