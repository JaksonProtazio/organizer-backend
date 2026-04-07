import django_filters
from .models import Tarefa

class TarefaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr="icontains", label="Nome da tarefa")
    data_inicio = django_filters.DateFilter(lookup_expr="exact", help_text="Formato: YYYY-MM-DD")

    class Meta:
        model = Tarefa
        fields = ["nome", "data_inicio"]