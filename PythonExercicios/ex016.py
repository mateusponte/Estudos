from math import hypot
from math import sqrt

n1=float(input('digite o valor de um cateto: '))
n2=float(input('digite o valor do outro cateto: '))
hyp=sqrt(n1**2+n2**2)
print('O valor da hipotenusa do triângulo é: {:.2f}'.format(hyp))
print('O valor da hipotenusa do triângulo é: {:.2f}'.format(hypot(n1,n2)))