from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    product_name= models.CharField(max_length=120)
    product_details=models.CharField(max_length=300)
    contact_number = models.IntegerField()
    product_pic=models.ImageField(upload_to='Images/')
    product_price = models.FloatField()
    product_stock = models.IntegerField()


def __str__(self):
    return self.contact_number 


