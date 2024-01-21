from django.shortcuts import render, redirect   
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

# Create your views here.

#En lugar de crear los views, se crea una clase que permite manejar los metodos 
#get y post para llevar la informacion de los usuarios que se registren a la base de datos
class formulario_registro(UserCreationForm):
    email= forms.EmailField(required=True, help_text="Requerido, debe ser un email valido")
    first_name= forms.CharField(required=False)
    last_name= forms.CharField(required=False)

    class Meta:
        model = User
        fields=("first_name","last_name","username","email","password1","password2")

     
class Vista_registro(View):

    def get(self, request):#Funcion encargada de mostrar el formulario 
        form=formulario_registro()
        return render(request, "autenticacion/registro.html", {"form":form})


    def post(self, request):# metodo encargado del envio de la informacion
        form=formulario_registro(request.POST)#Trae la informacion presente en el formulario
        
        if form.is_valid():
        
            usuario=form.save()#guarda directamente la informacion en la base de datos
            login(request, usuario)# Permite hacer el login del usuario

            return redirect("Inicio")
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg]);
            return render(request, "autenticacion/registro.html", {"form":form})
        
def cerrarSesion(request):
    logout(request)
    return redirect("Inicio")

def loguear(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)#Se obtienen los datos introducidos por el usuario
        if form.is_valid():
            #Se obtienen los datos introduciodos en cada cuadro de texto
            nombreUsuario=form.cleaned_data.get("username");
            contrasenia=form.cleaned_data.get("password");
            usuario=authenticate(username=nombreUsuario, password=contrasenia);#De esta manera se comprueba si los datos ingresados corresponden a los que estan en la base de datos
            # Si el usuario existe se realiza el loguin y se lleva a inicio
            if usuario is not None:
                login(request, usuario);
                return redirect("Inicio")
            else:
                messages.error(request, "Usuario no valido");
        else:
            messages.error(request, "Informacion incorrecta");
    form=AuthenticationForm;
    #messages.error(request, "algo aml");
    return render(request, "autenticacion/loguin.html", {"form":form})