class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calculo_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def exibir(self):
        print('Nome: ', self.nome)
        print('Nota1: ', self.nota1)
        print('Nota2: ', self.nota2)
        print('Media: ', self.media)

    def resultado(self):
        if self.media >= 6:
            print(f'Você foi aprovado')
        else:
            print(f'Você foi reprovado')


aluno1 = Aluno('Lucas', 6, 5)
aluno2 = Aluno('Maria', 10, 9)
aluno1.calculo_media()
aluno1.exibir()
aluno1.resultado()
