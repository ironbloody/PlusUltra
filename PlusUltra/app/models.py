from django.contrib.auth.models import AbstractUser
from django.db import models

### https://learndjango.com/tutorials/django-custom-user-model
# modelo User personalizado.
class Usuario(AbstractUser):
    # atributos adicionales.
    email = models.EmailField('email address', unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

#################################################################################
class Revista(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
         return self.nombre

class Publicacion(models.Model):
    titulo = models.CharField(max_length=500)
    fecha = models.DateField()
    revista = models.ForeignKey(to=Revista, on_delete=models.CASCADE, null=True)
    investigador = models.ManyToManyField(to=Usuario)
    
    def __str__(self):
         return self.titulo

class Idioma(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
         return self.nombre

### https://zerotobyte.com/django-many-to-many-relationship-explained/
class IdiomaPublicacion(models.Model):
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fecha = models.DateField()
    
    class Meta:
        # para que sea una combinación única.
        # https://docs.djangoproject.com/en/dev/ref/models/options/#unique-together
        unique_together = ('idioma', 'publicacion',)

    def __str__(self):
        return self.publicacion.titulo + ' - ' + self.idioma.nombre

class Genero(models.Model):
	nombre = models.CharField(max_length=255)
	
	def __str__(self):
        	return self.nombre

