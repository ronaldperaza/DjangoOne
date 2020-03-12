from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

class CategoriaResources(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado', 'fecha_creacion',)
    resources_class = CategoriaResources

class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'correo']
    list_display = ('nombres','estado', 'correo', 'fecha_creacion',)
    resource_class= AutorResources


# class PostAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
#     list_display = ('categoria', 'estado', 'fecha_creacion')



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)

