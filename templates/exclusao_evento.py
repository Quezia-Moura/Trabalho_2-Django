from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required

@login_required
def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if evento.criador != request.user:
        return redirect('pagina_inicial')
    if request.method == "POST":
        evento.delete()
        return redirect('pagina_inicial')
    return render(request, 'excluir_evento.html', {'evento': evento})
