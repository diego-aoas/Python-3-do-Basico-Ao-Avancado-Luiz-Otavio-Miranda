"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo'

print(variavel[5])
print(variavel[4:])
print(variavel[4:8])
print(variavel[:5])

print(len(variavel))
print(variavel[0:len(variavel):1]) # o passo (final :1) é de quantos em quantos
print(variavel[0:9:2])
print(variavel[0:9:4])
print(variavel[::-1])