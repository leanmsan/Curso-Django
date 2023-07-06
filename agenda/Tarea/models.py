from django.db import models
from datetime import date

class Tarea(models.Model):
    Titulo = models.CharField(max_length=100, blank=False, null=False)
    Descripcion = models.TextField(blank=True, null=True)
    FechaInicio = models.DateField(default=date.today)
    FechaFinalizacion = models.DateField(blank=True, null=True)
    Prioridad = models.IntegerField(default=3)
    
    def __str__(self):
        return self.Titulo
