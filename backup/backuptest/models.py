from django.db import models
import pymongo
import mongoengine
from djangotoolbox.fields import ListField

class post(models.Model):
    title = models.CharField(max_length = 100)
    link = models.URLField()
    popularity = models.IntegerField()
    
    def __str__(self):
        return self.title

class Sitescrawled(models.Model):
    title = models.CharField(max_length = 1000)

    
    #tags = ListField()
    #comments = ListField()
    
    #code

# Create your models here.
