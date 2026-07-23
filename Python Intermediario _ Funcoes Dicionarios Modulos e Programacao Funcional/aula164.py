# Decoradores com parâmetros

def fabrica_de_decoradores(a=None, b=None, c=None): #Pega os parâmetros do decorador
    def fabrica_de_funcoes(func): # Decorador (Recebe uma função)
        print('Decoradora 1')

        def aninhada(*args, **kargs): #Função que será executada
            print('Parâmetros do decorador: ',a, b, c)
            print('Aninhada')
            res = func(*args, **kargs)
            return res 
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores('Larissa', 'sabor', 'te quer')
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5) 
print(dez_mais_cinco)
print(dez_vezes_cinco)