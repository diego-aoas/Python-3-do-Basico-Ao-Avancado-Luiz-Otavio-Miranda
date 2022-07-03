"""
Funções - def em Python (Parte 1)
"""


## EXEMPLO 1
# def funcao():
#     print('Hello World!')
#
#
# funcao()
# funcao()


## EXEMPLO 2
# def saudacao(msg='Olá', nome='usuário'):  # Valor padrão
#     nome = nome.replace('e', '3')
#     msg = msg.replace('e', '3')
#     print(msg, nome)
#
#
# saudacao(nome='Zezinho', msg='Hi')
# saudacao('Olá', 'Luiz Otávio')
# saudacao('Oi', 'Luiz')
# saudacao('Hello', 'Maria')
# saudacao('Olá', 'Otávio')
# saudacao('Olá', 'João')

## EXEMPLO 3
def saudacao(msg='Olá', nome='usuário'):  # Valor padrão
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()

print(variavel)
