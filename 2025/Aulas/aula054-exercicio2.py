"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são? ')

try:
    horario_int = int(horario)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom dia!')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa tarde.')
    elif horario_int >= 18 and horario_int <= 23:
        print('Boa noite.')
    else:
        print('Não conheço essa hora.')
except:
    print('Digite um número inteiro.')