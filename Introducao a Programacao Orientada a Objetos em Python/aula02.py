# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classe

class Pessoa: # Classe
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Lucas', 'Mattos') # Objeto 1
# p1.nome = 'Lucas' # Atributo 1
# p1.sobrenome = 'Mattos' # Atributo 2

p2 = Pessoa('Wesley', 'Gomes') # Objeto 2
# p2.nome = 'Larissa' # Atributo 1
# p2.sobrenome = 'Cordeiro' # Atributo 2

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)