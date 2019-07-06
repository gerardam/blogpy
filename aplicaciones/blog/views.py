from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def programacion(request):
    return render(request, 'programacion.html')

def tecnologia(request):
    return render(request, 'tecnologia.html')

def alimentos(request):
    return render(request, 'alimentos.html')