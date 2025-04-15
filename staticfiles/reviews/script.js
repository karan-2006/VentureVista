document.addEventListener("DOMContentLoaded", function () {
    // === Filter Section ===
    const destinationFilter = document.getElementById("filter-destination");
    const ratingFilter = document.getElementById("filter-rating");
    const reviews = document.querySelectorAll(".review-card");

    function filterReviews() {
        const selectedDestination = destinationFilter.value;
        const selectedRating = ratingFilter.value;

        reviews.forEach(review => {
            const reviewDestination = review.getAttribute("data-destination");
            const reviewRating = review.getAttribute("data-rating");

            const matchesDestination = !selectedDestination || reviewDestination === selectedDestination;
            const matchesRating = !selectedRating || reviewRating === selectedRating;

            review.style.display = (matchesDestination && matchesRating) ? "block" : "none";
        });
    }

    // Event Listeners for filters
    if (destinationFilter && ratingFilter) {
        destinationFilter.addEventListener("change", filterReviews);
        ratingFilter.addEventListener("change", filterReviews);
    }

    // === Like Button Section ===
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function () {
            const reviewId = this.getAttribute('data-review-id');
            const likeCount = this.querySelector('.like-count');
            const self = this;

            fetch(`/reviews/like/${reviewId}/`, {
                method: 'POST',
                headers: { 'X-CSRFToken': '{{ csrf_token }}' }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    likeCount.innerText = data.likes;
                    self.classList.toggle('btn-outline-success');
                    self.classList.toggle('btn-success');
                    showToast("You liked this!", "success");
                } else {
                    showToast("Error liking review", "danger");
                }
            });
        });
    });

    // === Delete Review Section ===
    document.querySelectorAll('.delete-review-btn').forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            if (confirm('Are you sure you want to delete this review?')) {
                const reviewId = this.getAttribute('data-review-id');
                const reviewCard = this.closest('.review-card');

                fetch(`/reviews/delete/${reviewId}/`, {
                    method: 'POST',
                    headers: { 'X-CSRFToken': '{{ csrf_token }}' }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        reviewCard.remove();
                        showToast("Review deleted successfully", "danger");
                    } else {
                        showToast("Failed to delete review", "danger");
                    }
                });
            }
        });
    });

});

// Toast function for notifications
function showToast(message, type="success") {
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-bg-${type} border-0 show mb-2`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    document.getElementById('toast-container').appendChild(toast);
    setTimeout(() => toast.remove(), 4000);
}
