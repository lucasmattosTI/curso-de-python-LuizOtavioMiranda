def buscar_menor(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(lista):
    lista_ordenada = []
    for i in range(len(lista)):
        menor = buscar_menor(lista)
        lista_ordenada.append(lista.pop(menor))
    return lista_ordenada

def pesquisa_binaria(lista, item):
    lista_ordenada = ordenacao_por_selecao(lista)
    baixo = 0
    alto = len(lista_ordenada) - 1
    while baixo <= alto:
        meio = (baixo + alto) % 2
        chute = lista_ordenada[meio]
        if chute == item:
            return meio, lista_ordenada
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None, lista_ordenada


lista = [5, 3, 6, 2, 10]
item = 6

indice, lista_ordenada = pesquisa_binaria(lista, item)
print(f'Lista ordenada: {lista_ordenada}')
print()
if indice is not None:
    print(f'O número procurado ({lista_ordenada[indice]}) está na posição {indice} na lista.')