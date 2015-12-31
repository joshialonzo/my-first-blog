from django.shortcuts import render

# Learn   more    about   Django  views   by  reading the official    documentation:
# https://docs.djangoproject.com/en/1.8/topics/http/views/

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})