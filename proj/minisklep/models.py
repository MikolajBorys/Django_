from django.db import models

# Create your models here.

class Produkt(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Name