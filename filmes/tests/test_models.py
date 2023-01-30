from django.test import TestCase
from filmes.models import Filme

class FilmeModelTestCase(TestCase):

    def setUp(self):  # criando o cenário de testes
        self.filme = Filme(
            titulo = 'Procurando Nemo',
            data_lancamento = '2003-07-04'
        )

    def test_verifica_atributos_do_filme(self):
        """Teste que verifica os atributos de um filme com valores default"""
        self.assertEquals(self.filme.titulo,'Procurando Nemo')
        self.assertEquals(self.filme.tipo,'F')
        self.assertEquals(self.filme.data_lancamento,'2003-07-04')
        self.assertEquals(self.filme.likes, 0)
        self.assertEquals(self.filme.dislikes, 0)