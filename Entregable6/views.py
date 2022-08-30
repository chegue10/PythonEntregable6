from django.shortcuts import render
from .models import Personas
from django.http import HttpResponse
import sqlite3
# Create your views here.
def setPersona(request):
    apellido = 'Besedovsky'
    uno = {'nombre':"Luciano", 'apellido':apellido, 'dni':int(1233254325), 'fecha_nacimiento':'1971-05-13'}
    dos = {'nombre':"Manuel", 'apellido':apellido, 'dni':int(1233254325), 'fecha_nacimiento':'1999-07-27'}
    tres = {'nombre':"Matias", 'apellido':apellido, 'dni':int(1233254325), 'fecha_nacimiento':'2006-03-20'}
    persona1=Personas(nombre="Luciano", apellido=apellido, dni=int(1233254325), fecha_nacimiento ='1971-05-13')
    persona2=Personas(nombre="Manuel", apellido=apellido, dni=int(1233254325), fecha_nacimiento ='1999-07-27')
    persona3=Personas(nombre="Matias", apellido=apellido, dni=int(1233254325), fecha_nacimiento ='2006-03-20')
    persona1.save()
    persona2.save()
    persona3.save()
    texto=f"Personas agregadas"
    return render (request, "Entregable6/setPersona.html", {'apellido': apellido,'uno':uno,'dos':dos,'tres':tres})

def getPersona(request):
    apellido = 'Besedovsky'
    uno = {'nombre':"Luciano", 'apellido':apellido, 'dni':int(1233254325), 'fecha_nacimiento':'1971-05-13'}
    dos = {'nombre':"Manuel", 'apellido':apellido, 'dni':int(1233254325), 'fecha_nacimiento':'1999-07-27'}
    tres = {'nombre':"Matias", 'apellido':apellido, 'dni':int(1233254325), 'fecha_nacimiento':'2006-03-20'}
    return render (request, "Entregable6/getPersona.html",{'apellido': apellido,'uno':uno,'dos':dos,'tres':tres})
