from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valor = models.DecimalField('Valor',decimal_places=2, max_digits=8)
    quantidade = models.IntegerField('Quantidade')

    def __str__(self):
        return f'{self.nome} {self.valor} {self.quantidade}'
