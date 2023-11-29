from django.shortcuts import render, HttpResponse
#SE IMPORTAN LOS MODELOS DESDE MODELS A SER MOSTRADOS EN EL TEMPLATE, EN ESTE CASO LAS CATEGORIAS

# Create your views here.

#Se debe crear una vista por cada pagina del proyecto



def utiles(request):
    return render(request,"masutilapp/utiles.html")

def uniforme(request):
    return render(request,"masutilapp/uniformes.html")

def sobrenos(request):
    return render(request,"masutilapp/aboutUs.html")

def advertencia(request):
    return render(request,"masutilapp/advertencia.html")

def calificacion(request):
    return render(request,"masutilapp/calificacion.html")

def contacto(request):
    return render(request,"masutilapp/contact.html")

#def cuaderno(request):
#    return HttpResponse("Cuaderno")

def libros(request):
    return render(request,"masutilapp/libros.html")

def login(request):
    return render(request,"masutilapp/login.html")

def mensaje(request):
    return render(request,"masutilapp/mensaje.html")

def perfil(request):
    return render(request,"masutilapp/perfil.html")

def registro(request):
    return render(request,"masutilapp/registro.html")
