primeiro = int(input('Digite um valor: '))
segundo = int(input('Digite outro valor: '))

if primeiro > segundo:
    print(f'{primeiro=} é maior do que {segundo=}')
elif primeiro == segundo:
    print(f'{primeiro=} é igual ao {segundo=}')
else:
    print(f'{segundo=} é maior do que {primeiro=}')