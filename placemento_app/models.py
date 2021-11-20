from django.db import models

# Create your models here.

class hr_signup(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,default='')
    address = models.CharField(max_length=400)
    phonenumber = models.IntegerField(max_length=12)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class hr_login(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField(max_length=100,default='')
    password = models.CharField(max_length=15)

# This is for updateprofile.
class hr_models(models.Model):
    dept=models.CharField(max_length=50)
    year=models.IntegerField(max_length=10)
    rollno=models.IntegerField(max_length=20)
    skills=models.CharField(max_length=500)
