from django import forms
from common.models import Producto, Bateria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

