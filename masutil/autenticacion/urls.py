from django.urls import path

from .views import Vista_registro

app_name="autenticacion"
urlpatterns = [
   
    #COMO ES LAPRIMERA VISTA DE LA APP, LA RUTA VA DESDE LA RAIZ
    path('', Vista_registro.as_view(), name="Auth"),
]