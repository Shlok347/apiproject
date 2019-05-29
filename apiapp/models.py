from django.db import models

# Create your models here.
class UserProfile(models.Model):
    email = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    user_password = models.CharField(max_length=254)
    imei = models.CharField(max_length=64)
    lock_password = models.CharField(max_length=32)
    master_id = models.CharField(max_length=64)
    master_password = models.CharField(max_length=32)

class MasterProfile(models.Model):
    name = models.CharField(max_length=64)
    master_password = models.CharField(max_length=64)
