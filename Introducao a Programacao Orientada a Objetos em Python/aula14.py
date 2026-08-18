# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado

class Foo:
    def __init__(self):
        self.public = 'isso é público (public)'
        self._protected = 'isso é protegido (protected)'
        self.__private = 'isso é privado (private)'

    def metodo_public(self):
        self._metodo_protected()
        print(self._protected)
        self.__metodo_private()
        print(self.__private)
        return 'metodo é público'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
        


f = Foo()
print(f.public)
print(f.__metodo_private())
print(f.metodo_public())
