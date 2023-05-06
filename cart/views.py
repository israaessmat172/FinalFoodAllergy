from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Cart, Rating
from .serializers import ProductSerializer, CartSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    @action(detail=True, methods=['POST'])
    def rate(self, request, pk=None):
        user = request.user
        product = self.get_object()
        rating = request.data.get('rating')

        Rating.objects.update_or_create(user=user, product=product, defaults={'rating': rating})

        product.refresh_from_db()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=user, product=product, defaults={'quantity': quantity, 'price': product.price * quantity})

        if not created:
            cart.quantity += quantity
            cart.price += product.price * quantity
            cart.save()

        serializer = self.get_serializer(cart)
        return Response(serializer.data)
