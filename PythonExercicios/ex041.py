from datetime import date
ano=int(input('digite o ano de seu nascimento! '))
n=date.today().year
s=n-ano

if n-ano<=9:
    print('Você faz parte da categoria mirim!')
elif n-ano<=14 and n-ano>9:
    print('Você faz parte da categoria infantil!')
elif n-ano<=19 and n-ano>14:
    print('Você faz parte da categoria junior!')
elif n-ano<=20 and n-ano>19:
    print('Você faz parte da categoria sênior!')
elif n-ano>20:
    print('Você faz parte da categoria master!')
