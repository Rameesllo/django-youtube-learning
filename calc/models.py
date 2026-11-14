from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.CharField(max_length=100)

    def __str__(self):
        return self.name
