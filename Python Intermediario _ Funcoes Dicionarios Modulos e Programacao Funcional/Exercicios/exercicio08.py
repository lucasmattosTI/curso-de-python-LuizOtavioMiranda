# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os 

tarefas = []
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

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas')
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'cls':
        os.system('cls')
        continue
    elif tarefa == 'sair':
        break
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue