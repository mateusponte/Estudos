frase=str(input('digite um frase: ')).strip().upper()
palavras = frase.split() #quebra a palavras da frase
junto=''.join(palavras) #junta as palavras sem espaço
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso == junto:
    print('A frase é um palíndramo')
else:
    print('A frase não é um palíndramo')