from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from panel.models import Oficina, Asociado, Aporte

# Register your models here.
# admin.site.register(Oficinas)

class OficinasResources(resources.ModelResource):
    fields = (
        'codigo',
        'nombre',
        'ubicación',
    )
    class Meta:
        model = Oficina

class AsociadoResources(resources.ModelResource):
    fields = (
        'oficina',
        'cedula',
        'nombres',
        'apellidos',
        'estado_civil',
        'fecha_de_nacimiento',
        'correo',
        'genero',
        'estado',
        'sueldo',
        'tipo_titularidad'
    )
    class Meta:
        model = Asociado

class AportesResources(resources.ModelResource):
    fields = (
        'id',
        'asociado',
        'fecha',
        'valor'
    )
    class Meta:
        model = Aporte

@admin.register(Oficina)
class OficinasAdmin(ImportExportModelAdmin):
    resource_class = OficinasResources
    list_display = (
        'codigo',
        'nombre',
        'ubicación'
    )

@admin.register(Asociado)
class AsociadoAdmin(ImportExportModelAdmin):
    resource_class = AsociadoResources
    list_display = (
        'oficina',
        'cedula',
        'nombres',
        'apellidos',
        'estado_civil',
        'fecha_de_nacimiento',
        'correo',
        'genero',
        'estado',
        'sueldo',
        'tipo_titularidad',
        'fecha_de_vinculación'
    )

@admin.register(Aporte)
class AportesAdmin(ImportExportModelAdmin):
    resource_class = AportesResources
    list_display = (
        'id',
        'asociado',
        'fecha',
        'valor'
    )