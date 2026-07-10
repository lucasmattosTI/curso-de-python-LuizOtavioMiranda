"""
Considerando duas listas de inteiros ou flutuantes (lista A e lista B)
Alguns dos valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
=================== resultado
lista_soma = [2, 4, 6, 8]
"""

# Minha solução 
def soma_valores_lista(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        l1[i] + l2[i]
        for i in range(intervalo)
    ]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 5, 6 ,7, 8]

lista_de_somas = soma_valores_lista(lista_a, lista_b)
print(lista_de_somas)

# Solução do professor

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)