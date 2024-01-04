from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#En lugar de crear los views, se crea una clase que permite manejar los metodos 
#get y post para llevar la informacion de los usuarios que se registren a la base de datos
class Vista_registro(View):

    def get(self, request):#Funcion encargada de mostrar el formulario 
        form=UserCreationForm()
        return render(request, "autenticacion/registro.html", {"form":form})


    def post(self, request):
        pass
