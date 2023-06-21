from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from moduloApp.models import *
from moduloApp.forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


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
    if request.method == 'POST':
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


def viewRegistro(request):
    data = {
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password'])
            login(request, user)
            messages.sucess(request, "Te has registrado correctamente")
            return redirect(to="home")
        data['formulario'] = formulario

    return render(request, 'registration/registrar_nuevo.html', data)


def viewTienda(request):
    tiendas = Tienda.objects.all()
    data = {
        'tiendas': tiendas,
        'titulo': 'Tienda',
    }
    return render(request, 'viewTienda.html', data)


def agregarTienda(request):
    data = {
        'titulo': 'Agregar Tienda',
        'form': TiendaModelForm()
    }
    if request.method == 'POST':
        formulario = TiendaModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/tienda')
        else:
            data['form'] = formulario
    return render(request, 'formTienda.html', data)


def deleteTienda(request, id):
    tienda = Tienda.objects.get(id=id)
    tienda.delete()
    return redirect('/tienda')


def editarTienda(request, id):
    form = Tienda.objects.get(id=id)
    data = {
        'titulo': 'Editar Tienda',
        'form': TiendaModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = TiendaModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/tienda')
        else:
            data['form'] = form
    return render(request, 'formTienda.html', data)


def viewDevolucion(request):
    devoluciones = Devolucion.objects.all()
    data = {
        'devoluciones': devoluciones,
        'titulo': 'Devoluciones de Productos',
    }
    return render(request, 'viewDevolucion.html', data)


def agregarDevolucion(request):
    data = {
        'titulo': 'Agregar devoluciones',
        'form': DevolucionModelForm()
    }
    if (request.method) == 'POST':
        formulario = DevolucionModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/devolucion')
        else:
            data['form'] = formulario
    return render(request, 'formDevolucion.html', data)


def deleteDevolucion(request, id):
    devolucion = Devolucion.objects.get(id=id)
    devolucion.delete()
    return redirect('/devolucion')


def editarDevolucion(request, id):
    form = Devolucion.objects.get(id=id)
    data = {
        'titulo': 'Editar devolucion',
        'form': DevolucionModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = DevolucionModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/devolucion')
        else:
            data['form'] = form
    return render(request, 'formDevolucion.html', data)


def viewCategoria(request):
    categorias = Categoria.objects.all()
    data = {
        'categorias': categorias,
        'titulo': 'Categorias',
    }
    return render(request, 'viewCategoria.html', data)


def agregarCategoria(request):
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


def viewEntrada(request):
    entradas = Entrada.objects.all()
    data = {
        'entradas': entradas,
        'titulo': 'Entrada Producto',
    }
    return render(request, 'viewEntradaProducto.html', data)

def agregarEntrada(request):
    data = {
        'titulo': 'Agregar Entrada',
        'form': EntradaModelForm()
    }
    if (request.method) == 'POST':
        formulario = EntradaModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/entrada')
        else:
            data['form'] = formulario
    return render(request, 'formEntradaProductos.html', data)

def editarEntrada(request, id):
    form = Entrada.objects.get(id=id)
    data = {
        'titulo': 'Editar entrada producto',
        'form': EntradaModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = EntradaModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/entrada')
        else:
            data['form'] = form
    return render(request, 'formEntradaProductos.html', data)


def deleteEntrada(request, id):
    entrada = Entrada.objects.get(id=id)
    entrada.delete()
    return redirect('/entrada')




def viewSalida(request):
    salidas = Salida.objects.all()
    data = {
        'salidas': salidas,
        'titulo': 'Salida Producto',
    }
    return render(request, 'viewSalidaProducto.html', data)

def agregarSalida(request):
    data = {
        'titulo': 'Agregar Salidas',
        'form': SalidaModelForm()
    }
    if (request.method) == 'POST':
        formulario = SalidaModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/salida')
        else:
            data['form'] = formulario
    return render(request, 'formSalidaProductos.html', data)

def editarSalida(request, id):
    form = Salida.objects.get(id=id)
    data = {
        'titulo': 'Editar Salida producto',
        'form': SalidaModelForm(instance=form)
    }
    if (request.method == 'POST'):
        form = SalidaModelForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/salida')
        else:
            data['form'] = form
    return render(request, 'formSalidaProductos.html', data)


def deleteSalida(request, id):
    salida = Salida.objects.get(id=id)
    salida.delete()
    return redirect('/salida')
