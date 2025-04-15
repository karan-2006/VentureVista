document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll(".nav-link");
    tabs.forEach(tab => {
        tab.addEventListener("click", function() {
            setTimeout(() => {
                document.querySelector(".tab-pane.show").classList.add("fade-in");
            }, 150);
        });
    });
});