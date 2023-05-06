from django.contrib import admin
from . import models
from .models import Cart


class ProductAdmin(admin.ModelAdmin):
 
    search_fields = [
        "arabicName",
        "englishName",
        "arabicDescription",
        "englishDescription",
    ]

    filterset_fields = [
        "arabicName",
        "englishName",
        "arabicDescription",
        "englishDescription",
    ]
    

admin.site.register(models.Product, ProductAdmin)
admin.site.register(Cart)

