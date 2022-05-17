l=float(input('digite a largura da parede: '))
h=float(input('digite a altura da parede: '))
A=h*l
print('Sua parede tem {:.2f} m² \n Você precisará de {:.2f} litros de tinta para pintá-la'.format(A,A/2))