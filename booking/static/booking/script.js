document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.location-field').forEach(field => {
        field.addEventListener('input', function() {
            let value = this.value;
            document.querySelectorAll('.location-field').forEach(otherField => {
                if (otherField !== this) {
                    otherField.value = value;
                }
            });
        });
    });

    let today = new Date().toISOString().split('T')[0];
    document.querySelectorAll('.date-input').forEach(input => {
        input.value = today;
        input.min = today;
    });

    document.querySelectorAll('.date-input').forEach(dateField => {
        dateField.addEventListener('change', function() {
            let selectedDate = this.value;
            document.querySelectorAll('.date-input').forEach(otherDateField => {
                if (otherDateField !== this && otherDateField.value < selectedDate) {
                    otherDateField.value = selectedDate;
                    otherDateField.min = selectedDate;
                }
            });
        });
    });

    document.querySelectorAll('.search-btn').forEach(button => {
        button.addEventListener('click', function() {
            let type = this.dataset.type;
            let destination = document.querySelector(`#${type}Location`)?.value;
            let startDate = document.querySelector(`#${type}StartDate`)?.value || today;
            let endDate = document.querySelector(`#${type}EndDate`)?.value || startDate;

            if (!destination) {
                alert("Please enter a destination.");
                return;
            }

            let searchUrl = `/search-${type}/?destination=${destination}&start=${startDate}&end=${endDate}`;
            window.location.href = searchUrl;
        });
    });
});
