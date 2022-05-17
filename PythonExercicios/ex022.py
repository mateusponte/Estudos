num=int(input('digite um número com até quatro dígitos: '))
u= num // 1 % 10
d= num// 10 % 10
c= num // 100 % 10
m=num // 1000 % 10

print('Unidades: {} \n Dezenas: {}\nCentenas: {}\nMilhares: {}'.format(u, d, c, m))
