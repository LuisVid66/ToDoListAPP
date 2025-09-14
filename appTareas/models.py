from django.db import models
from django.conf import settings

class Tarea(models.Model):
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    hora_vencimiento = models.TimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.descripcion)


