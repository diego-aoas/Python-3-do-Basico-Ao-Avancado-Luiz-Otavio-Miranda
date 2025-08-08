"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

'''
print(1324)
print(456)

int('a')
'''

numero_str = input('Vou dobrar o número que você digitar: ')

# numero_float = float(numero_str)
# print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')