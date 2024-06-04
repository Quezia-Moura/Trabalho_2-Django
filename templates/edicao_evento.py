from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventoForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if evento.criador != request.user:
        return redirect('pagina_inicial')
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form})
