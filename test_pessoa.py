'''
class Pessoa
    __init__
    nome str
    sobrenome str
    dados_obtidos bool (inicia False)

API:
    obter_todos_os_dados -> method
    OK
    404

    (dados_obtidos se torna True se dados_obtidos com sucesso)
'''
import unittest
from unittest.mock import patch
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Gabriel', 'Dias')
        self.p2 = Pessoa('Maria', 'José')

    def test_pessoa_attr_nome_eh_str(self): #Nome str
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_nome_tem_valor_correto(self): #Nome valor
        self.assertEqual(self.p1.nome, 'Gabriel')
        self.assertEqual(self.p2.nome, 'Maria')

    def test_pessoa_attr_sobrenome_eh_str(self): # Sobrenome str
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self): #Sobrenome valor
        self.assertEqual(self.p1.sobrenome, 'Dias')
        self.assertEqual(self.p2.sobrenome, 'José')

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def teste_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def teste_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)

    def teste_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)