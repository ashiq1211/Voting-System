from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)