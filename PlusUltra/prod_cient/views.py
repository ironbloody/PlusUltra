from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.urls import reverse
import json
from django.db.models import Count
from django.db.models.functions import TruncYear
from app.models import Publicacion, Revista

# home page.
def home(request):
    # variable de session num_visitas.
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1
    
    # default template.
    template = loader.get_template('home.html')
    context = {
        'settings': settings,
        'dataarticulos': None,
        'num_visitas': num_visitas,
    }
    
    # está autenticado?
    if (request.user.is_authenticated):
        
        # es superusuario?
        if (request.user.is_superuser):
            return HttpResponseRedirect('admin/')

        # pertene a cierto grupo?
        if (len(request.user.groups.all()) > 0):
            # revisar el grupo (el primero).
            grupo = request.user.groups.all()[0]
            
            # cambia el template.
            if (grupo.name == "Investigador"):
                template = loader.get_template('publicaciones/dashboard.html')
                
                # gráfico publicaciones del usuario investigador autenticado.
                publicaciones = Publicacion.objects.filter(investigador=request.user)
                
                # agrupa número de publicaciones por el año.
                result = (publicaciones
                    .annotate(anio=TruncYear('fecha'))
                    .values('anio')
                    .annotate(dcount=Count('anio'))
                    .order_by()
                )
                
                # copia a un diccionario el rsultado.
                dataarticulos = []
                for item in result:
                    dataarticulos.append({'x': item["anio"].year, 'y': item["dcount"]})
                
                context['dataarticulos'] = json.dumps(dataarticulos)
                
                # gráfico revistas.
                result = (publicaciones
                    .values('revista_id')
                    .annotate(dcount=Count('revista_id'))
                    .order_by()
                )
                
                datarevistas = []
                for item in result:
                    obj_rev = Revista.objects.filter(id=item["revista_id"]).values()[0]
                    datarevistas.append({'label': obj_rev["nombre"], 'y': item["dcount"]})
                
                context['datarevistas'] = json.dumps(datarevistas)
            else:
                # otros grupos.
                pass
        else:
            # usuario sin grupo.
            pass
    else:
        # usuario no autenticado.
        pass

    return HttpResponse(template.render(context, request))
