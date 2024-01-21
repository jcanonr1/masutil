from django.shortcuts import render, redirect
from comercio.models import publicaciones, productos, User, facturaVenta, ventas, retroalimentacion
from carrito.carrito import carrito
from django.contrib import messages
from .forms import nproductoForm, new_calificationForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

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


        
def calificacion(request, publicacion_id):
    formulario_calificacion=new_calificationForm;#SE INSTANCIA EL OBJETO FORMULARIO
    if request.method=="POST":
        formulario_calificacion=new_calificationForm(data=request.POST);#se cargan en el formulario la informacion introducida para rescatar de los cuadros de texto
        if formulario_calificacion.is_valid():
            puntaje=request.POST.get("puntaje");#se guaradn en variables los datos suministrados por el usuario
            descripcion=request.POST.get("descripcion");
            calificar=retroalimentacion(id_usuario=request.user,id_publicacion=publicacion_id,puntaje=puntaje,descripcion=descripcion);
            calificar.save()
    return render(request,"comercio/calificacion.html",{"calificacion":formulario_calificacion})





def uniforme(request,id_categoria_id):
    
    #uniforme=productos.objects.filter(id_categoria=id_categoria_id);#SE FILTRA POR CATEGORIA CUANDO USUARIO HACE CLIC EN ENLACE
    
    publicacion=publicaciones.objects.filter(id_producto__id_categoria=id_categoria_id);# SE MUESTRAN LAS PUBLICACIONES ASOCIADAS A LA CATEGORIA ANTERIOR
   
    return render(request,"comercio/uniformes.html",{"uniformes":uniforme,"publicacion":publicacion})#EN EL RENDERIZADO SE MUESTRAN LOS PRODUCTO CORRESPONDIENTES A LA CATGERIA FILTRADA 

def procesar_factura(request):
    #factura=facturaVenta.objects.create(id_usuario=request.user,valor=23)#Se almacena lo que ha pedido el cliente
    carro=carrito(request)
    productosFactura=list()
    for key, value in carro.carro.items():
        productosFactura.append(facturaVenta(
            id_usuario=request.user,
            #cantidad=value["cantidad"],
            valor=value["precio"],
            descripcion=str(value["cantidad"])+" "+value["nombre"],
            medioDePago="No aplica por ahora",
            #factura=factura

        ))
        usuario=value["usuario"]
        correo=value["correo"]
        producto_actual=value["producto_id"];
        publicacion=value["publicacion_id"];
    print(publicacion)
    
    #con este metodo se inserta en la base de datos es como tener muchos insert into
    ultimas_facturas=facturaVenta.objects.bulk_create(productosFactura)
    for ultimo in ultimas_facturas:
        idfactura=ultimo.id_factura
    
    
        print(facturaVenta.id_factura)
        venta=ventas(id_producto_id=producto_actual,id_factura_id=idfactura)
        venta.save();

#Se debe revisar el envio del mail cuando se corrija para que le llegue a todos los vendedores
    #enviar_mail(
    #    #factura=factura,
    #    productosFactura=productosFactura,
    #    comprador=request.user.username,
    #    email_comprador=request.user.email,
    #    vendedor=usuario,
    #    email_vendedor=correo
    #    )
#
    #messages.success(request, "El pedido se ha creado correctamente")
    return redirect("Calificar",publicacion)

def enviar_mail(**kwargs):# De esta manera a funcion esta preparada para recibir una cantidad indetermindada de argumentos
    asunto=" Reserva completada",
    mensaje=render_to_string("emails/facturas.html",{
        #"factura":kwargs.get("factura"),
        "productosFactura":kwargs.get("productosFactura"),
        "nombreusuario":kwargs.get("comprador"),
        
    })

    mensaje_texto=strip_tags(mensaje)#De esta manera se omiten etiquetas de html
    from_email=kwargs.get("email_comprador");
    to=kwargs.get("email_vendedor");
     
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)