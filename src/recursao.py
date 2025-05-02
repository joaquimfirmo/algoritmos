# Recursão é um conceito fundamental em programação, onde uma função chama a si mesma para resolver um problema.
# A recursão é uma técnica poderosa que pode simplificar a solução de problemas complexos, tornando o código mais legível e fácil de entender.

# A baixo um exemplo de uma função recursiva simples que calcula o fatorial de um número inteiro positivo.


# O fatorial de um número n é o produto de todos os números inteiros de 1 a n.
# Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.
# A função fatorial(n) chama a si mesma com o valor n - 1 até que n seja igual a 1, momento em que retorna 1.
# A cada chamada recursiva, o valor de n diminui em 1, e a função continua a multiplicar os valores até que o resultado final seja obtido. 
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    




print(fatorial(4))    