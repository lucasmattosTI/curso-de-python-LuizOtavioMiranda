# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs): # -> não recebe 'self' e nem 'cls'
        print('Método estático', args, kwargs) # -> é igual a uma função porém protegido pela classe

c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3, 'banana', [1, 'Ai pageeeéé', True], {'N': 24, 'M': 32}, (2, 25, 11))
Classe.funcao_que_esta_na_classe(nomeado = 'Lucas')