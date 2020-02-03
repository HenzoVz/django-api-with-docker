from rest_framework.serializers import ModelSerializer
from core.models import Recurso

class RecursoSerializer(ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('nome', 'descricao', 'horario_func', 'idade_min')