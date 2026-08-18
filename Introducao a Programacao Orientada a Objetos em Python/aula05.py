# Escopo da classe e de métodos da class

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        # print(varivel) -> não consigo acessa 'variavel' pois ela não faz parte do escopo deste método
        return f'{self.nome} está comendo {alimento}' # -> usando o self, consigo ter acesso a coisas que está no escopo da classe

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

# print(Animal.nome) -> uma forma de retorna um atributo direto da classe

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('uva'))