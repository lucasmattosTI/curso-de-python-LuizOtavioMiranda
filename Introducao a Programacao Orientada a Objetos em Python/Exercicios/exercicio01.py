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

p1 = Pessoa('Lucas', 25)
p2 = Pessoa('Henrique', 15)
p3 = Pessoa('João', 18)
p4 = Pessoa('Larissa', 18)
bd = [vars(p1), vars(p2), vars(p3), vars(p4)]

with open(CAMINHO_ARQUIVO, 'w', encoding= 'utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)