from django.db import models

# Models
from tarefa.models import Tarefa

# Create your models here.
class Arquivo(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(upload_to="evidencias/")