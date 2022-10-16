from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Integrantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    depto = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido:{self.apellido} - Email:{self.email} Depto: {self.depto}"

class GastosFijos(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    valor = models.IntegerField()
    fechaDeVencimiento = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo} - Valor: {self.valor} - Fecha De Vencimiento: {self.fechaDeVencimiento}"


class TareasHogar(models.Model):
    nombre = models.CharField(max_length=30)
    fechaARealizar = models.DateField()
    realizada = models.BooleanField()

class GastosDiarios(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.IntegerField()
    tipo = models.CharField(max_length=30)
    fecha = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo} - Valor: {self.valor} - Fecha: {self.fecha}"


#class Avatar(models.Model):
#    #vinculo con el usuario
#    user = models.ForeignKey(User, on_delete = models.CASCADE)
#    #subcarpeta avatares de media
#    image = models.ImageField(upload_to='avatares', null = True, blank = True)
