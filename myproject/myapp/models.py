from msilib.schema import Feature
from django.db import models

# Create your models here.
class Feature(models.Model):
        name = models.CharField(max_length=50)
        detail = models.CharField(max_length=100)