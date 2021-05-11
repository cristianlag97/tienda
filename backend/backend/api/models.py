from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    product = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.quantity

