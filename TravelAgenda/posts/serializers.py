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

class PostSendSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        required=False, 
        write_only=True  # Prevents image data from being returned in responses
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'images']

    def validate_content(self, value):
        if len(value) < 10 or len(value) > 500:
            raise serializers.ValidationError("Content must be between 10 and 500 characters.")
        # Add additional content safety checks here as needed
        return value

    def validate_images(self, value):
        if len(value) > 9:
            raise serializers.ValidationError("You can upload up to 9 images only.")
        return value

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        post = Post.objects.create(**validated_data)
        
        # Save each image associated with the post
        for image in images:
            Image.objects.create(post=post, image=image)  # Assuming Image model has a 'post' FK and 'image' field

        return post