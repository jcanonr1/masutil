from django.contrib import admin
from .models import categoria
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    #SE ESPECIFICA QUE LOS CAMPO SON DE SOLO LECTURA
    readonly_fields=('created','updated')

admin.site.register(categoria,categoriaAdmin)