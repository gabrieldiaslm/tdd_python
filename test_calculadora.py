import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_mais_5_igual_10(self):
        self.assertEqual(soma(5,5), 10)

    def teste_soma_5_negativo_mais_5_igual_0(self):
        self.assertEqual(soma(-5,5), 0)

    def teste_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (1, 1, 2),
            (5.3, 4.7, 10),
            (-5, 5, 0),
            (100, 100, 200),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida = x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x,y), saida)
    
    def teste_x_nao_eh_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def teste_y_nao_eh_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10, '2')
unittest.main(verbosity=1)