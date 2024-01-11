from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage;
# Create your views here.
def contacto(request):
    formulario_contacto=formularioContacto;#SE INSTANCIA EL OBJETO FORMULARIO
    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST);#se cargan en el formulario la informacion introducida para rescatar de los cuadros de texto
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre");#se guaradn en variables los datos suministrados por el usuario
            email=request.POST.get("email");
            contenido=request.POST.get("contenido");
    

            email=EmailMessage("Mensaje desde Masutil app","El usuario con nombre {} con la direccion {} escribe lo siquiente: \n \n{}".format(nombre,email,contenido),
                               "",["micorreo@gmail.com"],reply_to=[email])
            
            #CON LO SIGUIENTE SE AVISA SI SE ENVIO EL MENSAJE O NO
            try:
                email.send()

                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")
          
            
        return redirect("/contacto/?valido") #CON ESTO SE REDIRIGE A LA PAGINA DE CONTACTO UNA VEZ SE HA HECHO LA PETICION POST, NO ANTES
    else:
        print("no util") 
    return render(request,"contacto/contact.html",{"miformulario":formulario_contacto})


