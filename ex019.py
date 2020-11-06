from random import choice

nomes = []
for i in range(4):
    aluno = input('Digite um nome de aluno: ')
    nomes.append(aluno)

print('O aluno escolhido foi: ', choice(nomes))


