from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image', 'price', 'stock']


admin.site.register(Product)
