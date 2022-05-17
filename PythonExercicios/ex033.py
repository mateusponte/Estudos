sal=float(input('Olá, digite o valor do seu salário! '))
if sal>1250:
    sal=sal*1.10
    print('Seu salário será {:.2f}'.format(sal))
else:
    sal=sal*1.15
    print('Seu salário será {:.2f}'.format(sal))