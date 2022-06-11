nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # delimita 2 pontos flutuantes
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))