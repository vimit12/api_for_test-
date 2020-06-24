from django.contrib import admin
from .models import ProductDetail

# Register your models here.
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_url',
                    'product_image', 'product_price']





admin.site.register(ProductDetail, ProductDetailAdmin)

