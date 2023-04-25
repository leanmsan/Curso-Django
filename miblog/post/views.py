from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

# Create your views here.
def queries(request):
    #Obtener todos los elementos
    authors = Author.objects.all()

    #Obtener los datos filtrados por condicion
    filtered = Author.objects.filter(email="sandra55@example.net")

    #Obtener un unico objeto
    author = Author.objects.get(id=1)

    #Obtener una deterninada cantidad de registros
    limits = Author.objects.all()[:10]

    #Obtener una cantidad determinada de registros desde un determinado punto
    offsets = Author.objects.all()[5:10]

    #Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    #Obtener todos los elementos cuyo id sea <= 15
    filtered = Author.objects.filter(id__lte=15)

    #Obtener todos los autores que contienen en su nombre la palabra yes
    filtered = Author.objects.filter(name__contains='yes')

    return render(request, 'post/queries.html', {'authors':authors, 'filtered':filtered, 'author':author, 'limits':limits, 'offsets':offsets, 'orders':orders})
#Fin clase queries

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Leandro"
    author.email = "leanmsan@gmail.com"
    author.save()
    
    return HttpResponse("Modificado")
    #return render(request, 'post/update.html', {})
