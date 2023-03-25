# Introdução ao try/except
# Try -> Tentar executar código
# Except -> ocorreu algum erro ao tentar executar

numero_str = input(
    'Drobarei o número que tu digitar: '
)

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número sua anta')