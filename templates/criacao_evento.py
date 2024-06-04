from django.shortcuts import render, redirect
from .forms import EventoForm
from django.contrib.auth.decorators import login_required

@login_required
def criar_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user
            evento.save()
            return redirect('pagina_inicial')
    else:
        form = EventoForm()
    return render(request, 'criar_evento.html', {'form': form})
