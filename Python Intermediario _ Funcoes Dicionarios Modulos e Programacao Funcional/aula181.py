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


#    if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'cls':
#         os.system('cls')
#         continue
#     elif tarefa == 'sair':
#         break
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue