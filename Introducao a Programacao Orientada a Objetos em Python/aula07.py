# Atributos de classe

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade  = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Lucas', 25)
p2 = Pessoa('Larissa', 18)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print()
print(Pessoa.ano_atual)