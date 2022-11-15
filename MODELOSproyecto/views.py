from django.shortcuts import render
from django.http import HttpResponse
from MODELOSproyecto.models import Infrmacion 

def Inicio(request):
    return render(request, "MODELOSproyecto/inicio.html")

