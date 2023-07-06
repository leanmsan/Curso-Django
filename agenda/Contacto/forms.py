from django.forms import ModelForm
from .models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        models = Contacto
        fields = '__all__'