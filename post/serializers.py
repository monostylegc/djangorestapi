from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['pk', 'post', 'content']

        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['pk', 'title','text', 'comments',]
    