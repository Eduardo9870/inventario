from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from moduloApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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



class TiendaForm(forms.Form):
    nombreTienda = forms.CharField(label="Nombre de la bodega" ,widget=forms.TextInput(attrs={"class": "form-control"}))
    direccionTienda = forms.CharField(label="Dirección de la bodega" ,widget=forms.TextInput(attrs={"class": "form-control"}))


class TiendaModelForm(ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'
        widgets = {
            'nombreTienda': forms.TextInput(attrs={"class": "form-control"}),
            'direccionTienda': forms.TextInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    pass 



class DevolucionForm(forms.Form):
    nombreDevolucion = forms.CharField(label="Nombre del producto", widget=forms.TextInput(attrs={"class": "form-control"}))
    cantidadDevolucion = forms.IntegerField(label="Cantidad de producto", widget=forms.NumberInput(attrs={"class": "form-control"}))
    precioDevolucion = forms.IntegerField(label=" Precio de compra realizada ", widget=forms.NumberInput(attrs={"class": "form-control"}))
    motivoDevolucion = forms.CharField(label="Motivo de devolución", widget=forms.Textarea(attrs={"class": "form-control"}))


class DevolucionModelForm(ModelForm):
    class Meta:
        model = Devolucion
        fields = '__all__'
        widgets = {
            'nombreDevolucion': forms.TextInput(attrs={"class": "form-control"}),
            'cantidadDevolucion': forms.NumberInput(attrs={"class": "form-control"}),
            'precioDevolucion': forms.NumberInput(attrs={"class": "form-control"}),
            'motivoDevolucion': forms.Textarea(attrs={"class": "form-control"}),
        }