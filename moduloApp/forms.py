from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from moduloApp.models import *


class TipoProductoForm(forms.Form):
    tipoProducto = forms.CharField()
    descripcionTipoProducto = forms.CharField()


class ProductoForm(forms.Form):
    nombreProducto = forms.CharField(label="Nombre del producto")
    cantidad = forms.IntegerField(label="Cantidad de producto")
    descripcionProducto = forms.CharField(label="Descripción del producto")


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    nombreProducto = forms.CharField(label="Nombre del producto")
    cantidad = forms.IntegerField(label="Cantidad de producto")
    descripcionProducto = forms.CharField(label="Descripción del producto")





class BodegaForm(forms.Form):
    nombreBodega = forms.CharField()
    direccionBodega = forms.CharField()
    
class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

    nombreBodega = forms.CharField(label="Nombre de bodega")
    direccionBodega = forms.CharField(label="Dirección de bodega")


class ProductoBodegaForm(forms.Form):
    stock = forms.IntegerField()
