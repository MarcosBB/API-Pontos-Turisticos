from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    ''' PARA SOBRESCREVER ACTIONS DO REST
    
    def list(self, request, *args, **kwargs):
        return Response({'teste':'123'})
    

    PODEMOS SOBRESCREVER OS MÉTODOS list, create, destroy, retrieve, uptade, partial_update e etc
    '''


    ''' PARA CRIAR ACTIOS DIFERENTES
    from rest_framework.decorators import action

    @action(methods=['post','get'], detail=True)
    def denunciar (self, request, pk=None):
        pass

    '''