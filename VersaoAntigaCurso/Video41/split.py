"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # srt
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
"""
string = "O Brasil é o pais do futebol, o Brasil é penta"
lista_1 = string.split(' ')
print(lista_1)
lista_2 = string.split(',')
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    # print(valor)
    # print(f'A palavra "{valor}" apareceu {lista_1.count(valor)} x')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

for valor in lista_2:
    print(valor.strip().capitalize())
