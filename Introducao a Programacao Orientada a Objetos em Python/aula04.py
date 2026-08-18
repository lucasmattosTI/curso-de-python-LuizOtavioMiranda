# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
 
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('fusca')
# fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro('Celta')
Carro.acelerar(celta) #-> é a mesma coisa que eu fazer: celta.acelerar()
