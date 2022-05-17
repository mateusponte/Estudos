def funcao1(*args, **kwargs):  #  rever essa ula e a lógica
    n = funcao2(*args, **kwargs)
    print(f'Exibir {n}')
    m = funcao3(*args,**kwargs)
    print(f'Mostrar {m}')


def funcao2(k,l):
    return k*l

def funcao3(f, g, h):
    return (f*g/h)


funcao1(funcao2(1, 2), funcao3(1, 2, 4))