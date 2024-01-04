from django.urls import path

from . import views


urlpatterns = [
   
    #COMO ES LAPRIMERA VISTA DE LA APP, LA RUTA VA DESDE LA RAIZ
    path('', views.contacto, name="Contacto"),
]