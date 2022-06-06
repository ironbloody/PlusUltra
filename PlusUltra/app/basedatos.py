from django.contrib.auth.models import AbstractUser
from django.db import models

### https://learndjango.com/tutorials/django-custom-user-model
# modelo User personalizado.

class Usuario(AbstractUser):
    # atributos adicionales.
    email = models.EmailField('email address', unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'rut']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Genero(models.Model):
	nombre = models.CharField(max_length=255)

class Articulo(models.Model):
	nombre = models.CharField(max_length=255)
	precio = models.integerField(max_length=255)
	stock = models.integerField(max_length=255)
	
