from django.shortcuts import render
from .models import Evento
from django.utils import timezone

def pagina_inicial(request):
    eventos_futuros = Evento.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')
    return render(request, 'pagina_inicial.html', {'eventos_futuros': eventos_futuros})
