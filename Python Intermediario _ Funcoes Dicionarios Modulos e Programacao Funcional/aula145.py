# List comprehension com mais de um for

lista1 = []
for x in range(3):
    for y in range(3):
        lista1.append((x, y))
print(lista1)

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista2)


lista_nome = [
    [letra for letra in 'Larissa']
    for x in range(5)
]

print(lista_nome)