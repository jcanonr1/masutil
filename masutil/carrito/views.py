from django.shortcuts import render, redirect # se redirige a la pagina para que refleje los cambios hechos en el carro

# Create your views here.
from .carrito import carrito #se importa la clase carrito
from comercio.models import publicaciones, productos # se imortan las publicaciones de usuarios

def agregar_producto(request, producto_id):
    carro=carrito(request)#variable de tipo carrito
    producto=publicaciones.objects.get(id_producto=producto_id);# se obtiene el producto a llevar al carro
    carro.agregar(publicaciones=producto);# se usa el metodo de la clase carrito

    category=productos.id_categoria
    #la idea es obtener el id categoria del producto y usar if para saber a donde redireccionar
    return redirect("Uniforme2")

def elimiar_producto(request, producto_id):
    carro=carrito(request)
    producto=publicaciones.objects.get(id_producto=producto_id);
    carro.eliminar(producto=producto);
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro=carrito(request)
    producto=publicaciones.objects.get(id_producto=producto_id);
    carro.restar_carro(publicaciones=producto);
    return redirect("Uniforme2")

def limpiar_carrito(request, producto_id):
    carro=carrito(request)
    carro.limpiar_carro();
    return redirect("tienda")