from django.shortcuts import render
from .forms import ProveedorForm

# Create your views here.
def index(request):
    form = ProveedorForm()
    return render(request, 'index.html', {'form': form})