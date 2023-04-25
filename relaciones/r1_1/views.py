from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create (request):
    #Creando los elementos
    place = Place(name="Lugar 1", address="Calle Demo")
    place.save()

    restaurant = Restaurant(place = place, number_of_employees = 3)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
