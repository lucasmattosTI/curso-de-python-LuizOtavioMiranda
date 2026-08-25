# Exercício com classes
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

onix = Carro('Onix')
chevrolet = Fabricante('Chevrolet')
motor_1_2_turbo = Motor('1.2 Turbo')

onix.fabricante = chevrolet
onix.motor = motor_1_2_turbo

print(f'O carro é {onix.nome}, o fabricante é {onix.fabricante.nome} e o motor é {onix.motor.nome}.')

prisma = Carro('Primas')
motor_1_0_Turbo = Motor('1.0 Turbo')

prisma.fabricante = chevrolet
prisma.motor = motor_1_0_Turbo

print(f'O carro é {prisma.nome}, o fabricante é {prisma.fabricante.nome} e o motor é {prisma.motor.nome}.')

toro = Carro('Toro')
fiat = Fabricante('Fiat')
motor_1_6_Turbo = Motor('1.6 Turbo')

toro.fabricante = fiat
toro.motor = motor_1_6_Turbo

print(toro.nome, toro.fabricante.nome, toro.motor.nome)