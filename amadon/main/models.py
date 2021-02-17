from django.db import models

# Create your models here.
class Store(models.Model): 
    item = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)