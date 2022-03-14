"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')

hora.isdigit()

try:
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('O horário não pode ter mais de 24 horas')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
except:
    print('O valor inserido não é hora')
