from atracoes.api.serializers import AtracaoSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes')
    