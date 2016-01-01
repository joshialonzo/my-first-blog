from django import forms
from .models import Post

# https://docs.djangoproject.com/en/1.8/topics/forms/

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
