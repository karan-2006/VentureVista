from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

def blog_index(request):
    posts_by_category = {
        "Travel Tips": BlogPost.objects.filter(category="travel_tips").order_by('-created_at')[:8],
        "Customer Stories": BlogPost.objects.filter(category="customer_stories").order_by('-created_at')[:8],
        "Industry News": BlogPost.objects.filter(category="industry_news").order_by('-created_at')[:8],
    }
    return render(request, 'blog/index.html', {"categories": posts_by_category})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog:blog_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_blog_post.html', {'form': form})
