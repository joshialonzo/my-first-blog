from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Learn   more    about   Django  views   by  reading the official    documentation:
# https://docs.djangoproject.com/en/1.8/topics/http/views/

# Create your views here.
def post_list(request):
    # https://docs.djangoproject.com/en/1.8/ref/models/querysets/
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', { 'posts' : posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post' : post })
