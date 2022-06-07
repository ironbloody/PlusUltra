from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario, Revista, Publicacion, Idioma, IdiomaPublicacion, Genero, Articulo, Compra, Ejemplar, Tipo, Editorial, Ciudad
#
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ["email", "username", "first_name", "last_name", "ciudad"]
    
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ["email", "username", "first_name", "last_name", "ciudad"]

#
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'revista', 'fecha')
    list_filter = ('revista', 'fecha')
    search_fields = ('titulo',)

#
class IdiomaPublicacionAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'idioma', 'fecha')
    list_filter = ('idioma', 'fecha')

#
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(IdiomaPublicacion, IdiomaPublicacionAdmin)



admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Articulo)
admin.site.register(Compra)
admin.site.register(Ejemplar)
admin.site.register(Tipo)
admin.site.register(Editorial)
admin.site.register(Ciudad)
