from rest_framework import serializers
from .models import Post, Comment, PostImage

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['pk', 'author', 'post', 'content']


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['pk', 'post', 'image']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only=True)
    images = PostImageSerializer(many = True)
    
    class Meta:
        model = Post
        fields = ['pk', 'author', 'title','text', 'images', 'comments',]
    