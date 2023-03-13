"""
Formatando valores com modificadores - Aula 05

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE/TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""


nome = 'Marcondes'
print(f'{nome:@^20}')