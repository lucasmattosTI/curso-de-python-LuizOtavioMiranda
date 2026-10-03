class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter -> obtem valor
    @property
    def preco(self):
        return self._preco

    # Setter -> configura valor
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('camiSetA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('bolsA', "R$35")
p2.desconto(5)
print(p2.nome, p2.preco)