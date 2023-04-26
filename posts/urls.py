from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')
# router.register('likes', LikeViewSet, basename='Likes')
router.register('comments', CommentViewSet, basename='Comments')

urlpatterns = [
    path('', include(router.urls)),
]