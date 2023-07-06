from django import forms
from django.forms import ModelForm
from moduloApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from moduloApp.models import *
from django.forms import ModelForm, TextInput, DateInput, Textarea

class CategoriaForm (forms.Form):
    nombreCategoria = forms.CharField(label="Nombre de la categoría", widget=forms.TextInput(attrs={"class": "form-control"}))
    descripcionCategoria = forms.CharField(label="Descripción de la categoría" ,widget=forms.Textarea(attrs={"class": "form-control"}))

class CategoriaModelForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombreCategoria': forms.TextInput(attrs={"class": "form-control"}),
            'descripcionCategoria': forms.Textarea(attrs={"class": "form-control"}),
        }

    


class ProductoForm(forms.Form):
    nombreProducto = forms.CharField(
        label="Nombre del producto", widget=forms.TextInput(attrs={"class": "form-control"}))
    cantidad = forms.IntegerField(label="Cantidad de producto", widget=forms.NumberInput(
        attrs={"class": "form-control"}))
    descripcionProducto = forms.CharField(
        label="Descripción del producto", widget=forms.Textarea(attrs={"class": "form-control"}))


class ProductoModelForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombreProducto': forms.TextInput(attrs={"class": "form-control"}),
            'cantidad': forms.NumberInput(attrs={"class": "form-control"}),
            'precio': forms.TextInput(attrs={"class": "form-control"}),
            'descripcionProducto': forms.Textarea(attrs={"class": "form-control"}),
        }


class BodegaForm(forms.Form):
    nombreBodega = forms.CharField(
        label="Nombre de la bodega", widget=forms.TextInput(attrs={"class": "form-control"}))
    direccionBodega = forms.CharField(
        label="Dirección de la bodega", widget=forms.TextInput(attrs={"class": "form-control"}))


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
    nombreTienda = forms.CharField(
        label="Nombre de la bodega", widget=forms.TextInput(attrs={"class": "form-control"}))
    direccionTienda = forms.CharField(
        label="Dirección de la bodega", widget=forms.TextInput(attrs={"class": "form-control"}))


class TiendaModelForm(ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'
        widgets = {
            'nombreTienda': forms.TextInput(attrs={"class": "form-control"}),
            'direccionTienda': forms.TextInput(attrs={"class": "form-control"}),
        }


class DevolucionForm(forms.Form):
    nombreDevolucion = forms.CharField(
        label="Nombre del producto", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    cantidadDevolucion = forms.IntegerField(
        label="Cantidad de producto", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    fechaDevolucion = forms.DateField(
        label="Fecha de devolución del producto", widget=forms.DateInput(attrs={"class": "form-control datepicker"})
    )
    descripcionDevolucion = forms.CharField(
        label="Motivo de devolución", widget=forms.Textarea(attrs={"class": "form-control"})
    )

class DevolucionModelForm(ModelForm):
    class Meta:
        model = Devolucion_Producto
        fields = '__all__'
        widgets = {
            'nombreDevolucion': TextInput(attrs={"class": "form-control"}),
            'fechaDevolucion': DateInput(attrs={"class": "form-control datepicker"}),
            'cantidadDevolucion': TextInput(attrs={"class": "form-control"}),
            'descripcionDevolucion': Textarea(attrs={"class": "form-control"}),
        }

class CategoriaForm(forms.Form):
    nombreCategoria = forms.CharField(
        label="Nombre de la categoría", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    descripcionCategoria = forms.CharField(
        label="Descripción de la categoría", widget=forms.Textarea(attrs={"class": "form-control"})
    )

class EntradaForm(forms.Form):
    cantidadEntrada = forms.IntegerField(
        label="Cantidad de producto", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    fechaEntrada = forms.DateField(
        label="Fecha de ingreso del producto", widget=forms.DateInput(attrs={"class": "form-control"})
    )
    descripcionEntrada = forms.CharField(
        label="Descripción", widget=forms.Textarea(attrs={"class": "form-control"})
    )

class EntradaModelForm(ModelForm):
    class Meta:
        model = Entrada_Producto
        fields = '__all__'
        widgets = {
            'cantidadEntrada': TextInput(attrs={"class": "form-control"}),
            'fechaEntrada': DateInput(attrs={"class": "form-control"}),
            'descripcionEntrada': Textarea(attrs={"class": "form-control"}),
        }

class SalidaForm(forms.Form):
    cantidadSalida = forms.IntegerField(
        label="Cantidad de producto", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    fechaSalida = forms.DateField(
        label="Fecha de salida", widget=forms.DateInput(attrs={"class": "form-control"})
    )
    descripcionSalida = forms.CharField(
        label="Descripción", widget=forms.Textarea(attrs={"class": "form-control"})
    )

class SalidaModelForm(ModelForm):
    class Meta:
        model = Salida_Producto
        fields = '__all__'
        widgets = {
            'cantidadSalida': TextInput(attrs={"class": "form-control"}),
            'fechaSalida': DateInput(attrs={"class": "form-control"}),
            'descripcionSalida': Textarea(attrs={"class": "form-control"}),
        }
