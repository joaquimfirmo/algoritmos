# Este algoritmo ordena uma lista de números inteiros em ordem crescente
# usando o método de ordenação por seleção
# O algoritmo funciona da seguinte maneira:             
# 1. Cria uma nova lista vazia chamada novoArr
# 2. Enquanto a lista original arr não estiver vazia, ele encontra o menor elemento da lista
#    e o remove da lista original, adicionando-o à nova lista
# 3. O processo se repete até que a lista original esteja vazia
# 4. A nova lista ordenada é retornada



def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice



def ordenaPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr



print(ordenaPorSelecao([5, 3, 6, 2, 10,0,7,4,1,8,9]))