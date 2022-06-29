from django.contrib import admin
from .models import Cursos
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('Materia', 'Profesor', 'carrera')
    search_fields=('Materia', 'Profesor', 'carrera')
    list_filter = ('carrera','Profesor')

    date_hierarchy = 'created'
admin.site.register(Cursos,AdministrarModelo)
# Register your models here.
