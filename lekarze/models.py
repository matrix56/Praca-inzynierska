from django.db import models
from django.utils import timezone
from django.utils import dates

class Doctor(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    specjalization = models.CharField(max_length=30)

    def __str__(self):
        return self.surname + " " + self.name + " " + self.specjalization

# Create your models here.
