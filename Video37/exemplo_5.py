"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'

## EXEMPLO 1
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

## EXEMPLO 2
# Mesma coisa que:
# for letra in texto:
#     print(letra)

## EXEMPLO 3
# for n, letra in enumerate(texto):
#     print(n, letra)

## EXEMPLO 4
# for numero in range(10):
#     print(numero)

## EXEMPLO 5
# for numero in range(20, 10, -1):
#     print(numero)

## EXEMPLO 6

# continue - pula para o próximo laço
# break - termina o laço

nova_string = ""

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string = nova_string + letra.upper()
    else:
        nova_string += letra

print(nova_string)
