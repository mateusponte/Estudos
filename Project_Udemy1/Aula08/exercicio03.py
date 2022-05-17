def aumento (n1, n2):
    aumento = n1 + n1*n2
    print(f'O valor digitado foi {n1} e o aumento foi de {n2} o total é {aumento}')

aumento(n1=int(input('digite um valor: ')), n2=float(input('Digite um outro valor em porcentagem: ')))
