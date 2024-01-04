from django import forms

class formularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True, max_length=75);
    email=forms.EmailField(label="email",required=True, max_length=75);
    contenido=forms.CharField(label="Contenido",required=True, max_length=750,widget=forms.Textarea);
