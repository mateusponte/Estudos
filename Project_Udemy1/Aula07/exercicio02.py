#programa para dizer se um número é par ou ímpar

num=input('Olá, digite um número inteiro: ')

if num.isdigit():

    if int(num) % 2 == 0:
        print(f'{num} é um número par')
    else:
        print(f'{num} é um número ímpar')
else:
    print('Não é um número inteiro')
