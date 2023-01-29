from rest_framework import viewsets, filters
from filmes.serializers import FilmeSerializer
from filmes.models import Filme
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    # print(str(queryset.query))
    serializer_class = FilmeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    filterset_fields = ['tipo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

