from django.shortcuts import render, redirect
from moduloApp.models import *
from moduloApp.forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = UserCreationForm()
    return render(request, 'registration/registro.html', {'formulario': formulario})

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/home')
    else:
        formulario = AuthenticationForm()
    return render(request, 'login.html', {'formulario': formulario})




def viewProducto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos,
        'titulo': 'Productos',
    }
    return render(request, 'viewProductos.html', data)


def addProducto(request):
    data = {
        'titulo': 'Agregar productos',
        'form': ProductoForm()
    }
    if (request.method) == 'POST':
        formulario = ProductoForm(request.POST)
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
        'form': ProductoForm(instance=form)
    }
    if (request.method == 'POST'):
        form = ProductoForm(request.POST, instance=form)
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
        'form': BodegaForm()
    }
    if (request.method) == 'POST':
        formulario = BodegaForm(request.POST)
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
        'form': BodegaForm(instance=form)
    }
    if (request.method == 'POST'):
        form = BodegaForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/bodega')
        else:
            data['form'] = form
    return render(request, 'formBodega.html', data)



class CustomLoginView(LoginView):
    template_name = 'login.html'
