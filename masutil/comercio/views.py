from django.shortcuts import render
from comercio.models import publicaciones
from comercio.models import productos
# Create your views here.

#SE ESPERA QUE EN LA VISTA PERFIL APAREZCAN LOS PRODUCTOS CARGADOS POR EL USUSARIO
def perfil(request):
    publicacion=publicaciones.objects.all()
    return render(request,"comercio/perfil.html",{"publicacion":publicacion})

def calificacion(request):
    return render(request,"comercio/calificacion.html");

def uniforme(request,id_categoria_id):
    uniforme=productos.objects.get(id_producto=id_categoria_id);#SE FILTRA POR CATEGORIA CUANDO USUARIO HACE CLIC EN ENLACE
    publicacion=publicaciones.objects.filter(id_producto=uniforme);# SE MUESTRAN LAS PUBLICACIONES ASOCIADAS A LA CATEGORIA ANTERIOR
    return render(request,"comercio/uniformes.html",{"uniformes":uniforme,"publicacion":publicacion})#EN EL RENDERIZADO SE MUESTRAN LOS PRODUCTO CORRESPONDIENTES A LA CATGERIA FILTRADA 