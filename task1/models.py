from django.db import models
from datetime import datetime
# Create your models here.

class Info(models.Model):
    type_of=models.TextField(default='Hi')
    first_name=models.TextField(default='Hi')
    last_name=models.TextField(default='Hi')
    prof_pic = models.ImageField(upload_to='pics')
    username =models.TextField(default='Hi')
    email=models.EmailField(unique=True)
    password=models.TextField(default='Hi')
    address=models.TextField(default='Hi')
    city=models.TextField(default='Hi')
    state=models.TextField(default='Hi')
    pincode=models.TextField(default='Hi')
class Post(models.Model):
    title = models.TextField(default='Hi')
    content1 = models.TextField(default='Hi')
    date = models.DateTimeField(default = datetime.now, blank = True)
    category=models.TextField(default='Hi')
    summary=models.TextField(default='Hi')
    img = models.ImageField(upload_to = 'pics')
   

class Draft(models.Model):
    tag = models.TextField(default='draft')
    title = models.TextField(default='Hi')
    content1 = models.TextField(default='Hi')
    date = models.DateTimeField(default = datetime.now, blank = True)
    category=models.TextField(default='Hi')
    summary=models.TextField(default='Hi')
    img = models.ImageField(upload_to = 'pics')
    