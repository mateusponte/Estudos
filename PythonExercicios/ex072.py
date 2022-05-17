#tupla
numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')

while True:
    n=int(input('digite um número entre 0 e 20: '))
    if n>=0 and n<=20:
        break

print(f'você digitou {numeros[n]}')