from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("hola mundo")

def dos(request):
    return HttpResponse("<br><br> ya entendi") #<br> me sirve como tab

def DiaDeHoy(request):
    dia = datetime.now()
    texto = f"hoy es el dia {dia}"
    return HttpResponse(texto)

def MiNombre(self,nombre):
    Doctexto = f"mi nombre es <br><br> {nombre}"
    return HttpResponse(Doctexto)

def ProbandoTemplate(self):
    
    nombre = 'Mica'
    apellido = 'Aimone'
    ListaNotas =[1,5,2,9,8]
     
    diccionario = {"nombre":nombre, "apellido":apellido,"notas":ListaNotas} 
    miHtml = open('/Users/Mica/OneDrive/Desktop/coder/Proyecto1/Proyecto1/plantillas/template1.html')

    plantilla = Template(miHtml.read()) #con template leo la ruta para crear la plantilla dentro del contexto
    
    miHtml.close() #cerramos el archivo

    miContexto = Context(diccionario) #en este caso no hay parametros, pero igual hay q crearlo

    documento = plantilla.render(miContexto) #inicializamos renderizamos la plantilla en el doc

    return HttpResponse(documento)

