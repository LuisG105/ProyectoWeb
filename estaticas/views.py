from django.shortcuts import render

def mostrar_homes(request):
    return render(request, 'inicio.html')

def mostrar_acerca(request):
    perfil_datos = {
        'nombre': 'Enrique Molina',
        'carrera': 'Turismo',
        'correo': 'EnrMoli050@gmail.com',
        'region': 'Calama, Chile',
    }

    return render(request, 'acerca.html', {'perfil': perfil_datos})