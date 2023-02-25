from django.db import models

# Create your models here.
class Feature(models.Model): 

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=300,default="HELLO, WORLD!")

class Client(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=200)
