from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CartViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)