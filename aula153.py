# Try, except, else e finally

try:
    a = 10
    b = 0
    #print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

except NameError:
    print('Nome b não está definido.')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Mensagem:', error)
    print('Nome:', error.__class__.__name__)

print('CONTINUAR')