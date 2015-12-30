from django.contrib import admin
from .models import Post

# Register your models here.

# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
# admin package
# site module inside admin
# register function inside site module
admin.site.register(Post)