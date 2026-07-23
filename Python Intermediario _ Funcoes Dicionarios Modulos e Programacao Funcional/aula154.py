# Try, except, else e finally + Built-in Exceptions
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('Abrir arquivo')
    8 / 0
    
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

else:
    print('Não deu erro')

finally:
    print('FECHAR ARQUIVO')