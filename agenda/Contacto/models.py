from django.db import models
from datetime import date

class Contacto(models.Model):
    Nombre = models.CharField(max_length=50, blank=False, null=False)
    Apellido = models.CharField(max_length=60, blank=True, null=True)
    Telefono = models.CharField(max_length=12, blank=False, null=False)
    Email = models.EmailField()
    FechaInclusion = models.DateField(default=date.today)
    Notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Nombre

