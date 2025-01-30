"""
URL configuration for produto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index.html'),
    path('produtos', views.ProdutosView.as_view(), name='produtos.html'),
    path('<int:produto_id>', views.Details, name='details.html'),
    path('categorias', views.CategoriasView.as_view(), name='categorias.html'),
    path('fornecedores', views.FornecedoresView.as_view(), name='fornecedores.html'),
    path('criar', views.Create, name='create.html'),
    path('criarcategoria', views.CreateCategoria, name='createcategoria.html'),
    path('criarfornecedor', views.CreateFornecedor, name='createfornecedor.html'),
]
