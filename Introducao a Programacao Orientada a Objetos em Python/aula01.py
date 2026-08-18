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
    # dados dentro de uma classe são atributos
    # ações (funções) dentro de uma classe são métodos

p1 = Pessoa() # Instância da classe ou objeto
p1.nome = 'Lucas' # atributos
p1.sobrenome = 'Mattos' # atributos
print(p1.nome, p1.sobrenome)

p2 = Pessoa() # Nova instância da classe ou um novo objeto
p2.nome = 'Larissa'
p2.sobrenome = 'Cordeiro'
print(p2.nome, p2.sobrenome)