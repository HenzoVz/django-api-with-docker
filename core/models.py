from django.db import models
from atracoes.models import Recurso
from comentarios.models import Comentario
from avaliacoes.models import Avaliacoe
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recursos = models.ManyToManyField(Recurso)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacoe)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
