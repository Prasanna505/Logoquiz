from django.db import models
from django.forms import CharField

# Create your models here.

class PointsTable(models.Model):
    name = models.CharField(max_length=20)
    points = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name