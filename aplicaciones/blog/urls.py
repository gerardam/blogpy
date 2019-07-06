from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('programacion', programacion, name = 'programacion'),
    path('tecnologia', tecnologia, name = 'tecnologia'),
    path('alimentos', alimentos, name = 'alimentos'),
]