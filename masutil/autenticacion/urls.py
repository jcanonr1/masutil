from django.urls import path

from .views import Vista_registro, cerrarSesion, loguear

app_name="autenticacion"
urlpatterns = [
   
    #COMO ES LAPRIMERA VISTA DE LA APP, LA RUTA VA DESDE LA RAIZ
    path('', Vista_registro.as_view(), name="Auth"),
    path('cerrar_sesion', cerrarSesion, name="cerrar_sesion"),
    path('loguear', loguear, name="loguear"),
]