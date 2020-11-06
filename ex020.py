from random import shuffle

nomes = []
for i in range(4):
    nomes.append(input('Digite um nome de um aluno:'))
shuffle(nomes)
print('A ordem da apresentação será: ')
print(nomes)


