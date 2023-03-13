"""
While em Python - Aula 7

continue - ignora o que está abaixo dele
break - finaliza o loop
"""

### Exemplo 1

# while True:  # loop infinito
#     nome = input("Qual o seu nome? ")
#     print(f'Olá {nome}!')

### Exemplo 2

# x = 0
# while x < 5:
#     print(x)
#     x = x + 1
# print('Acabou!')

### Exemplo 3

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         continue
#
#     print(x)
#     x = x + 1

### Exemplo 4

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break
#
#     print(x)
#     x = x + 1

### Exemplo 5

# x = 0
#
# while x < 10:
#     y = 0
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
#         y += 1
#     x += 1
#
# print('Acabou!')

### Exemplo 6

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print('Resultado:', num_1 + num_2)
    elif operador == '-':
        print('Resultado:', num_1 - num_2)
    elif operador == '/':
        print('Resultado:', num_1 / num_2)
    elif operador == '*':
        print('Resultado:', num_1 * num_2)
    else:
        print('Operador inválido')

    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
