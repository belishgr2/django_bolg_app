from django import forms
from .models import Post

class PostModelForm(forms.ModelForml):
    class Meta:
        model = Post
        fields =['title','text']