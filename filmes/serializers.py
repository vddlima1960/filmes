from rest_framework import serializers
from filmes.models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['titulo', 'tipo', 'data_lancamento', 'likes']