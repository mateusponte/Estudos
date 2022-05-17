palavra_secreta = 'sagitario'
digitadas = []
chances = 2

while True:
    if chances<=0:  #  verificar as chances de acertar a palavra
        print('Acabou suas chances!')
        break
    letra = input('Digite um letra: ')  #  recebe a variável que o usuário digitar
    digitadas.append(letra)  #  alimenta um lista com as variáveis digitadas
    if len(letra) >1: #proibe o usuário de digitar mais  de uma letra
        print('Digite apenas uma letra!')
        continue
    if letra in palavra_secreta:  #  verifica a condição de existência da variável na palavra secreta
        print(f'A letra {letra} existe na palavra secreta!')
    else:
        print(f'A letra {letra} não existe na palavra secreta!')
        chances -= 1
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == palavra_secreta:
        print(f'Você acertou a palavra {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
