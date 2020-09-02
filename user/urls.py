from django.urls import path, include  
from rest_framework import routers  
from . import views

router = routers.DefaultRouter()  
router.register(r'user', views.UserViewSet)  
router.register(r'group', views.GroupViewSet)

urlpatterns = [  
    # 사용자, 그룹목록 처리를 위한 url - 위의 router에서 처리되어 있다
    path('', include(router.urls)),
    # 인증처리를 위한 url
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]