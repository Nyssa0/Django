from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=2000, default="")
    image = models.URLField(max_length=200, default="")
    price = models.FloatField(
        validators=[MinValueValidator(0.0)], default=0.0
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0)], default=0
    )

    # renames the instances of the model
    # with their name
    def __str__(self):
        return self.name
