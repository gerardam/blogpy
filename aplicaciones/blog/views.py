from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.filter(estado = True)
    return render(request, 'index.html', {'posts':posts})

def detallePost(request, slug):
    #post = Post.objects.get(slug = slug)
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'detalle_post':post})

def programacion(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    return render(request, 'programacion.html', {'posts': posts})

def tecnologia(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    return render(request, 'tecnologia.html', {'posts': posts})

def alimentos(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Alimentos'))
    return render(request, 'alimentos.html', {'posts': posts})