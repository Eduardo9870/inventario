from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from moduloApp.models import *


class TipoProductoForm(forms.Form):
    tipoProducto = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    descripcionTipoProducto = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))


class ProductoForm(forms.Form):
    nombreProducto = forms.CharField(label="Nombre del producto", widget=forms.TextInput(attrs={"class": "form-control"}))
    cantidad = forms.IntegerField(label="Cantidad de producto", widget=forms.NumberInput(attrs={"class": "form-control"}))
    descripcionProducto = forms.CharField(label="Descripción del producto", widget=forms.Textarea(attrs={"class": "form-control"}))


class ProductoModelForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombreProducto': forms.TextInput(attrs={"class": "form-control"}),
            'cantidad': forms.NumberInput(attrs={"class": "form-control"}),
            'descripcionProducto': forms.Textarea(attrs={"class": "form-control"}),
        }


class BodegaForm(forms.Form):
    nombreBodega = forms.CharField(label="Nombre de la bodega" ,widget=forms.TextInput(attrs={"class": "form-control"}))
    direccionBodega = forms.CharField(label="Dirección de la bodega" ,widget=forms.TextInput(attrs={"class": "form-control"}))


class BodegaModelForm(ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'
        widgets = {
            'nombreBodega': forms.TextInput(attrs={"class": "form-control"}),
            'direccionBodega': forms.TextInput(attrs={"class": "form-control"}),
        }


class ProductoBodegaForm(forms.Form):
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))


class categoriaForm(forms.Form):
    nombreCategoria = forms.CharField(label="nombreCategoria", widget=forms.TextInput(attrs={"class": "form-control"}))
    descripcion = forms.CharField(label="Descripción ", widget=forms.Textarea(attrs={"class": "form-control"}))


class categoriaModelForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombreCategoria': forms.TextInput(attrs={"class": "form-control"}),
            'descripcion': forms.Textarea(attrs={"class": "form-control"}),
        }

class Entrada_ProductoForm(forms.Form):
    fecha_entrada = forms.CharField(label="Nombre del producto", widget=forms.TextInput(attrs={"class": "form-control"}))
    descripcion_entrada = forms.IntegerField(label="Cantidad de producto", widget=forms.NumberInput(attrs={"class": "form-control"}))



class Entrada_ProductoModelForm(ModelForm):
    class Meta:
        model = Entrada_Producto
        fields = '__all__'
        widgets = {
            'fecha_entrada': forms.TextInput(attrs={"class": "form-control"}),
            'descripcion_entrada': forms.NumberInput(attrs={"class": "form-control"}),
 
        }