# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classe

class Pessoa:
    def __init__(self, nome, sobrenome):     # Na class usasse o 'def' para definir métodos, tipo como se fosse uma função
        self.nome = nome                     # O 'self' retorna o objeto da classe
        self.sobrenome = sobrenome          

p1 = Pessoa('Lucas', 'Mattos')
print(p1.nome, p1.sobrenome)

p2 = Pessoa('Luiz', 'Otávio')
print(p2.nome, p2.sobrenome)


'''
A classe é como se fosse o molde, o molde gera objetos;
Cada objeto tem um self que retorna ele dentro da classe;
O __init__ é um dos primeiros métodos a ser chamado numa 
classe para inicialiar os atributos da classe.
'''