from django.db import models

# Create your models here.

class Info(models.Model):
    type_of=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    prof_pic = models.ImageField(upload_to='pics')
    username =models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)

