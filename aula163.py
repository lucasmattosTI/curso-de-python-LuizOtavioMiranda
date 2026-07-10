# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func): # Função decoradora: ela recebe uma função, cria uma função interna para
    # ter uma cloger, e essa função não será executada, apenas retornada para ser executada posteriormente.
    # Na decoração desta função, podemos fazer coisas antes ou depois do resultado.

    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        # resultado += 'Qualquer coisa'
        print(f'Ok, você foi decorada, e o seu resultado será "{resultado}".')
        return resultado
    return interna

def e_string(param):
     if not isinstance(param, str):
         raise TypeError('Parâmetro deve ser uma string')

@criar_funcao # Decorador
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

# inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('Lucas')
print(invertida)

