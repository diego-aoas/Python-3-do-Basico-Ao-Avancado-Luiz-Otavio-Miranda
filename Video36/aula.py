#       Índices
#       0123456789........................34

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
# print(tamanho_frase)
contador = 0
nova_string = ''
# print(frase[])

### EXEMPLO 1:
# while contador < 10:
#     print(contador)
#     contador += 1

### EXEMPLO 2:
# while contador < tamanho_frase:
#     # print(frase[contador],contador)
#     nova_string += frase[contador]
#     print(nova_string)
#     contador += 1
#
# print(nova_string)

### EXEMPLO 3:
input_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)

