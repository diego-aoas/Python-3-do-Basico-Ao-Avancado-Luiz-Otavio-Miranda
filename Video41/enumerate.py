"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # srt
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
"""

## EXEMPLO 1
# string = "O Brasil é o pais do futebol, o Brasil é penta"
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

## EXEMPLO 2
lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

lista2 = ['Luiz', 'João', 'Maria']

for v in lista:
    print(v)

for indice, nome in enumerate(lista2):
    print(indice, nome)
