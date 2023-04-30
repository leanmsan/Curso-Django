from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentarioFrom, ContactForm

def form(request):
    comentario_form = ComentarioFrom({'name': 'Leandro', 'url': 'http://www.instagram.com', 'comentario': 'Comentario'})
    return render(request, 'form.html', {'comentario_form': comentario_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse("Metodo no permitido")
    
    return HttpResponse(request.POST['name'])

def widget (request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valido")
        else:
            return render(request, 'widget.html', {'form': form})