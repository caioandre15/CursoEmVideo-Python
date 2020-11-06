from math import sin, cos, tan, radians
a = float(input('Digite um ângulo qualquer: '))
print('Ângulo {:.2f}\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
