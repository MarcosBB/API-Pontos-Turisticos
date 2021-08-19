from rest_framework.fields import SerializerMethodField
from atracoes.api.serializers import AtracaoSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'descricao_completa')
    
    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome, obj.descricao)