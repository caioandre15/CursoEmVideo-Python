from math import hypot
catetoOposto = float(input('Digite a medida do cateto oposto: '))
catetoAdjacente = float(input('Digite a medida do cateto adjacente: '))
print('Comprimento da hipotenusa é: {:.2f}'.format(hypot(catetoOposto,catetoAdjacente)))