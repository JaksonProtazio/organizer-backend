from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_finalizacao = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)