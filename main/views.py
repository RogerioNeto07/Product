from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

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

def Create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = Produto()
            produto.nome = form.cleaned_data['nome']
            produto.codigo = form.cleaned_data['codigo']
            produto.descricao = form.cleaned_data['descricao']
            produto.preco = form.cleaned_data['preco']
            # quantidade
            produto.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            form = ProdutoForm(request.POST)
    else:
        form = ProdutoForm()

    return render(request, 'create.html', {'form': form})



