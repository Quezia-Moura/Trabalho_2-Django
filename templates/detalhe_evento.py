from django.shortcuts import render, get_object_or_404
from .models import Evento

def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'detalhe_evento.html', {'evento': evento})
