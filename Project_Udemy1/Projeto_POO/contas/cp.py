from contas.cliente import Conta


class ContaPoupanca(Conta):
    def __init__(self, conta, agencia, saldo):
        super().__init__(conta, agencia, saldo)
        self._saldo = saldo
        print(
            f'Sua conta é {self._conta}, agência {self._agencia} e seu saldo é {self._saldo}')


    def sacar(self, valor):

        if (self._saldo + self._limite) < valor:
            print(f'Não há saldo disponível')
        else:
            print(f'você sacou {valor}')
            self._saldo = (self._saldo + self._limite) - valor

    def extrato(self):
        print(f'Seu extrato é {self._saldo}')

    def deposito(self, valor):
        self._saldo += valor
        print(
            f'Seu saldo é {self._saldo}'
        )
