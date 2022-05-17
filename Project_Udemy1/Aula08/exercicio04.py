#exercicio função FizzBuzz

def fizzbuzz(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        print('FizzBuzz')
    elif n1 % 5 == 0:
        print('Buzz')
    elif n1 % 3 == 0:
        print('Fizz')
    else:
        print(n1)

fizzbuzz(n1 = int(input('Digite um número: ')))