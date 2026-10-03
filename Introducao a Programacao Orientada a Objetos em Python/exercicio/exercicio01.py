# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'Introducao a Programacao Orientada a Objetos em Python/exercicio/exercicio01.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Lucas', 26)
p2 = Pessoa('Larissa', 18)
p3 = Pessoa('Henrique', 15)
p4 = Pessoa('Flávia', 30)

bd = [vars(p1), vars(p2), vars(p3), vars(p4)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii = False, indent = 2)