# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import os

caminho_arquivo = 'D:\\Nuvem\\ESTUDOS PROGAMAÇÂO\\Python\\Curso de Python - Otavio Miranda\\arquivos\\'
caminho_arquivo += 'aula174.txt'
print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n', 'Linha 5\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print()
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print()
#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
# 
# print('#' * 10)
# 
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # Cria e escreve no arquivo ou apaga o que já exite e reescreve
#     arquivo.writelines(
#         ('Atenção', ', o show vai começar\n')
#     )
# with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo: # Adiciona coisas no arquivo
#     arquivo.writelines(
#         ('Primeira música!')
#     )

# os.remove(caminho_arquivo) # Remove o arquivo - remove ou unlink
os.rename(caminho_arquivo, 'D:\\Nuvem\\ESTUDOS PROGAMAÇÂO\\Python\\Curso de Python - Otavio Miranda\\arquivos\\Sabor_18.txt')