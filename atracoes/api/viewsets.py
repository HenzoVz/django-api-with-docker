from rest_framework.viewsets import ModelViewSet
from atracoes.models import Recurso
from .serializers import RecursoSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer