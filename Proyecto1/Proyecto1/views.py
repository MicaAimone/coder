from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader #el loader reemplaza a la ruta absoluta 

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

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

