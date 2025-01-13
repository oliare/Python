from django.db import models

class Car(models.Model):
    CATEGORY_CHOICES = [
        (0, 'Sedan'),
        (1, 'SUV'),
        (2, 'Electric'),
        (3, 'Coupe'),
    ]

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    color = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, upload_to='cars/')
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)

    def __str__(self):
        return f"{self.brand} - {self.model} ({self.year})"

class Category(models.Model):
    name = models.CharField(max_length = 100, choices = Car.CATEGORY_CHOICES, default = 0) 

    def __str__(self):
        return self.name