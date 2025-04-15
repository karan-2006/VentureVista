    // Bootstrap Carousel Auto-slide
    const carouselElement = document.querySelector("#carouselExampleIndicators");
    if (carouselElement) {
        new bootstrap.Carousel(carouselElement, {
            interval: 3000,
            ride: "carousel"
        });
    }

    // Validate phone input
    const phoneInput = document.querySelector("#phone");
    const getAppLinkBtn = document.querySelector("input[type='submit']");

    if (phoneInput && getAppLinkBtn) {
        getAppLinkBtn.addEventListener("click", function (event) {
            event.preventDefault();
            const phonePattern = /^[0-9]{3}-[0-9]{3}-[0-9]{4}$/;

            if (!phonePattern.test(phoneInput.value)) {
                alert("Please enter a valid phone number in the format 012-345-6789.");
            } else {
                alert("App link sent to your phone!");
                phoneInput.value = "";
            }
        });
    }

