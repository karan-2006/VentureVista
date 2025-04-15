from django.db import models
from django.conf import settings  

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('travel_tips', 'Travel Tips'),
        ('customer_stories', 'Customer Stories'),
        ('industry_news', 'Industry News'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False,null=False)


    def __str__(self):
        return self.title
