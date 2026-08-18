# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'João', 'idade': 35} # Dados do João

p1 = Pessoa(**dados) # Objeto p1 com os dados (dados do João) desempacotados
# p1.nome = 'Eita' -> Mudando o valor de um atributo de um objeto
# del . p1.nome -> deletando um atributo de um objeto

print(p1.__dict__) # Mostra como os valores de um objeto são armazenados (dicionário)
print(vars(p1)) # Também mostra o 'dict'
p1.__dict__['outra'] = 'coisa' # Adicionando um atributo e valor no objeto
p1.__dict__['nome'] = 'Lucas' # Mudando o valor de um atributo do objeto
print(vars(p1))
del p1.__dict__['outra'] # Deletando um atributo do objeto pelo dict
print(vars(p1))
