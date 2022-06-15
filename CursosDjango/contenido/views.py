from django.shortcuts import render , HttpResponse

# Create your views here.

menu = """<a href="/home/">Preincipal</a>
<a href="/curs/">cursos</a>
<a href="/reg/">Registrarte</a>
    """
    
def  principal (request):
    contenido= """<h1>Mensaje de bienbenida</h1>
    <p>Mensaje</p>
    <p>descripcion</p>
    """
    return HttpResponse(menu+contenido)

def cursos (request):
    contenida="""
    <ul>
  <li>Matematicas</li>
  <li>Base de datos</li>
  <li>Programacion</li>
</ul>
    """
    return HttpResponse(menu+contenida)  

def registro (request):
    contenide="""<h2>Contactos</h2>
     <p>Noombre: <input type="text" name="nombre"></p>
    <p>Correo: <input type="text" name="correo"></p>
    <label for="cars">Materias:</label>

<select name="cars" id="cars">
  <option value="volvo">Matematicas</option>
  <option value="saab">Base de datos </option>
  <option value="mercedes">Programacion</option>
  
</select>
    <p>COMENTARIOS:</p><p><textarea  cols="30" rows="10"></textarea></p>
    <p><input type="button" value="Enviar" name="enviar"></p>
    """
    return HttpResponse(menu+contenide)  