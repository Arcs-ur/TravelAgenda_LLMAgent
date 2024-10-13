from rest_framework import serializers
from .models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'uploaded_at']

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'created_at', 'likes', 'images']
        read_only_fields = ['user', 'created_at', 'likes']