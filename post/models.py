from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def path_image_path(instance, filename):
    return f'posts/{instance.post.content}/{filename}'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name = 'images')
    image = models.ImageField(upload_to = 'path_image_path')
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name = 'comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    
