from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoe
from .serializers import AvaliacoesSerializer


class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacoe.objects.all()
    serializer_class = AvaliacoesSerializer