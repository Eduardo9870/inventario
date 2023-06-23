from django.shortcuts import render, redirect
from moduloApp.models import *
from moduloApp.forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


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


from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

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

def is_admin_or_bodeguero(user):
    return user.is_superuser or user.groups.filter(name='Bodeguero').exists()

@login_required
@user_passes_test(is_admin_or_bodeguero)
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


""" ----------------------------------------------------------------------------------------------------- """

def generar_reporte(request):
    # Obtener los productos de la base de datos
    productos = Producto.objects.all()
    bodegas = Bodega.objects.all()
    tiendas = Tienda.objects.all()
    categorias = Categoria.objects.all()
    devoluciones = Devolucion.objects.all()
    entradas = Entrada.objects.all()
    salidas =Salida.objects.all()
    titulo = "Reportes "

    # Renderizar el template con los datos
    reporte_html = render_to_string('reporte.html', {'productos': productos, 'bodegas':bodegas, 'tiendas': tiendas, 'categorias': categorias, 'devoluciones': devoluciones, 'entradas': entradas, 'salidas':salidas, 'titulo': titulo})

    # Crear una respuesta HTTP con el contenido HTML
    response = HttpResponse(content_type='text/html')
    response.write(reporte_html)

    return response

def descargar_reporte_pdf(request):
    # Obtener los datos de la base de datos
    productos = Producto.objects.all()
    bodegas = Bodega.objects.all()
    tiendas = Tienda.objects.all()
    categorias = Categoria.objects.all()
    devoluciones = Devolucion.objects.all()
    entradas = Entrada.objects.all()
    salidas =Salida.objects.all()


    # Crear un objeto BytesIO para almacenar el PDF generado
    buffer = BytesIO()

    # Crear el objeto PDF utilizando reportlab
    p = canvas.Canvas(buffer)

    # Agregar el título al PDF
    titulo = "Reportes Generales"
    p.setFont("Helvetica-Bold", 16)
    p.drawCentredString(300, 750, titulo)

    # Agregar los datos de los productos al PDF
    y = 700
    p.drawString(50, y, "Datos de productos:")
    y -= 20

    # Dibujar encabezado de columnas
     # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Producto")
    p.drawString(200, y, "Cantidad")
    p.drawString(280, y, "Descripción")
    p.drawString(380, y, "Bodega")
    p.drawString(460, y, "Categoria")
    
    y -= 20

    for producto in productos:
        p.drawString(50, y, str(producto.id))       
        p.drawString(100, y, str(producto.nombreProducto))
        p.drawString(200, y, str(producto.cantidad))
        p.drawString(280, y, str(producto.descripcionProducto))
        p.drawString(380, y, str(producto.bodega))
        p.drawString(460, y, str(producto.categoria))
        y -= 20

 # Espacio entre las secciones de datos
    y -= 20


    p.drawString(50, y, "Datos de bodegas:")
    y -= 20
    # Dibujar encabezado de columnas
    # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Nombre")
    p.drawString(200, y, "Dirección")
    y -= 20
    for bodega in bodegas:
        p.drawString(50, y, str(bodega.id)) 
        p.drawString(100, y, str(bodega.nombreBodega))
        p.drawString(200, y, str(bodega.direccionBodega))
        y -= 20

 # Espacio entre las secciones de datos
    y -= 20

    p.drawString(50, y, "Datos de tiendas:")
    y -= 20
        # Dibujar encabezado de columnas
     # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Nombre")
    p.drawString(200, y, "Dirección")
    p.drawString(330, y, "Bodega")
    

    y -= 20
    for tienda in tiendas:
        p.drawString(50, y, str(tienda.id)) 
        p.drawString(100, y, str(tienda.nombreTienda))
        p.drawString(200, y, str(tienda.direccionTienda))
        p.drawString(330, y, str(tienda.bodega)) 
        y -= 20

 # Espacio entre las secciones de datos
    y -= 20

    p.drawString(50, y, "Datos de categorias:")
    y -= 20
        # Dibujar encabezado de columnas
     # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Nombre")
    p.drawString(230, y, "Descripción")

    y -= 20
    for categoria in categorias:
        p.drawString(50, y, str(categoria.id)) 
        p.drawString(100, y, str(categoria.nombreCategoria))
        p.drawString(230, y, str(categoria.descripcionCategoria))
        y -= 20

 # Espacio entre las secciones de datos
    y -= 20

    p.drawString(50, y, "Datos de devoluciones:")
    y -= 20
        # Dibujar encabezado de columnas
     # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Nombre")
    p.drawString(200, y, "Cantidad")
    p.drawString(300, y, "Precio")
    p.drawString(400, y, "Motivo")
    y -= 20
    for devolucion in devoluciones:
        p.drawString(50, y, str(devolucion.id)) 
        p.drawString(100, y, str(devolucion.nombreDevolucion))
        p.drawString(200, y, str(devolucion.cantidadDevolucion))
        p.drawString(300, y, str(devolucion.precioDevolucion))
        p.drawString(400, y, str(devolucion.motivoDevolucion))
        y -= 20

 # Espacio entre las secciones de datos
    y -= 20

    p.drawString(50, y, "Datos de entradas:")
    y -= 20
        # Dibujar encabezado de columnas
     # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Fecha")
    p.drawString(200, y, "Descripción")
    p.drawString(300, y, "Bodega")

    y -= 20
    for entrada in entradas:
        p.drawString(50, y, str(entrada.id)) 
        p.drawString(100, y, str(entrada.fecha_entrada))
        p.drawString(200, y, str(entrada.descripcion_entrada))
        p.drawString(300, y, str(entrada.bodega))
        y -= 20

 # Espacio entre las secciones de datos
    y -= 20

    p.drawString(50, y, "Datos de salidas:")
    y -= 20
        # Dibujar encabezado de columnas
     # Establecer estilo de fuente normal
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "#")
    p.drawString(100, y, "Fecha")
    p.drawString(200, y, "Descripción")
    p.drawString(300, y, "Bodega")

    y -= 20
    for salida in salidas:
        p.drawString(50, y, str(salida.id)) 
        p.drawString(100, y, str(salida.fecha_salida))
        p.drawString(200, y, str(salida.descripcion_salida))
        p.drawString(300, y, str(salida.bodega))
        y -= 20

    

    # Guardar el contenido del PDF
    p.showPage()
    p.save()

    # Obtener el contenido del BytesIO y crear la respuesta HTTP
    buffer.seek(0)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_productos.pdf"'
    response.write(buffer.getvalue())

    return response

def mostrar_reporte(request):
    # Obtener los productos de la base de datos
    productos = Producto.objects.all()
    bodegas = Bodega.objects.all()
    tiendas = Tienda.objects.all()
    categorias = Categoria.objects.all()
    devoluciones = Devolucion.objects.all()
    entradas = Entrada.objects.all()
    salidas =Salida.objects.all()

    titulo = "Reportes"


    return render(request, 'reporte.html', {'productos': productos, 'bodegas':bodegas, 'tiendas':tiendas, 'categorias': categorias, 'devoluciones': devoluciones, 'entradas':entradas, 'salidas':salidas, 'titulo': titulo})

