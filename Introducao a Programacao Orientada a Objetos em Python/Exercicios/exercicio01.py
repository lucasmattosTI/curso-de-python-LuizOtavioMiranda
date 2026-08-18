# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'D:\\Nuvem\\ESTUDOS PROGAMAÇÂO\\Python\\Curso de Python - Otavio Miranda\\Introducao a Programacao Orientada a Objetos em Python\\Exercicios\\exercicio01.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João Pedro', 15)
p2 = Pessoa('Larissa', 18)
p3 = Pessoa('Lucas', 25)

bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding= 'utf-8') as arquivo:
    print('FAZENDO DUMP')
    json.dump(bd, arquivo, ensure_ascii= False, indent = 2)