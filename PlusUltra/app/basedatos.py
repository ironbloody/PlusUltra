from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # atributos adicionales.
    email = models.EmailField('email address', unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'rut']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Genero(models.Model):
	nombre = models.CharField(max_length=255)
	
	def __str__(self):
        	return self.nombre

class Articulo(models.Model):
	nombre = models.CharField(max_length=255)
	precio = models.integerField(max_length=255)
	stock = models.integerField(max_length=255)
	
