from sys import path

import aula159_package.modulo
from aula159_package import modulo
from aula159_package.modulo import soma_do_modulo

from aula159_package.modulo import *
print(variavel)

print(aula159_package.modulo.soma_do_modulo(3, 4))
print(modulo.soma_do_modulo(5, 6))
print(soma_do_modulo(1, 2))

print(soma_do_modulo(9, 10))