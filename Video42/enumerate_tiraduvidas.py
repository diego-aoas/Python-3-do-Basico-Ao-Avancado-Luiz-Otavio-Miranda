"""
* Enumerate - Enumerar elementos da lista # list
"""

lista = [
    # 0      1        2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Lu']  # 2
]

# print(lista[1][2])

# enumerada = enumerate(lista)
# print(list(enumerada))

enumerada = list(enumerate(lista))
print((enumerada[1][1][2]))
