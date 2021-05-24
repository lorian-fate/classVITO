from django.db import models


# Create your models here.


class Dea(models.Model):
    codigo_dea = models.CharField(max_length = 100)
    direccion_ubicacion = models.CharField(max_length = 100)
    direccion_portal_numero = models.CharField(max_length = 10)
    horario_acceso = models.CharField(max_length = 100)
    x_utm = models.IntegerField(default = None)
    y_utm = models.IntegerField(default = None)


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)