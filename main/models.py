from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    codigo = models.CharField(max_length=10, unique=True, null=False, blank=False)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()