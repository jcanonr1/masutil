from django.db import models
from servicios.models import categoria
from django.contrib.auth.models import User
# Create your models here.

class compradores(models.Model):
    id_comprador=models.AutoField(primary_key=True);
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

class vendedores(models.Model):
    id_vendedor=models.AutoField(primary_key=True);
    nombre=models.CharField(max_length=50, null=False);
    documento=models.IntegerField(null=False,unique=True);
    email=models.EmailField(null=False, max_length=30);
    username=models.CharField(max_length=50);
    password=models.CharField(max_length=50,null=False);

    class Meta:
        verbose_name='vendedor'
        verbose_name_plural='vendedores'

    def __str__(self):
        return self.documento;

class facturaVenta(models.Model):
    id_factura=models.AutoField(primary_key=True);
    id_comprador=models.ForeignKey(compradores, on_delete=models.CASCADE);
    orderDate=models.DateTimeField(auto_now_add=True);
    descripcion=models.CharField(max_length=100)

class ordenPedido(models.Model):
    id_ordenPedido=models.AutoField(primary_key=True);
    id_vendedor=models.ForeignKey(vendedores, on_delete=models.CASCADE);
    valor=models.IntegerField();
    medioDePago=models.CharField(max_length=50);

class productos(models.Model):
    id_producto=models.IntegerField(primary_key=True);
    id_categoria=models.ForeignKey(categoria, on_delete=models.CASCADE);
    id_factura=models.ForeignKey(facturaVenta, on_delete=models.CASCADE);
    id_ordenPedido=models.ForeignKey(ordenPedido, on_delete=models.CASCADE);
    autor=models.ForeignKey(User, on_delete=models.CASCADE);
    valor=models.IntegerField();
    descripcion=models.CharField(max_length=50);
    imagen=models.ImageField(upload_to='comercio');
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.descripcion;

class retroalimentacion(models.Model):
    id_retroalimentacion=models.IntegerField(primary_key=True);
    id_vendedor=models.ForeignKey(vendedores, on_delete=models.CASCADE);
    id_comprador=models.ForeignKey(compradores, on_delete=models.CASCADE);
    puntaje=models.IntegerField();
    descripcion=models.CharField(max_length=50);