# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carro = None
    
   

nivus, onix, fastback, virtus = Carro('Nivus'), Carro('Onix'), Carro('Fastback'), Carro('Virtus')
motor_1_0_turbo, motor_1_2_turbo = Motor('1.0 Turbo'), Motor('1.2 Turbo')
fiat, chevrolet, volkswagen = Fabricante('Fiat'), Fabricante('Chevrolet'), Fabricante('Volkswagen')

nivus.motor = motor_1_0_turbo
nivus.fabricante = volkswagen

print(f'O carro {nivus.nome} fabricado pela {nivus.fabricante.nome} tem o motor {nivus.motor.nome}.')
print()

onix.motor = motor_1_0_turbo
onix.fabricante = chevrolet

print(f'O carro {onix.nome} fabricado pela {onix.fabricante.nome} tem o motor {onix.motor.nome}.')
print()

fastback.motor = motor_1_2_turbo
fastback.fabricante = fiat

print(f'O carro {fastback.nome} fabricado pela {fastback.fabricante.nome} tem o motor {fastback.motor.nome}.')
print()

virtus.motor = motor_1_2_turbo
virtus.fabricante = volkswagen

print(f'O carro {virtus.nome} fabricado pela {virtus.fabricante.nome} tem o motor {virtus.motor.nome}.')
