from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache

@login_required
@never_cache
def tareas(request, pk=None):
    form = None
    tarea_detail = None
    confirm_delete = None
    today = datetime.today().date()

    if pk:
        if 'editar' in request.path:
            tarea = get_object_or_404(Tarea, pk=pk)
            if request.method == 'POST':
                form = TareaForm(request.POST, instance=tarea)
                if form.is_valid():
                    form.save()
                    return redirect('tareas')
            else:
                form = TareaForm(instance=tarea)
                tarea_detail = tarea
        elif 'eliminar' in request.path:
            confirm_delete = get_object_or_404(Tarea, pk=pk)
            if request.method == 'POST':
                confirm_delete.delete()
                return redirect('tareas')
        else:
            tarea_detail = get_object_or_404(Tarea, pk=pk)
    else:
        if request.method == 'POST':
            form = TareaForm(request.POST)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.usuario = request.user
                tarea.save()
                return redirect('tareas')
        else:
            form = TareaForm()

    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'appTareas/tareas.html', {
        'form': form,
        'tareas': tareas,
        'tarea_detail': tarea_detail,
        'confirm_delete': confirm_delete,
        'today': today,
    })

def salir(request):
    logout(request)
    return redirect('/')
