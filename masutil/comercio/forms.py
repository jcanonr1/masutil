from django import forms

from .models import productos, retroalimentacion

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
      

class edicionForm(forms.ModelForm):

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


class new_calificationForm(forms.Form):
    opciones = (
         ("1","uno"),
         ("2","dos"),
         ("3","tres"),
         ("4","cuatro"),
         ("5","cinco"),
     )
    puntaje = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=opciones, )
                                           
    descripcion=forms.CharField(label="Descripcon",required=True, max_length=750,widget=forms.Textarea);
    