"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade:', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)