from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=150)
    localizacao = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)

    class Meta:
        unique_together = ['nome', 'localizacao', 'bairro']

    def __str__(self):
        return f"{self.nome} - {self.localizacao} - {self.bairro}"

class Produto(models.Model):
    loja = models.ForeignKey(       # ← ESSA LINHA É O RELACIONAMENTO
        Loja,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produtos'
    )
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
