from django.urls import path
from . import views
#SE IMPORTAN PARA TENER ACCESO ALSETTINGS Y LOS ARCHIVOS MEDIA
from django.conf import settings
from django.conf.urls.static import static

app_name="carrito"

urlpatterns=[

    path('agregar/<int:producto_id>/',views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/',views.elimiar_producto, name='eliminar'),
    path('restar/<int:producto_id>/',views.restar_producto, name='restar'),
    path('limpiar/',views.limpiar_carrito, name='limpiar'),
]
#permite acceso a media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)