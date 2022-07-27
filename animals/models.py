from django.db import models
from characterisrics.models import Characteristic
from groups.models import Group

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    characteristics = models.ManyToManyField(Characteristic)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, related_name='animals')
    


 