from rest_framework.viewsets import ModelViewSet
from core.models import Atracao
from .serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    # Documentação: www.django-rest-framework.org/api-guide/filtering
    filter_fields = ('nome', 'descricao')