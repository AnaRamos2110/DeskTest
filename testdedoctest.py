'''
O doctest é um módulo embutido no Python que permite testar o comportamento de funções, métodos ou classes diretamente a partir de exemplos escritos na docstring. 
Ele verifica se o código nos exemplos da docstring produz a saída esperada, funcionando como uma forma simples e eficaz de criar testes.
'''

def soma(a, b):
    """
    Soma dois números e retorna o resultado
    >>> soma (2, 3)
    5
    
    >>> soma (-1, 1)
    0
    """

    return a + b

 #Para verificar o teste mais complexo chamamamos no terminal : python -m doctest testa_doctest.py -v -- Pode usar o terminal padrão! 
 #O Pycash é opcional e não é obrigatório. Ele salva os dados do teste recém executado.