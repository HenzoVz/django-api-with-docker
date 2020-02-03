from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacoe


class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avaliacoe
        fields = ['user', 'comentario', 'nota', 'data']