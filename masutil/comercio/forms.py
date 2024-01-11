from django import forms

from .models import productos

class nproductoForm(forms.ModelForm):

    class Meta:
        model = productos;
        
        fields = ('id_producto','nombre_producto','id_categoria','valor','descripcion','imagen');
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)#Trae las categorias disponibles desde la BBDD
        self.fields['nombre_producto'].required=False;
        self.fields['valor'].required=False;
        self.fields['descripcion'].required=False;
        self.fields['imagen'].required=False;
        
        self.fields['id_categoria'].widget.attrs.update({
            'class': 'form-select'
        })
      
    
        
    