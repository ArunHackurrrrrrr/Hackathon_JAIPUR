from django.db import models

# Create your models here.
class userData(models.Model):
    userUid = models.CharField(max_length=20,default='NIL')
    userName = models.CharField(max_length=20,default='NIL')
    userMail = models.CharField(max_length=20,default='NIL')
    userPass = models.CharField(max_length=20,default='NIL')
    userRole = models.CharField(max_length=30,default='NIL')
    
class UserLocation(models.Model):
    userDate = models.DateField()
    userTime = models.CharField(max_length=25,default='NIL')
    userLon = models.CharField(max_length=50,default='NIL')
    userLat = models.CharField(max_length=50,default='NIL')
    userCheckIn = models.CharField(max_length=100,default='NIL')
    userCheckOut = models.CharField(max_length=100,default='NIL')
class userLog(models.Model):
    userLogin = models.CharField(max_length=25,default='NIL')
    userLogOut = models.CharField(max_length=25,default='NIL')
    userLoginT = models.TimeField(default='00:00:00')
    userLogOutT = models.TimeField(default='00:00:00')
 
class userAtt(models.Model):
    attDate = models.CharField(max_length=25,default='NIL')
    att = models.CharField(max_length=25,default='NIL')

class Office(models.Model):
    latOffice = models.CharField(max_length=30,default='NIL')
    longOffice = models.CharField(max_length=30,default='NIL')
    radOffice = models.CharField(max_length=30,default='NIL')