from abc import ABC


class Conta(ABC):
    def __init__(self, conta, agencia, saldo):
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return saldo._saldo

    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
