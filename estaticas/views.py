from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'inicio.html')

def mostrar_acerca(request):
    return render(request, 'acerca.html',)