from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='offers/', null=True, blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Slide(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='slides/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title