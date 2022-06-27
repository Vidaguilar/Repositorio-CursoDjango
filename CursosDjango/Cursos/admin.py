from django.contrib import admin
from .models import Cursos
# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Cursos,AdministrarModelo)
# Register your models here.
