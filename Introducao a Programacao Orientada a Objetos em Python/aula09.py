# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2026 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_de_instancia(self):
        print('Método de instância') # -> recebe self

    @classmethod # -> o método passa a ser um método de classe
    def metodo_de_classe(cls): # -> O método vai precisar receber a própria classe 'cls'
        print('Método de classe')

    # Fábrica de objetos

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo', idade)
    
# print(Pessoa.ano) -> imprimindo um atributo de Classe

p1 = Pessoa('Lucas', 25)
p1.metodo_de_instancia()
Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos('Larissa')
print(p2.nome, p2.idade)
p3 = Pessoa.criar_anonimo(23)
print(p3.nome, p3.idade)