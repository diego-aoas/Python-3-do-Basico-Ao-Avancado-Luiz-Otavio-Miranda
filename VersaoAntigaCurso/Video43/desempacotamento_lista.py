"""
Desempacotamento de listas em Python
"""

lista = ['Luiz', 'João', 'Maria']

# n1, n2, n3 = lista
n1, n2, *outra_lista = lista  # O * outra lista gera uma nova lista que não engloba os outros elementos

print(n2)
print(outra_lista)
