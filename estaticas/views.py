from django.shortcuts import render

def mostrar_homes(request):
    return render(request, 'inicio.html')

def mostrar_acerca(request):
    datos = {
        'nombre': 'Enrique Molina',
        'carrera': 'Turismo',
        'correo': 'EnrMoli050@gmail.com',
        'contacto': '9 98887150',      
        'ubicacion': 'Calama, Chile',         
        'proyecto': 'Informacion de Chile',

    }

    return render(request, 'acerca.html', datos)