from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    numeroT = models.IntegerField()
    descripcion = models.CharField(max_length=500)