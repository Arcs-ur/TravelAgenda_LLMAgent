from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Image

class PostSendForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        word_count = len(content.split())
        if word_count < 10 or word_count > 200:
            raise ValidationError('Content must be between 10 and 200 words.')
        return content

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
