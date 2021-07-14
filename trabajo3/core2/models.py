from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True)
    nombreMarca = models.CharField(max_length=50, verbose_name='Nombre Marca')


class Modelo(models.Model):
    idModelo=models.IntegerField(primary_key=True)
    nombreModelo = models.CharField(max_length=50, verbose_name='Modelo')
    patente = models.CharField(max_length=6, verbose_name='Patente')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)


class Usuario(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=10)