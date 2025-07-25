'''
No exemplo abaixo, vamos usar uma função simples para fazer um unittest, uma outra biblioteca nativa de Python mas que  é um pouco mais complexa do que o doctest.
Enquanto o doctest se baseia em comentários, o unittest precisa que uma classe seja declarada para poder interpretar a função à ser testada!
'''

import unittest
import funcao_unittest

class TestCalculator(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(funcao_unittest.soma(2, 3), 5)
        self.assertEqual(funcao_unittest.soma(-1, 1), 0)
    


if __name__ == "__main__":
    unittest.main()