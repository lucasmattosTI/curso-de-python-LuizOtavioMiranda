# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
#string = 'Luiz'  # str
#print(string.upper())
#print(isinstance(string, str))

class Pessoa: # Classe
    ... 

p1 = Pessoa() # Objeto 1
p1.nome = 'Lucas' # Atributo 1
p1.sobrenome = 'Mattos' # Atributo 2

p2 = Pessoa() # Objeto 2
p2.nome = 'Larissa' # Atributo 1
p2.sobrenome = 'Cordeiro' # Atributo 2  '

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)