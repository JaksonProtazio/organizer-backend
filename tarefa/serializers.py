from rest_framework.serializers import ModelSerializer, ListField, FileField

# Tarefa
from .models import Tarefa

# Arquivo
from arquivo.models import Arquivo
from arquivo.serializers import ArquivoSerializer

class TarefaSerializer(ModelSerializer):
    arquivos = ListField(
        child = FileField(),
        write_only = True,
        required = False
    )
    #arquivo = FileField(write_only=True, required=False)
    arquivos_detalhes = ArquivoSerializer(source = "arquivos", many = True, read_only = True)

    class Meta:
        model = Tarefa
        fields = [
            "id", 
            "nome", 
            "descricao",
            "data_inicio", 
            "data_finalizacao",
            "created_at",
            "modified_at",
            "arquivos",
            "arquivos_detalhes"
        ]

    def create(self, validated_data):
        # retira arquivos que vieram na requisição e 
        # deixa apenas dados da tarefa
        arquivos = validated_data.pop("arquivos")

        tarefa = Tarefa.objects.create(**validated_data)

        # se houver arquivos salva os arquivos da tarefa
        for arq in arquivos:
            Arquivo.objects.create(tarefa = tarefa, arquivo = arq)

        return tarefa