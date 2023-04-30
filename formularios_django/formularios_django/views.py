from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentarioFrom

def form(request):
    comentario_form = ComentarioFrom({'name': 'Leandro', 'url': 'http://www.instagram.com', 'comentario': 'Comentario'})
    return render(request, 'form.html', {'comentario_form': comentario_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse("Metodo no permitido")
    
    return HttpResponse(request.POST['name'])