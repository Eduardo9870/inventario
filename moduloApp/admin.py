from django.contrib import admin
from django.contrib.auth.models import Permission
from moduloApp.models import Categoria
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User
from import_export import resources
# Register your models here.

class BodegaResources(resources.ModelResource):
    fields = (
        'nombreBodega',
        'direccionBodega',
    )
    class Meta:
        model = Bodega

@admin.register(Bodega)
class BodegaAdmin(ImportExportModelAdmin):
    resource_class = BodegaResources
    list_display = (
        'nombreBodega',
        'direccionBodega',
    )
