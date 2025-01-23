from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index.html'),
    path('<int:produto_id>', views.Details, name='details.html'),
    path('categorias', views.Categorias, name='categorias.html'),
    path('fornecedores', views.Fornecedores, name='fornecedores.html'),
    path('criar', views.Create, name='create.html')
]