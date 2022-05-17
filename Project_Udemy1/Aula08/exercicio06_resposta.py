def mestre(funcao, *args, **kwargs):
    return funcao(*args,**kwargs)


def fala_oi(nome):
    return f'Oi, {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

executando = mestre(fala_oi, 'Mateus')

executando2 = mestre(saudacao, 'Mateus', 'Olá')

print(executando)
print(executando2)