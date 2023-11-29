from django.urls import path

from masutilapp import views
#SE IMPORTA EL ARCHIVO SETTINGS PARA TENER A DISPOSICION MEDIA_URL Y MEDIA_ROOT
from django.conf import settings
#TAMBIEN SE DEBEN IMPORTAR LOS ARCHIVOS STATIC
from django.conf.urls.static import static

urlpatterns = [
   
    path('utiles/', views.utiles, name="Utiles"),
    path('uniforme/', views.uniforme, name="Uniforme"),
    path('sobrenos/', views.sobrenos, name="Sobre nosotros"),
    path('advertencia/', views.advertencia, name="Advertencia"),
    path('calificacion/', views.calificacion, name="Calificacion"),
    path('contacto/', views.contacto, name="Contacto"),
    path('libros/', views.libros, name="Libros"),
    path('login/', views.login, name="Login"),
    path('mensaje/', views.mensaje, name="Mensaje"),
    path('perfil/', views.perfil, name="Perfil"),
    path('registro/', views.registro, name="Registro"),
]
#SE AÑADE UNA NUEVA URL PARA VISUALIZAR LA IMAGEN DE LA CATEGORIA, LOS ELEMENTOS MEDIA_ SE ENCUENTRAN EN SETTINGS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)