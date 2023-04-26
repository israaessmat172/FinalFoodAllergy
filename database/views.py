from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Allergy, Category, Food, FoodAllergy
from .permissions import FoodAllergyPermission, CategoryPermission, AllergyPermission, FoodPermission
from .serializers import (
    AllergySerializer,
    CategorySerializer,
    FoodAllergySerializer,
    FoodSerializer, 
)
# Create your views here.

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [FoodPermission]


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [AllergyPermission]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermission]
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

   

class FoodAllegryViewSet(viewsets.ModelViewSet):
    queryset = FoodAllergy.objects.all()
    serializer_class = FoodAllergySerializer
    permission_classes = [FoodAllergyPermission]


    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    