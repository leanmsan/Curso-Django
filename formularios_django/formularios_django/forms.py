from django import forms

class ComentarioFrom(forms.Form):
    name = forms.CharField()
    url = forms.URLField(label='Tu sitio Web', required=False, initial='http://')
    comentario = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre: ', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != 'Open':
            raise forms.ValidationError("Solo el valor Open esta permitido en este campo")
        else:
            return name