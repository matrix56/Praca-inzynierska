from django.db import models

# Create your models here.
class Patient(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    pesel = models.IntegerField()

    def __str__(self):
        return self.surname + " " + self.name
