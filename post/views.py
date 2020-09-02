from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer, CommentSerializer, VoteSerializer
from .models import Post, Comment, Vote

class PostViewSet(ModelViewSet):
   queryset = Post.objects.all()
   serializer_class = PostSerializer
    
class CommentViewSet(ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
    
class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
