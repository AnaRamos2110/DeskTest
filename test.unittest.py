import unittest
import unittest_funcao_divisao
class Divisao_test(unittest.TestCase): #Criando a classe para realizar os testes
    def test_soma(self):
        # Sobre o assertEqual: Ele é uma assertiva que verifica se dois valores são iguais. Se os valores comparados não forem iguais, o teste falha e uma mensagem de erro é exibida.
        self.assertEqual(unittest_funcao_divisao.divisao(10, 5),2 )   #Número inteiro 
        self.assertEqual(unittest_funcao_divisao.divisao(0, 25), 0) #Dividindo zero
        self.assertEqual(unittest_funcao_divisao.divisao(25, 0), "Erro de divisão; Não é possivel dividir por zero.") #Verificando se a trativa de erro vai ser chamada.
        self.assertEqual(unittest_funcao_divisao.divisao(10, 2.5), 4) #Testando números decimais


if __name__ == "__main__":
    unittest.main()
