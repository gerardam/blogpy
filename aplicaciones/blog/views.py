from django.shortcuts import render
from .models import Post, Categoria

def home(request):
    posts = Post.objects.filter(estado = True)
    return render(request, 'index.html', {'posts':posts})

def detallePost(request, slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'post.html', {'detalle_post':post})

def programacion(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Programacion'))
    return render(request, 'programacion.html', {'posts': posts})

def tecnologia(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Tecnologia'))
    return render(request, 'tecnologia.html', {'posts': posts})

def alimentos(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre = 'Alimentos'))
    return render(request, 'alimentos.html', {'posts': posts})