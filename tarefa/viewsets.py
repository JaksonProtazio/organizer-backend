from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser

# Tarefa
from .models import Tarefa
from .serializers import TarefaSerializer
from .filters import TarefaFilter

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TarefaFilter
    parser_classes = [MultiPartParser, FormParser]  