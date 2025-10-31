from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil
from .forms import PerfilForm

def perfil(request):
    user = Perfil.objects.get(request.POST)
    return render(request, "account/exibir_perifl.html", {"perfil": user})

def editar_perfil(request):
    perf = request.user.perfil
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perf)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm()
    return render(request, "account/editar_perfil.html", {"forn" : form})