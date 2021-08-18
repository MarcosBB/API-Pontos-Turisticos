from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id= self.request.query_params.get('id', None)
        nome= self.request.query_params.get('nome', None)
        descricao= self.request.query_params.get('descricao', None)
        queryset= PontoTuristico.objects.all()

        if id:
            queryset= PontoTuristico.objects.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao_iexact=descricao)

        return queryset


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