from django import urls
from django.urls import path
from . import views

urlpatterns=[
    path('', views.perfil, name="perfil"),
    path('editarperfil/', views.editar_perfil, name="editar_perfil")
]