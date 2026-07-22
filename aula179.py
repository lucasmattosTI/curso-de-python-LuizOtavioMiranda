# Salvando dados Python em JSON com módulo json
# JSON: JavaScript Object Notation
import json

# pessoa = {
#     'nome': 'Lucas',
#     'sobrenome': 'Coelho de Mattos',
#     'endereço': [
#         {'rua': 'R1', 'numero': 32} ,
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.79,
#     'numeros_preferidos': (2, 3, 7, 10),
#     'dev': True,
#     'nada': None,
# }
# 
# with open('aula179.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo, 
#         ensure_ascii=False,
#         indent=2
#     )

with open('aula179.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])