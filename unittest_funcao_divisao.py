def divisao(a, b):          #Criando a função e estabelecendo parâmetros
        if b == 0:
              try:
                     a / b
              except ZeroDivisionError:          #Condição para caso o divisor seja igual a zero
                return "Erro de divisão; Não é possivel dividir por zero." #Gerando uma tratativa de erro com a função print para ficar mais intuitivo ao usuário para não tentar passar o número 0 no parâmetro do divisor.
        else:
                return a / b #Sen~so tiver 0 na conta, o else retorna os números que você inseriu na função.
    


#print(divisao(2, 2)) -- PARA TESTAR SE A FUNÇÃO APARECE QUANDO VOCê CHAMA ELA, O PRINT É SIMPLES DEMAIS DEPENDENDO DO QUE VOCÊ QUER TESTAR, 