from django.contrib import admin
from .models import Cursos
from .models import AcvidadesdelCurso
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('Materia', 'Profesor', 'carrera')
    search_fields=('Materia', 'Profesor', 'carrera')
    list_filter = ('carrera','Profesor')

    date_hierarchy = 'created'
admin.site.register(Cursos,AdministrarModelo)
# Register your models here.
class AdministrarActividades(admin.ModelAdmin):
 
 list_display = ('id', 'actividad')
 search_fields = ('id','created')
 date_hierarchy = 'created'
 readonly_fields = ('created', 'id')

admin.site.register(AcvidadesdelCurso,AdministrarActividades)