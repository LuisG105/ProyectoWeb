from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'inicio.html')

def mostrar_acerca(request):
    datos = {
        'nombre': 'Luis Gutiérrez',
        'carrera': 'Ingeniería en Informática',
        'correo': 'lg035540@gmail.com',
        'redes_sociales': [
            {'plataforma': 'GitHub', 'url': 'https://github.com/LuisG105'},
            {'plataforma': 'LinkedIn', 'url': 'https://linkedin.com'},
        ]
    }
    return render(request, 'acerca.html', {'perfil': datos})