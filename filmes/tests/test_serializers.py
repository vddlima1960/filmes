from django.test import TestCase
from filmes.models import Filme
from filmes.serializers import FilmeSerializer

class FilmeSerializerTestCase(TestCase):

    def setUp(self):    # definindo o cenário de teste
        self.filme = Filme(
            titulo = 'Procurando Nemo',
            tipo = 'F',
            data_lancamento = '2003-07-04',
            likes = 2340,
            dislikes = 40
        )
        self.serializer = FilmeSerializer(instance=self.filme)

    def test_verifica_campos_serializados(self):  #função que realizará os testes
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data 
        self.assertEquals(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))
    
    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEquals(data['titulo'], self.filme.titulo)
        self.assertEquals(data['tipo'], self.filme.tipo)
        self.assertEquals(data['data_lancamento'], self.filme.data_lancamento)
        self.assertEquals(data['likes'], self.filme.likes)
