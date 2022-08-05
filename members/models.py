from os import name
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    relationship = models.CharField(max_length=40)
    age = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
