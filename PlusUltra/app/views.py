from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from .models import Publicacion, Revista, IdiomaPublicacion, Idioma, Usuario
from .forms import PublicacionForm, IdiomaPublicacionForm

# Decorador para verificar grupo.
def es_investigador(user):
    # usuario autenticado?
    if (user.is_authenticated):
        # usuario pertenece al grupo Investigador?
        return user.groups.filter(name='Investigador').exists()
    else:
        return False

# Create your views here.
@user_passes_test(es_investigador)
def index(request):
    template = loader.get_template('publicaciones/index.html')
    
    publicaciones = Publicacion.objects.filter(investigador=request.user)

    context = {
        'publicaciones': publicaciones,
        'settings': settings,
    }
    
    return HttpResponse(template.render(context, request))

@user_passes_test(es_investigador)
def add(request):
    if (request.method == 'GET'):
        form = PublicacionForm()
        # muesta usarios de esos grupos.
        form.fields['investigador'].queryset = Usuario.objects.filter(groups__name__in=['Investigador', 'Director'])
        #queryset = Usuario.objects.filter(groups__name__in=['Investigador', 'Director'])
        
        # mostrar formulario.
        template = loader.get_template('publicaciones/add.html')
    
        context = {
            'settings': settings,
            'form': form,
            'isadd': True,
        }
    
        return HttpResponse(template.render(context, request))
    
    elif (request.method == 'POST'):
        # guardar datos.
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ingreso realizado.")

        return redirect('index')
        
        

@user_passes_test(es_investigador)
def delete(request, id):
    publicacion = Publicacion.objects.get(id=id)
    
    if (request.method == 'GET'):
        # muestra el formulario.
        template = loader.get_template('publicaciones/delete.html')

        context = {
            'settings': settings,
            'publicacion': publicacion,
        }
    
        return HttpResponse(template.render(context, request))
        
    elif (request.method == 'POST'):
        # elimina la publicación.
        publicacion.delete()
        messages.success(request, "Eliminación realizada.")

        return redirect('index')

@user_passes_test(es_investigador)
def update(request, id):
    publicacion = Publicacion.objects.get(id=id)
    
    if (request.method == 'GET'):
        # muestra el formulario con datos.
        form = PublicacionForm(instance=publicacion)
        form.fields['investigador'].queryset = Usuario.objects.filter(groups__name__in=['Investigador', 'Director'])
        template = loader.get_template('publicaciones/add.html')

        context = {
            'publicacion': publicacion,
            'settings': settings,
            'form': form,
            'isadd': False,
        }
        
        return HttpResponse(template.render(context, request))
        
    elif (request.method == 'POST'):
        # actualiza datos.
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Actualización realizada.")

        return redirect('index')



"""
Idiomas Publicación.
"""

@user_passes_test(es_investigador)
def idiomapub(request, id):
    # obtiene la publicación.
    publicacion = Publicacion.objects.get(id=id)
    # obtiene los idiomas de la publicación.
    idiomapub = IdiomaPublicacion.objects.filter(publicacion=publicacion)
    
    template = loader.get_template('publicaciones/idiomapub.html')

    context = {
        'publicacion': publicacion,
        'idiomapub': idiomapub,
        'settings': settings,
    }
    
    return HttpResponse(template.render(context, request))

@user_passes_test(es_investigador)
def addidiomapub(request, id):
    #
    if (request.method == 'GET'):
        # pasa el id de la publicación.
        publicacion = Publicacion.objects.get(id=id)
        template = loader.get_template('publicaciones/addidiomapub.html')
    
        context = {
            'publicacion': publicacion,
            'settings': settings,
            'form': IdiomaPublicacionForm(publicacion=id),
            'isadd': True,
        }
    
        return HttpResponse(template.render(context, request))
        
    elif (request.method == 'POST'):
        # pasa id de publicación como parámetro.
        form = IdiomaPublicacionForm(request.POST, publicacion=id)
        
        if form.is_valid():
            form.save()
        else:
            #FIXME
            msg = ""
            for error in form.errors.as_data():
                for e in form.errors[error].as_data():
                    msg = msg + str(e)
            messages.info(request, msg)
    
        return redirect('idiomapub', id)

@user_passes_test(es_investigador)
def deleteidiomapub(request, id, id_idi):
    publicacion = Publicacion.objects.get(id=id)
    idioma = Idioma.objects.get(id=id_idi)
    
    #
    if (request.method == 'GET'):
        template = loader.get_template('publicaciones/deleteidiomapub.html')

        context = {
            'publicacion': publicacion,
            'idioma': idioma,
            'settings': settings,
        }
    
        return HttpResponse(template.render(context, request))
        
    elif (request.method == 'POST'):
        idiomapub = IdiomaPublicacion.objects.get(publicacion=publicacion, idioma=idioma)
        idiomapub.delete()

        return redirect('idiomapub', id)

@user_passes_test(es_investigador)
def updateidiomapub(request, id, id_idi):
    publicacion = Publicacion.objects.get(id=id)
    idioma = Idioma.objects.get(id=id_idi)
    idiomapub = IdiomaPublicacion.objects.get(publicacion_id=id, idioma_id=id_idi)
    
    if (request.method == 'GET'):
        # muestra el formulario con datos.
        form = IdiomaPublicacionForm(instance=idiomapub, publicacion=id)
        template = loader.get_template('publicaciones/addidiomapub.html')

        context = {
            'publicacion': publicacion,
            'idioma': idioma,
            'settings': settings,
            'form': form,
            'isadd': False,
        }
        
        return HttpResponse(template.render(context, request))
        
    elif (request.method == 'POST'):
        # actualiza datos.
        form = IdiomaPublicacionForm(request.POST, instance=idiomapub, publicacion=id)
        if form.is_valid():
            form.save()
        else:
            #FIXME
            msg = ""
            for error in form.errors.as_data():
                for e in form.errors[error].as_data():
                    msg = msg + str(e)
            messages.info(request, msg)

        return redirect('idiomapub', id)
        
