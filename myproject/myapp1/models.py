from django.db import models



class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
