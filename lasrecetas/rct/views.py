from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from rct.models import Receta

def index(request):
    receta = Receta.objects.all()
    return render_to_response('rct/index.html',
                              {'receta': receta})

def receta_detalle(request, receta_id):
    receta = get_object_or_404(Receta, pk=receta_id)
    return render_to_response('rct/receta_detalle.html',
                              {'receta' : receta})
