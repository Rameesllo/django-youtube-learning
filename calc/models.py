from django.db import models

# Create your models here.
class Destination:
    id: int
    name: str
    desc: str
    price: int
    offer: bool



class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.CharField(max_length=100)