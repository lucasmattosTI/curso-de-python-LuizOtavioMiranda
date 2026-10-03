# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2026 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # decorator - o método passa a ser um método de classe
    def metodo_de_classe(cls):  # recebe a classe
        print('Olá!')

    @classmethod
    def sabor_dezoito(cls, nome):
        return cls(nome, 18)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo', idade)

p1 = Pessoa('Lucas', 26)
p2 = Pessoa.sabor_dezoito('Larissa')
p3 = Pessoa.criar_anonimo(42)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

# p1.metodo_de_classe()
Pessoa.metodo_de_classe()