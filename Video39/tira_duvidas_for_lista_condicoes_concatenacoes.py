"""
secreto_temporario = ''
for letra_secreta in secreto:
    if letra_secreta in digitadas:
        secreto_temporario += letra_secreta
    else:
        secreto_temporario += '*'
"""
secreto = 'python'

secreto_temporario = ''

digitadas = ['o', 't', 'p', 'y', 'h']

for letra_secreta in secreto:
    print(f'Iteração para a letra {letra_secreta}')

    if letra_secreta in digitadas:
        print(f'Eba, a letra qeu eu queria {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        print(f'Essa letra eu não queria {letra_secreta}')
        secreto_temporario += '*'
    print('secreto_temporario=', secreto_temporario)

print()
print(secreto_temporario)

if secreto == secreto_temporario:
    print('Você ganhou!')
