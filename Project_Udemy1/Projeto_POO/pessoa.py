# classe para pessoas
from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
        print(f'Olá, {self._nome}')

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("Nome precisa ser uma string")
        else:
            self._nome = nome

    @idade.setter
    def idade(self, idade):
        if not isinstance(idade, int):
            raise ValueError("Idade precisa ser um inteiro")
        else:
            self._idade = idade
