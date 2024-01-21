from django.db import models
from servicios.models import categoria
from django.contrib.auth.models import User
# Create your models here.

class usuarios(models.Model):
    id_usuario=models.AutoField(primary_key=True);
    nombre=models.CharField(max_length=50, null=False);
    documento=models.IntegerField(null=False,unique=True);
    email=models.EmailField(null=False, max_length=30);
    username=models.CharField(max_length=50);
    password=models.CharField(max_length=50,null=False);

    class Meta:
        verbose_name='comprador'
        verbose_name_plural='compradores'

    def __str__(self):
        return self.documento;

class productos(models.Model):
    id_producto=models.AutoField(primary_key=True);
    id_categoria=models.ForeignKey(categoria, on_delete=models.CASCADE);
    nombre_producto=models.CharField(max_length=70);
    valor=models.IntegerField();
    descripcion=models.CharField(max_length=50);
    imagen=models.ImageField(upload_to='comercio');#CREA SUBCARPETA DENTRO DE MEDIA DONDE SE GUARDAN LAS IMAGENES, MEDIA SE CONFIGURA EN SETTINGS
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre_producto;

class facturaVenta(models.Model):
    id_factura=models.AutoField(primary_key=True);
    id_usuario=models.ForeignKey(User, on_delete=models.CASCADE);
    orderDate=models.DateTimeField(auto_now_add=True);
    valor=models.IntegerField();
    descripcion=models.CharField(max_length=100)
    medioDePago=models.CharField(max_length=50, null=True);

class publicaciones(models.Model):
    id_publicacion=models.AutoField(primary_key=True);
    id_usuario=models.ForeignKey(User,on_delete=models.CASCADE);
    id_producto=models.ForeignKey(productos, on_delete=models.CASCADE);
    fecha_publicacion=models.DateTimeField(auto_now=True);

class ventas(models.Model):
    id_venta=models.AutoField(primary_key=True);
    id_producto=models.ForeignKey(productos, on_delete=models.CASCADE);
    id_factura=models.ForeignKey(facturaVenta, on_delete=models.CASCADE);
    
    
class retroalimentacion(models.Model):
    id_retroalimentacion=models.AutoField(primary_key=True);
    id_usuario=models.ForeignKey(User, on_delete=models.CASCADE);
    id_publicacion=models.ForeignKey(publicaciones, on_delete=models.CASCADE);
    puntaje=models.IntegerField();
    descripcion=models.CharField(max_length=50);

class conversaciones(models.Model):
    id_conversacion=models.AutoField(primary_key=True);
    fecha=models.DateTimeField(auto_now=True);
    contenido=models.CharField(max_length=200);

class miembros_conversacion(models.Model):
    id_miembros=models.AutoField(primary_key=True);
    id_usuario=models.ForeignKey(User, on_delete=models.CASCADE);
    id_conversacion=models.ForeignKey(conversaciones, on_delete=models.CASCADE);

