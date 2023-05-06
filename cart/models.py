from django.db import models
from users.models import User
from database.models import Allergy

class Product(models.Model):
    arabicName = models.CharField(max_length=255)
    englishName = models.CharField(max_length=255)
    arabicDescription = models.TextField()
    englishDescription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    ratings = models.ManyToManyField(User, through='Rating', related_name='rated_products')
    allergies = models.ManyToManyField(Allergy, related_name='products')

    def __str__(self):
        return f"{self.arabicName} - {self.englishName}"
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
