# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Lucas', 26)
print(p1.__dict__)
print(vars(p1))
print(p1.nome)
p1.__dict__['Sexo'] = 'Masculino'
p1.__dict__['nome'] = 'João'
print(vars(p1))
# p1.nome = 'Mudei o nome'
print(p1.nome)