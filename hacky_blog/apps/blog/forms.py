from django import forms
from .models import Post, Comment

# https://docs.djangoproject.com/en/1.8/topics/forms/

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)