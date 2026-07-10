# O ponto de vista do __main__ pode te confundir em módulos e pacotes Python
print(__name__)

from aula159_package.modulo import soma_do_modulo

# Importando um módulo que importou de outro módulo