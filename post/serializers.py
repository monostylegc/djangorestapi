from rest_framework import serializers
from .models import Post, Comment, Vote

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['pk', 'post', 'content']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote 
        fields = ['pk', 'post', 'vote',]
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only=True)
    votes = VoteSerializer(many = True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['pk', 'title','text', 'comments', 'votes',]
    