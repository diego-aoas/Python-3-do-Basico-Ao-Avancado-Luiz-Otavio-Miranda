"""
Manipulando strings
* String indices
* Fatiamento de Strings
"""

texto = 'Python s2'

nova_string = texto[:2]  # pega da posição 0 até 1
print(nova_string)
nova_string = texto[1:3]  # pega da posição 1 até a 2
print(nova_string)
nova_string = texto[3:]  # pega da posição 3 até o fim
print(nova_string)
nova_string = texto[0:6:2]  # pega da posição 0 até a 5 pulando de 2 em 2
print(nova_string)
