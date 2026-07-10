# Recarregando módulos, importlib e singleton

import importlib

import aula158_m

print(aula158_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula158_m)

print('Fim')