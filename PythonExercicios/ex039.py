from datetime import date

ano=int(input('Digite o ano que você nasceu: '))
n=date.today().year
s=n-ano

if n-ano>18:
    print('Você passou {} anos do prazo para se alistar'.format(s))
elif n-ano==18:
    print('Você deve ser alistar!')
elif n-ano<18:
    print('Você ainda não precisa se alistar, ainda falta {} anos para você se alistar'.format(s))

