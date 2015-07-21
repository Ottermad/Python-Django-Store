from django.db import models

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Shirt(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField()
    price = models.FloatField()
    paypal = models.CharField(max_length=13)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name