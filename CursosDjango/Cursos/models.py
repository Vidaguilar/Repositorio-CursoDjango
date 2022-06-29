from django.db import models

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
