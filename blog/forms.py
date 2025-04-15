from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=BlogPost.CATEGORY_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'category']
