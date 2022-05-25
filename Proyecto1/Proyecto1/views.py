from datetime import datetime
from django.http import HttpResponse


from django.http import HttpResponse

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