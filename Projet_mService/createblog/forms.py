from django import forms
from .models import Post, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

class ImageForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput, required=False)

    class Meta:
        model = Image
        fields = ['images']
