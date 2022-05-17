#programa para ler nome e média do aluno e guardando também a situação em um dicionário
dados={}
dados['Nome']=str(input('Digite seu nome: ')).strip()
dados['Média']=float(input('Digite sua média: '))
if dados['Média']>= 7:
    print(f'Seu nome é {dados["Nome"]} \n Sua média foi {dados["Média"]}  e você está aprovado!')
else:
    print(f'Seu nome é {dados["Nome"]} \n Sua média foi {dados["Média"]} e você foi reprovado! Boa sorte na próxima!')
