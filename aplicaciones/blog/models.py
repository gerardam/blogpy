from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Categoria activada/no activada', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombre del autor', max_length = 255, null = False, blank = False)
    apellidos = models.CharField('Apellidos del autor', max_length = 255, null = False, blank = False)
    facebook = models.URLField('Facebook', null = False, blank = True)
    twitter = models.URLField('Twitter', null = False, blank = True)
    instagram = models.URLField('Instagram', null = False, blank = True)
    web = models.URLField('Web', null = False, blank = True)
    correo = models.EmailField('E-mail', null = False, blank = False)
    estado = models.BooleanField('Autor activo/inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripcion', max_length = 150, null = False, blank = False)
    contenido = RichTextField()
    imagen = models.URLField(max_length = 500, null = False, blank = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Autor activo/inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo