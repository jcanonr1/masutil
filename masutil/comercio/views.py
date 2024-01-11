from django.shortcuts import render, redirect
from comercio.models import publicaciones, productos, User

from .forms import nproductoForm
# Create your views here.

#SE ESPERA QUE EN LA VISTA PERFIL APAREZCAN LOS PRODUCTOS CARGADOS POR EL USUSARIO
def perfil(request,usuario_id):#Se traen todas las publicaciones hechas por el usuario autenticado
    publicacion=publicaciones.objects.filter(id_usuario_id=usuario_id)
    return render(request,"comercio/perfil.html",{"publicacion":publicacion})

def n_producto(request,usuario_id):
    productoNuevo=nproductoForm;
    user = User.objects.get(id=usuario_id)
    print(user.id)
    if request.method=="POST":
        productoNuevo=nproductoForm(request.POST, request.FILES)
        #print("entro al post")
        if productoNuevo.is_valid():            
            productoNuevo.save();
            producto=productos.objects.last()
            idproducto=producto.id_producto
            publicacion=publicaciones(id_usuario_id=user.id,id_producto_id=idproducto)
            publicacion.save()
            #print("conseguido")
            return redirect("Perfil", usuario_id)
        else:
            #print("rechazado")
            for field in productoNuevo:
                print("Field Error:", field.name,  field.errors)
            return render(request,"comercio/nuevos_productos.html",{"prodnuevo":productoNuevo})
            
    else:
        pass
        #print("no utl")
    return render(request,"comercio/nuevos_productos.html",{"prodnuevo":productoNuevo})


        
def calificacion(request):
    return render(request,"comercio/calificacion.html");

def uniforme(request,id_categoria_id):
    
    #uniforme=productos.objects.filter(id_categoria=id_categoria_id);#SE FILTRA POR CATEGORIA CUANDO USUARIO HACE CLIC EN ENLACE
    
    publicacion=publicaciones.objects.filter(id_producto__id_categoria=id_categoria_id);# SE MUESTRAN LAS PUBLICACIONES ASOCIADAS A LA CATEGORIA ANTERIOR
   
    return render(request,"comercio/uniformes.html",{"uniformes":uniforme,"publicacion":publicacion})#EN EL RENDERIZADO SE MUESTRAN LOS PRODUCTO CORRESPONDIENTES A LA CATGERIA FILTRADA 