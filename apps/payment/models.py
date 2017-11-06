from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPersonalModel(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=9)
    nacimiento = models.DateField


class UserFinancialModel(models.Model):
    user = models.ForeignKey(User, null=True)
    titular = models.CharField(max_length=80)
    caducidad = models.DateField
    codigo_cvv = models.IntegerField()
    numero_tarjeta = models.IntegerField()
    direccion = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    codigo_postal = models.IntegerField()
