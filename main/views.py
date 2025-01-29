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
            produto = Produto(
                nome=form.cleaned_data['nome'],
                descricao=form.cleaned_data['descricao'],
                codigo=form.cleaned_data['codigo'],
                preco=form.cleaned_data['preco'],
                quantidade=form.cleaned_data['quantidade'],
                fornecedor=form.cleaned_data['fornecedor']
            )
            produto.save()
            produto.categorias.set(form.cleaned_data['categoria'])  # Para ManyToManyField
            return HttpResponseRedirect(reverse('index.html'))
    else:
        form = ProdutoForm()

    return render(request, 'create.html', {'form': form})

def CreateCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            Categoria.objects.create(nome=form.cleaned_data['nome'])
            return HttpResponseRedirect(reverse('index.html'))  # Redireciona para a lista de categorias
    else:
        form = CategoriaForm()

    return render(request, 'createcategoria.html', {'form': form})

def CreateFornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            Fornecedor.objects.create(
                nome=form.cleaned_data['nome'],
                CNPJ=form.cleaned_data['CNPJ']
            )
            return HttpResponseRedirect(reverse('index.html'))
    else:
        form = FornecedorForm()

    return render(request, 'createfornecedor.html', {'form': form})
    


