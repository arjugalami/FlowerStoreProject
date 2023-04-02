from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VendorRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_name=models.CharField(max_length=50,default=0)
    vendor_photo=models.ImageField(upload_to="static/images/",null=True,blank=True)
    vendor_email=models.EmailField(max_length=50,null=0,default=0)
    vendor_location=models.CharField(max_length=50,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#data base ma connectivity ko lagi use


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_name=models.CharField(max_length=50,default=0)
    product_photo=models.ImageField(upload_to="static/images/",null=True,blank=True)
    product_description=models.CharField(max_length=500,default=0)
    product_price=models.IntegerField(max_length=10,default=0)
    product_quantity=models.IntegerField(max_length=10,default=0)
    product_address=models.CharField(max_length=50,default=0)