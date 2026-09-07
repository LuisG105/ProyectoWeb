from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'inicio.html')

def mostrar_acerca(request):
    datos = {
        'nombre': 'Eduardo Molina',
        'correo': 'EduMoli04@gmail.com',
        'redes_sociales': [
            {'plataforma': 'LinkedIn', 'url': 'https://linkedin.com'},
        ]
    }
    return render(request, 'acerca.html', {'perfil': datos})