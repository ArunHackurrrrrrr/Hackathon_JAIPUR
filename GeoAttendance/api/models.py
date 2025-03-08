from django.db import models

# Create your models here.
class UserData(models.Model):
    userName = models.CharField(max_length=20,default='nil')
    userpass = models.CharField(max_length=20,default='nil')
    useremail = models.CharField(max_length=20,default='nil')
    usermobi = models.CharField(max_length=20,default='nil')