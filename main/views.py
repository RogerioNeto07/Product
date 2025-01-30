from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = 'index.html'

class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'

# def Produtos(request):
#     produtos = Produto.objects.all()
#     context = {'produtos': produtos}
#     return render(request, 'produtos.html', context)

class CategoriasView(ListView):
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'

# def Categorias(request):
#     categorias = Categoria.objects.all()
#     context = {'categorias': categorias}
#     return render(request, 'categorias.html', context)

class FornecedoresView(ListView):
    model = Fornecedor
    template_name = 'fornecedores.html'
    context_object_name = 'fornecedores'

# def Fornecedores(request):
#     fornecedores = Fornecedor.objects.all()
#     context = {'fornecedores': fornecedores}
#     return render(request, 'fornecedores.html', context)

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
            produto.categorias.set(form.cleaned_data['categoria'])
            return HttpResponseRedirect(reverse('produtos.html'))
    else:
        form = ProdutoForm()

    return render(request, 'create.html', {'form': form})

def CreateCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            Categoria.objects.create(nome=form.cleaned_data['nome'])
            return HttpResponseRedirect(reverse('produtos.html'))
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
            return HttpResponseRedirect(reverse('produtos.html'))
    else:
        form = FornecedorForm()

    return render(request, 'createfornecedor.html', {'form': form})
    


