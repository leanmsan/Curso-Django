from django.shortcuts import render
from .forms import ProductoForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'productos.html', {'form': form})
    else:
        form = ProductoForm()
        return render(request, 'productos.html', {'form': form})
