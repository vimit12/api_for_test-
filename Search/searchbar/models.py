from django.db import models
from datetime import date, datetime

# Create your models here.
class ProductDetail(models.Model):
    name = models.CharField(max_length=264,default=False)
    product_name = models.CharField(max_length=264)
    product_url = models.URLField(max_length=200,blank=True)
    product_image = models.URLField(max_length=200, blank=True)
    product_price = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f'self.product_name'

