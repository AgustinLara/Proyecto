from django.shortcuts import render
from django.http import HttpResponse
from MODELOSproyecto.models import Infrmacion 

def Inicio(request):
    return HttpResponse("Bienvenidos a ¡LOB!")

def Items(request):
    return HttpResponse("Seccion de ITEMS")

def Buffs_Nerfeos(request):
    return HttpResponse("Nerfeos y BUffeos de la UBDATE")

