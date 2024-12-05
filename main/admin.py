from django.contrib import admin
from main.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','codigo', 'preco','quantidade', 'data')
    search_fields = ['nome', 'codigo']
    list_filter = ['data']
    ordering = ['-data']
admin.site.register(Produto, ProdutoAdmin)
    

