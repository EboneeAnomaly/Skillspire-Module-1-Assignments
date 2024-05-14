from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dietary_preference = models.CharField(max_length=20)
    DIET_CHOICES = [
        ('vegitarian', 'Vegitarian'),
        ('vegan', 'Vegan'),
        ('no_preference', 'No Preference'),
    ]
    dietary_preference = models.CharField(max_length=50, choices=DIET_CHOICES)
