from django.urls import path
from .views import tareas, salir
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(tareas), name='tareas'),
    path('<int:pk>/', login_required(tareas), name='tarea_detail'),
    path('<int:pk>/editar/', login_required(tareas), name='tarea_editar'),
    path('<int:pk>/eliminar/', login_required(tareas), name='tarea_eliminar'),
    path('salir/', salir, name='salir'),
]


