import os 
import json

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding = 'utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding = 'utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent= 2, ensure_ascii= False)
    return dados

CAMINHO_ARQUIVO = 'D:\\Nuvem\\ESTUDOS PROGAMAÇÂO\\Python\\Curso de Python - Otavio Miranda\\Exercicios\\exercicio09.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa=} removida da lista de tarefas.')
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas')
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'cls': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas)
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)