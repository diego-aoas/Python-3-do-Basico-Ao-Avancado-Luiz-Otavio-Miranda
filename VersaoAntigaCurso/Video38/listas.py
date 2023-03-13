"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

## EXEMPLO 1
# booleanos = True
# inteiros = 10
# flutuante = -10.10
# strings = 'Textos'
# # lista = [1, 2, 3, 4, 'Luiz Otávio', True, 10.5]
#
# #         0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']
# #        -5   -4   -3   -2   -1
#
# string = 'ABCDE'
#
# print(string[1])
# print(lista[::2])
# print(lista[::-1])

## EXEMPLO 2

# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# # l3 = l1 + l2
# # l1.extend(l2)
# l1.extend('a')
#
# print(f'Limpo: {l2}')
#
# l2.append('b')  # para adicionar no final da lista utiliza append
# print(f'Append "b", mostrando índice 3: {l2[3]}')
# print(f'Append l2 completo: {l2}')
#
# l2.insert(0, "banana")  # insere no índice determinado o valor
# print(f'Insert "banana" índice 0: {l2}')
#
# l2.pop()  # remove item da lista
# print(f'Pop: {l2}')
#
# # print(l1)
# # print(l2)
# # print(l3)
#
# l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'l4 limpo: {l4}')
#
# del (l4[3:5])  # Deleta itens do indice, lembrando que o último não é excluído.
# print(f'del de l2 3 a 5: {l4}')
# print(f'Valor Máximo de l4: {max(l4)}')
# print(f'Valor Minimo de l4: {min(l4)}')
#
# l5 = list(range(1, 10))
# print(f'Fazendo uma lista de um range: {l5}')
#
# l6 = list(range(1, 100, 8))
# # print(l6)
#
# # for valor in l6:
# #     print(valor)
#
# l7 = ['String', True, 10, -20.5]
#
# for elem in l7:
#     print(f'O tipo de {elem} é {type(elem)}')

## EXEMPLO 3

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu...')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUUL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.\n')
