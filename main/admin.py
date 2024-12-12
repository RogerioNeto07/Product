from django.contrib import admin
from main.models import *

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','codigo', 'preco','quantidade', 'data',)
    search_fields = ['nome', 'codigo', 'categoria']
    list_filter = ['data']
    ordering = ['-data']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome','CNPJ')
    search_fields = ('nome','CNPJ')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Fornecedor, FornecedorAdmin)
    

