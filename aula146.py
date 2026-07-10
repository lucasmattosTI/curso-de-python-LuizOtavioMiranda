# Dictionary comprehension e Set comprehension

# Dicionário

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
    if chave != 'categoria'

}

# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

print(dc)

# Set

s1 = {i for i in range(10)}
print(s1)