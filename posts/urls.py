from django.urls import path, include
from rest_framework import routers
from .views import PublicPostViewSet, CommentViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PublicPostViewSet, basename='Posts')
router.register('addposts', PostViewSet, basename='Posts')
# router.register('likes', LikeViewSet, basename='Likes')
router.register('comments', CommentViewSet, basename='Comments')

urlpatterns = [
    path('', include(router.urls)),
]