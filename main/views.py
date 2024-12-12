from django.shortcuts import render
from .models import *

def Index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'index.html', context)

def Categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'categorias.html', context)

def Fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    context = {'fornecedores': fornecedores}
    return render(request, 'fornecedores.html', context)

def Details(request, produto_id):
   produto = Produto.objects.get(id=produto_id)
   context = {'produto': produto}
   return render(request, 'details.html', context)

