from django.conf import settings
from django.db import models
from destinations.models import Destination

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    anonymous_user = models.CharField(max_length=255, blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        username = self.user.username if self.user else self.anonymous_user or "Anonymous"
        return f"Review by {username} for {self.destination} - Rating: {self.rating}"
