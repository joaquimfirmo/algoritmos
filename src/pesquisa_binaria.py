
# Pesquisa Binária
# Algoritmo eficiente para encontrar um item em uma lista ordenada
# A pesquisa binária divide a lista em duas metades e compara o item procurado com o elemento do meio
# Se o item for menor que o elemento do meio, a pesquisa continua na metade inferior da lista
# Se o item for maior, a pesquisa continua na metade superior
# O processo se repete até que o item seja encontrado ou a lista seja reduzida a zero

# Exemplo de implementação em Python
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        palpite = lista[meio]

        if palpite == item:
            return meio
        if palpite > item:
            alto = meio - 1 
        else:
            baixo = meio + 1
    return None

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item = 7

resultado = pesquisa_binaria(lista, item)
if resultado is not None:
    print(f"Item encontrado na posição {resultado}.")
else:
    print("Item não encontrado na lista.")