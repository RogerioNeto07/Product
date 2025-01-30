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

   def clean_codigo(self):
      codigo = self.cleaned_data['codigo']
      if Produto.objects.filter(codigo=codigo).exists():
         raise forms.ValidationError("Já existe um produto com este código.")
      if not codigo.isalnum():
         raise forms.ValidationError("o código não pode ter caracteres especiais")
      return codigo
   
   def clean_preco(self):
      preco = self.cleaned_data['preco']
      if preco <= 0:
         raise forms.ValidationError("O preço deve ser maior que 0.")
      return preco

   def clean_quantidade(self):
      quantidade = self.cleaned_data['quantidade']
      if quantidade < 0:
         raise forms.ValidationError("A quantidade deve ser maior ou igual a 0.")
      return quantidade
   
   def clean_nome(self):
      nome = self.cleaned_data['nome']
      if len(nome) < 3:
         raise forms.ValidationError("O nome do produto deve ter ao menos 3 caracteres.")
      return nome

class CategoriaForm(forms.Form):
   nome = forms.CharField(max_length=20)

class FornecedorForm(forms.Form):
   nome = forms.CharField(max_length=200)
   CNPJ = forms.CharField(max_length=18)

