from rest_framework import serializers
from .models import Product, Cart, Rating

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    def get_products(self, obj):
        products = obj.products
        dataofproducts = {
            "image": products.image,
            "arabicDescription": products.arabicDescription,
            "englishDescription": products.englishDescription,
            "arabicName": products.arabicName,
            "englishName": products.englishName,
            "price": products.price,
        }
        return dataofproducts

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"