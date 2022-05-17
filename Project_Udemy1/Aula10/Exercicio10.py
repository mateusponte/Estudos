lista_tarefas = []

while True:
    print('Olá, seja bem vindo ao editor de tarefas!')
    print(f'Essas são suas tarefas: {lista_tarefas}')
    n=int(input('Olá, o que deseja fazer:\n 1 - adicionar tarefa\n 2 - Refazer tarefa\n 3 - Desfazer \n 4 - Sair\n'))
    if n not in [1, 5]:
        print('Opção não válida, tente novamente!')
        pass
    elif n == 1:
        tarefa = str(input('Digite sua tarefa: '))
        lista_tarefas.append(tarefa)
        pass
    elif n == 2:
        lista_tarefas.pop()
        tarefa = str(input('Digite sua tarefa: '))
        lista_tarefas.append(tarefa)
        print(lista_tarefas)
        pass
    elif n == 3:
        lista_tarefas.pop()
        print(lista_tarefas)
        pass
    elif n == 4:
        break

