from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Juegos(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Distribuidora(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Biblioteca(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Carrito(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Puntos(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)
    
class Tienda(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Perfil(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Amigos(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)

class Colección(models.Model):
    id = models.IntegerField(max_length=200)
    nombre = models.TextField(max_length=100)