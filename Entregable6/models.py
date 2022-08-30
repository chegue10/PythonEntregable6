from django.db import models

# Create your models here.
class Personas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField
    fecha_nacimiento = models.DateField()



    