from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('p', views.ProdutosView.as_view(), name='produtos.html'),
    path('<int:produto_id>', views.Details, name='details.html'),
    path('categorias', views.CategoriasView.as_view(), name='categorias.html'),
    path('fornecedores', views.Fornecedores, name='fornecedores.html'),
    path('criar', views.Create, name='create.html'),
    path('criarcategoria', views.CreateCategoria, name='createcategoria.html'),
    path('criarfornecedor', views.CreateFornecedor, name='createfornecedor.html'),
]