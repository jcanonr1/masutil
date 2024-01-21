from django.contrib import admin
from .models import productos, publicaciones, ventas, facturaVenta
from servicios.models import categoria

# Register your models here.

#REGISTAR EN EL ADMINISTRADOR
class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


#admin.site.register(categoria,categoriaAdmin);
admin.site.register(productos);
admin.site.register(publicaciones);
admin.site.register(ventas);
admin.site.register(facturaVenta);