from django.shortcuts import render
from servicios.models import categoria   #se importa desde la app servicios

# Create your views here.
def inicio(request):

    categorias=categoria.objects.all() #Se importan todas las catgeroias creadas 
    return render(request,"servicios/index.html",{"categorias":categorias})
