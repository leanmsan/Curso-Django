from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario

# Create your views here.
def test(request):
    return HttpResponse("Funciona Correctamente")

def create(request):
    #comment = Comentario(nombre="Leandro", score=5, comentario='Este es un comentario')
    #comment.save()
    comment = Comentario.objects.create(nombre="Leandro")
    return HttpResponse("ruta para probar la creacion de modelos")

def delete(request):
    #comment = Comentario.objects.get(id=1)
    #comment.delete()
    Comentario.objects.filter(id=2).delete()
    return HttpResponse("Borrar un comentario")
