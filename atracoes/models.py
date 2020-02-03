from django.db import models


class Recurso(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_min = models.IntegerField()

    def __str__(self):
        return self.nome    