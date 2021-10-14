from django.db import models
import os
from django.core.files import File
import urllib


class ItemforHire(models.Model):
    product_name = models.CharField(max_length=120)
    product_details = models.TextField(max_length=1000)
    contact_number = models.IntegerField(default=None)
    #lender_email = models.EmailField(max_length=120, help_text='Required. Enter a valid email address.')
    product_pic = models.FileField(upload_to='Images/', blank=True, null=True)
    product_price = models.FloatField()
    product_stock = models.IntegerField()
    product_condition = models.CharField(max_length=120)
    hire_duration = models.DurationField()
    product_location = models.CharField(max_length=50)








