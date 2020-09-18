from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from .views import PostViewSet, PostImageViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()
post_router = router.register(r'post', PostViewSet)
post_router.register(r'postimage', PostImageViewSet, basename='post-image', parents_query_lookups = ['post'])

urlpatterns = [
   path('', include(router.urls)),
]
