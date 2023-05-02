from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import (AllergyViewSet, CategoryViewSet, 
                    FoodAllegryViewSet, FoodViewSet,MiniFoodAllegryViewSet)

router = DefaultRouter()

router.register("food", FoodViewSet, basename="Food")
router.register("allergy", AllergyViewSet, basename="Allergy")
router.register("category", CategoryViewSet, basename="Category")
router.register("foodallegry", FoodAllegryViewSet, basename="FoodAllergy")
router.register("minifoodallergy", MiniFoodAllegryViewSet, basename="MiniFoodAllergy")
urlpatterns = [
    path("", include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)