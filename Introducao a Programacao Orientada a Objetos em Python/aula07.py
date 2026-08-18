# Atributos de classe

class Pessoa:
    ano_atual = 2026 #abributo de classe que podem ser usados em todas as instâncias que precisar

    def __init__(self, nome, idade, fez_aniversario):
        self.nome = nome
        self.idade = idade
        self.fez_aniversario = fez_aniversario

    def get_ano_nascimento(self):
        if self.fez_aniversario == 'Sim':
            return Pessoa.ano_atual - self.idade
        return Pessoa.ano_atual - (self.idade + 1)

p1 = Pessoa('Lucas', 25, 'Não')
p2 = Pessoa('Maria', 25, 'Sim')
p3 = Pessoa('Larissa', 18, 'Sim')

print(f'{p1.nome} nasceu no ano {p1.get_ano_nascimento()}')

print(f'{p2.nome} nasceu no ano {p2.get_ano_nascimento()}')

print(f'{p3.nome} nasceu no ano {p3.get_ano_nascimento()}')