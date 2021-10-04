from django.db import models
import os
from django.core.files import File
import urllib
class Item(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    product_name= models.CharField(max_length=120)
    product_details=models.TextField(max_length=1000)
    contact_number = models.IntegerField(default=None )
    product_pic=models.FileField(upload_to='Images/',blank=True,null=True)
    product_price = models.FloatField()
    product_stock = models.IntegerField()
    





