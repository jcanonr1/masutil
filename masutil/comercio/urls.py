from django.urls import path
from . import views
#SE IMPORTAN PARA TENER ACCESO ALSETTINGS Y LOS ARCHIVOS MEDIA
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    path('perfil',views.perfil, name='Perfil'),
    path('perfil/Uniformes/<int:id_categoria_id>/', views.uniforme, name="Uniforme"),
    path('perfil/Uniformes/2/', views.uniforme, name="Uniforme2"),#linea provisional para que funcione carrito con id categoria =2
]
#permite acceso a media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)