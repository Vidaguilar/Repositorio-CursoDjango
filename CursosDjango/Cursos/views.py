from django.shortcuts import render
from .models import Cursos
def cursos(request):
    cursos=Cursos.objects.all()
    return render(request, "cursos/principal.html",{'cursos':cursos})

# Create your views here.
