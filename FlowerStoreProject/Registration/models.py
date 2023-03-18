from django.db import models

# Create your models here.
class Registration(models.Model):
    full_name=models.CharField(max_length=50,null=0,default=0)
    username=models.CharField(max_length=50,null=0,default=0)
    email=models.EmailField(max_length=50,null=0,default=0)
    password=models.CharField(max_length=50,null=0,default=0)
    confirm_password=models.CharField(max_length=50,null=0,default=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)