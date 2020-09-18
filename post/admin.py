from django.contrib import admin
from .models import Post, Comment, PostImage

# Register your models here.
admin.site.register(Comment)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    
    class meta:
        model = Post
        
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
