from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"