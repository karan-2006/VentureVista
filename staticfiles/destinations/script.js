document.getElementById('search').addEventListener('input', function() {
    let filter = this.value.toLowerCase();
    let destinations = document.querySelectorAll('.destination-card');
    
    destinations.forEach(card => {
        let name = card.getAttribute('data-name');
        if (name.includes(filter)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});

document.querySelectorAll('.view-details').forEach(button => {
    button.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = this.getAttribute('data-name');
        document.getElementById('modalDescription').textContent = this.getAttribute('data-desc');
        document.getElementById('modalImage').src = this.getAttribute('data-img');
        let modal = new bootstrap.Modal(document.getElementById('detailsModal'));
        modal.show();
    });
});