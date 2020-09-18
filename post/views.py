from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import PostSerializer, CommentSerializer, PostImageSerializer
from .models import Post, Comment, PostImage

class PostViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PostImageViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
 