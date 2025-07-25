def eh_par(num):
    """
    Verifica se um número é par.

    >>> eh_par(13)
    False
    
    >>> eh_par(11)  #Quando adicionamos um número que o resultado vai gerar em falso, ele gera um relatório, se o código estiver sendo perfeitamente interpretado, ele não gera resultado.
    True

    >>> eh_par(-2)
    False

    >>> eh_par(0)
    True
    """
    return num % 2 == 0





