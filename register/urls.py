from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.formulario, name='create'), #define um nome mais fácil para acessar no html
    path('<int:id>/', views.formulario, name='update'),
    path('remove/<int:id>/', views.remover, name='delete'),
    path('listagem/', views.listar, name='retrieve')
]
