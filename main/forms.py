from django import forms
from .models import *

class ProdutoForm(forms.Form):
   nome = forms.CharField(max_length=200)
   descricao = forms.CharField(max_length=200, widget= forms.Textarea)
   codigo = forms.CharField(max_length=10)
   preco = forms.DecimalField(max_digits=10, decimal_places=2)
   quantidade = forms.IntegerField()
   fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all())
   categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all())


