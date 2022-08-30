from django.shortcuts import render
from .models import Personas
from django.http import HttpResponse

# Create your views here.
def setPersona(request):

    persona1=Personas(nombre="Luciano", apellido='Besedovsky', dni=int(1233254325), fecha_nacimiento ='1971-05-13')
    persona2=Personas(nombre="Manuel", apellido='Besedovsky', dni=int(1233254325), fecha_nacimiento ='1999-07-27')
    persona3=Personas(nombre="Matias", apellido='Besedovsky', dni=int(1233254325), fecha_nacimiento ='2006-03-20')
    persona1.save()
    persona2.save()
    persona3.save()
    texto=f"Personas agregadas"
    return render (request, "Entregable6/setPersona.html")

def getPersona(request):
    return render (request, "Entregable6/getPersona.html")
