# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno
    


# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor B'

    def __init__(self, atributo, qualquer_coisa):
        super().__init__(atributo)
        self.qualquer_coisa = qualquer_coisa

    def metodo(self):
        # super().metodo()
        print('B')

class C(B):
    atributo_c = 'valor C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlei o sistema!')

    def metodo(self):
        # super(B, self).metodo() # Aqui o super é o A
        super().metodo() # Aqui p super é o B
        # super(A, self).metodo() # Aqui p super é o object
        print('C')

c = C('Atributo', 'Qualquer coisa')

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

# c.metodo()
# print(C.mro())
# print(B.mro())

print(c.atributo)
print(c.qualquer_coisa)