from pyclbr import Class
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.db import models
class Cursos(models.Model): 
    Materia = models.CharField(max_length=12,verbose_name="Mat") 
    Grado = models.TextField()
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    Descripcion = models.TextField() 
    carrera = models.TextField()
    Profesor = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"] 
    def __str__(self):
      return self.Materia

class AcvidadesdelCurso(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="clave")
    materia=models.ForeignKey(Cursos,on_delete=models.CASCADE,verbose_name="Materia")
    created = models.DateField(auto_now_add=True,verbose_name="Registrado")
    actividad = RichTextField(verbose_name="Comentario")
    class Meta:
         verbose_name = "Actividad"
         verbose_name_plural = "Actividades"
         ordering = ["-created"] 
    def __str__(self):
         return self.actividad