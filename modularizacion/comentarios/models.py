from django.db import models

# Clase comentario
class Comentario(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comentario = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.nombre
#Fin clase comentarios