from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
class Products(models.Model):
    name=models.TextField(max_length=55)
    desc=models.TextField(max_length=1000)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.ImageField(upload_to='Images/')   