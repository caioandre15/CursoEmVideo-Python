import random

nomes = []
for i in range(4):
    aluno = input('Digite um nome de aluno: ')
    nomes.append(aluno)

sorteio = random.randint(1, 4)

print('O aluno escolhido foi: ', nomes[sorteio])


