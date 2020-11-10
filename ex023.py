num = float(input('Digite um número entre 0 e 9999: '))

'''print('unidade: ', num[3])
print('dezena: ', num[2])
print('centena: ', num[1])
print('milhar: ', num[0])'''

a = num%10
b = num%100/10
c = num%1000/100
d = num%10000/1000

#Outra forma
'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10                              
m = num // 1000 % 10
'''

print('unidade: ', int(a))
print('dezena: ', int(b))
print('centena: ', int(c))
print('milhar: ', int(d))


