from django.urls import path

from . import views
#SE IMPORTA EL ARCHIVO SETTINGS PARA TENER A DISPOSICION MEDIA_URL Y MEDIA_ROOT
from django.conf import settings
#TAMBIEN SE DEBEN IMPORTAR LOS ARCHIVOS STATIC
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    
   
]
#permite acceso a media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)