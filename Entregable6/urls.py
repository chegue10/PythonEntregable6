
from django.urls import path
from Entregable6.views import *

urlpatterns = [
    
    path("getPersona/", getPersona),
    path("setPersona/", setPersona),
   
]
