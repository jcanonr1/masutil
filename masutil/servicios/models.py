from django.db import models

# Create your models here.

class categoria(models.Model):
    id_categoria=models.AutoField(primary_key=True);
    name=models.CharField(max_length=30,null=True);
    descripcion=models.CharField(max_length=50);
    imagen=models.ImageField(upload_to='categoria');
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.descripcion;
        
