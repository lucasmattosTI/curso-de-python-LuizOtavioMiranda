# dir, hasattr e getattr em Python

string = 'Lucas'

# rint(dir(string))

metodo = 'upper'

if hasattr(string, metodo):
    print('Existe o método upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)