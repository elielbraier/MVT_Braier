from django.http import HttpResponse
from django.shortcuts import render

from App_MVT.models import Familia

def familia(self, nombre, edad, fecha_nacimiento):
    familia = Familia(nombre = nombre, edad = edad, fecha_nacimiento = fecha_nacimiento)
    familia.save()
    return HttpResponse(f"""
    <p>Nombre: {familia.nombre} - Edad: {familia.edad} - Fecha Nacimiento: {familia.fecha_nacimiento} </p> """)


def lista_familiares(self):
    lista = Familia.objects.all()
    return render(self, "lista_familiares.html", {"lista_familiares": lista})