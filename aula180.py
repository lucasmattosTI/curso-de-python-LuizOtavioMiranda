# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None): # Inicia a lista com None
    if lista is None: # Se lista for None
        lista = [] # Cria uma nova lista
    lista.append(nome) # Adiciona elemento
    return lista # Retorna a lista

clientes1 = adiciona_clientes('Lucas')
adiciona_clientes('Henrique', clientes1)
adiciona_clientes('João Pedro', clientes1)
adiciona_clientes('Otávio', clientes1)

clientes2 = adiciona_clientes('Larissa')
adiciona_clientes('Jhenifer', clientes2)
adiciona_clientes('Emilly', clientes2)
adiciona_clientes('Milena', clientes2)
adiciona_clientes('Ariane', clientes2)

print(clientes1)
print(clientes2)