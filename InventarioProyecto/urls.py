"""InventarioProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from moduloApp.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuenta/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('login/', CustomLoginView.as_view(), name='login'),

    path('producto/', viewProducto, name='producto'),
    path('add/', addProducto, name='add'),
    path('producto/delete/<int:id>', deleteProducto, name='deleteProducto'),
    path('producto/edit/<int:id>', editarProducto, name='editarProducto'),
    path('bodega/', viewBodega, name='bodega'),
    path('addBodega/', addBodega, name='addBodega'),
    path('bodega/delete/<int:id>', deleteBodega, name='deleteBodega'),
    path('bodega/edit/<int:id>', editarBodega, name='editarBodega'),
    path('registro/', viewRegistro, name='registro'),
    path('tienda/', viewTienda, name='tienda'),
    path('agregarTienda/', agregarTienda, name='agregarTienda'),
    path('tienda/delete/<int:id>', deleteTienda, name='deleteTienda'),
    path('tienda/edit/<int:id>', editarTienda, name='editarTienda'),
    path('devolucion/', viewDevolucion, name='devolucion'),
    path('agregarDevolucion/', agregarDevolucion, name='agregarDevolucion'),
    path('devolucion/delete/<int:id>', deleteDevolucion, name='deleteDevolucion'),
    path('devolucion/edit/<int:id>', editarDevolucion, name='editarDevolucion'),
]
