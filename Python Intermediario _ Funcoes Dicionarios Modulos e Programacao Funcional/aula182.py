# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve POSICIONAL
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores. NOMEADOS
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma1(a, b, /, x, y):  # Antes da (/) deve ser somente posicional
    print(a + b + x + y)

soma1(1, 2, y = 4, x = 3)

def soma2(a, b, *, c): #Após o (*) deve ser nomeado
    print(a + b + c)
soma2(1, 2, c = 3)

def soma3(a, b, /, *, c, d):
    print(a + b + c + d) 
soma3(1, 2, c = 3, d = 4)