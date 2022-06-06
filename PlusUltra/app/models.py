from django.contrib.auth.models import AbstractUser
from django.db import models

class Ciudad(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
        	return self.nombre

class Usuario(AbstractUser):
    # atributos adicionales.
    Email = models.EmailField('Email address', unique = True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Nombre', 'Apellido', 'RUT',]
   

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
        
#PLUSULTRAAAAAAAAA------------------------------------------

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Genero(models.Model):
	nombre = models.CharField(max_length=255)
	
	def __str__(self):
        	return self.nombre

class Editorial(models.Model):
	nombre = models.CharField(max_length=255, default="some string")

	def __str__(self):
        	return self.nombre

	
class Tipo(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
        	return self.nombre


class Articulo(models.Model):
	nombre = models.CharField(max_length=255)
	precio = models.IntegerField()
	stock = models.IntegerField()
	genero = models.ManyToManyField(Genero)
	editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
	tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
	idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
	
	def __str__(self):
        	return self.nombre
class Compra(models.Model):
	fecha = models.DateField()
	precio_total = models.IntegerField()
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Ejemplar(models.Model):
	nombre = models.CharField(max_length=255)
	articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

	def __str__(self):
        	return self.nombre


