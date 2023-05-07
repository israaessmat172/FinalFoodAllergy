from django.urls import path
from .views import predict_food

urlpatterns = [
    path('predict_food/', predict_food, name='predict_food'),
]