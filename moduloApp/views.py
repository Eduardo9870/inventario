from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from moduloApp.models import *
from moduloApp.forms import *
from django.contrib.auth.views import LoginView
# Create your views here.
from .forms import BodegaForm
from .models import Bodega

def viewProducto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos,
        'titulo': 'Productos',
    }
    return render(request, 'viewProductos.html', data)
    
def viewEntrada_Producto(request):
    Entrada_Productos = Entrada_Producto.objects.all()
    data = {
        'Entrada_Productos': Entrada_Productos,
        'titulo': 'Entrada_Productos',
    }
    return render(request, 'viewEntradaProducto.html', data)

def addEntrada(request):
    data = {
        'titulo': 'Agregar Entrada',
        'form': Entrada_ProductoModelForm()
    }
    if (request.method) == 'POST':
        formulario = Entrada_ProductoModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/entradaProducto')
        else:
            data['form'] = formulario
    return render(request, 'formEntradaProductos.html', data)


def viewCategoria(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias': categorias,
        'titulo': 'categorias',
    }
    return render(request, 'viewCategoria.html', data)

def addCategoria(request):
    data = {
        'titulo': 'Agregar categoria',
        'form': categoriaModelForm()
    }
    if (request.method) == 'POST':
        formulario = categoriaModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categoria')
        else:
            data['form'] = formulario
    return render(request, 'formCategoria.html', data)

def editarCategoria(request, id):
    form = Categoria.objects.get(id=id)
    data = {
        'titulo': 'Editar categoria',
        'form': categoriaModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = categoriaModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/categoria')
        else:
            data['form'] = form
    return render(request, 'formCategoria.html', data)

def deleteCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('/categoria')


def addProducto(request):
    data = {
        'titulo': 'Agregar productos',
        'form': ProductoModelForm()
    }
    if (request.method) == 'POST':
        formulario = ProductoModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto')
        else:
            data['form'] = formulario
    return render(request, 'formProductos.html', data)


def deleteProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/producto')


def editarProducto(request, id):
    form = Producto.objects.get(id=id)
    data = {
        'titulo': 'Editar productos',
        'form': ProductoModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = ProductoModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/producto')
        else:
            data['form'] = form
    return render(request, 'formProductos.html', data)




def viewBodega(request):
    bodegas = Bodega.objects.all()
    data = {
        'bodegas': bodegas,
        'titulo': 'Bodega',
    }
    return render(request, 'viewBodega.html', data)


def addBodega(request):
    data = {
        'titulo': 'Agregar Bodega',
        'form': BodegaModelForm()
    }
    if (request.method) == 'POST':
        formulario = BodegaModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/bodega')
        else:
            data['form'] = formulario
    return render(request, 'formBodega.html', data)


def deleteBodega(request, id):
    bodega = Bodega.objects.get(id=id)
    bodega.delete()
    return redirect('/bodega')


def editarBodega(request, id):
    form = Bodega.objects.get(id=id)
    data = {
        'titulo': 'Editar Bodega',
        'form': BodegaModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = BodegaModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/bodega')
        else:
            data['form'] = form
    return render(request, 'formBodega.html', data)



class CustomLoginView(LoginView):
    template_name = 'login.html'
