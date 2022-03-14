"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num1 = input('Digite um número inteiro: ')

num1.isdigit()
try:

    num1 = int(num1)

    if num1 % 2 == 0:
        print(f'O {num1} é um número par.')
    else:
        print(f'O {num1} é um número ímpar.')
except:
    print(f'{num1} não é um número inteiro')
