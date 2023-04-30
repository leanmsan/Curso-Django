from django import forms

class ComentarioFrom(forms.Form):
    name = forms.CharField(label='Escribe tu nombre', max_length=100, help_text='100 caracteres maximo')
    url = forms.URLField(label='Tu sitio Web', required=False, initial='http://')
    comentario = forms.CharField()
