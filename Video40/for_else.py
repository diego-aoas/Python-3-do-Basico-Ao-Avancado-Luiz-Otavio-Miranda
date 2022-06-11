"""
For / Else em Python
"""

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

## EXEMPLO 1
"""
for valor in variavel:
    print(valor)
    # continue
    break
    print(valor)
"""

## EXEMPLO 2
"""
for valor in variavel:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)
"""

## EXEMPLO 3

for valor in variavel:
    # print(valor)
    if valor.lower().startswith('j'):
        # break
        # pass
        continue
    print(valor)
# else:
#     print('Não existe uma palavra que começa com J.')
