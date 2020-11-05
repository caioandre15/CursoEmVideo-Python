import random

nomes = []
for i in range(4):
    nomes.append(input('Digite um nome de um aluno:'))

for i in range(1, 5):
    sorteio = random.randint(0, len(nomes)-1)
    print('{}º {}'.format(i, nomes[sorteio]))
    #print(nomes)
    del(nomes[sorteio])

