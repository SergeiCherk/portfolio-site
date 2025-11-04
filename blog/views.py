from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    # Преобразуем tags в список
    for post in posts:
        if post.tags:
            post.tag_list = [tag.strip() for tag in post.tags.split(',')]
        else:
            post.tag_list = []
    
    return render(request, 'blog/list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    if post.tags:
        post.tag_list = [tag.strip() for tag in post.tags.split(',')]
    else:
        post.tag_list = []
    return render(request, 'blog/detail.html', {'post': post})