largura = float(input('Qual é a largura da parede: '))
altura = float(input('Qual é a altura: '))
area = largura*altura
qtdeDeTinta = area/2
print('Area: {}\n'
      'Serão necessários {:.2f} litros de tinta, para pintar a sua parede.'.format(area, qtdeDeTinta))
