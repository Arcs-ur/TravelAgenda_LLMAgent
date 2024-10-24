from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Image, Comment

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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 只展示评论内容字段
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write a comment...', 'rows': 3}),
        }

# class PostUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content'] 

# class ImageUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image'] 
#         widgets = {
#             'image': forms.ClearableFileInput(attrs={'multiple': True}),
#         }