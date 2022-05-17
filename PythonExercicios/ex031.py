from datetime import date

n=int(input('Olá, digite o ano que você está! '))
if n==0:
    n=date.today().year

if n%4==0 and n%100!=0 or n%400==0:
    print('Esse é um ano bissexto!')
else:
    print('Esse não é um ano bissexto!')