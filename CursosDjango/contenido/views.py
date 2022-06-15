from django.shortcuts import render , HttpResponse

# Create your views here.


    
def  principal (request):
    return render (request,"contenido/principal.html")

def cursos (request):
    return render (request,"contenido/cursos.html")

def registro (request):
    return render (request,"contenido/registro.html")