from contas.cliente import Conta


class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo, limite=100):
        super().__init__(conta, agencia, saldo)
        self._saldo = saldo
        self._limite = limite
        val = self.valida(self._conta, self._agencia)
        if val is True:
            print(
                f'Sua conta é {self._conta}, agência {self._agencia} e seu saldo é {self._saldo} com limite de {self._limite}')
        else:
            print(f'Seus dados não estão cadastrados em nosso sistema')

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):

        if (self._saldo + self._limite) < valor:
            print(f'Não há saldo disponível')
        else:

            self._saldo = self._saldo - valor
            print(f'você sacou {valor} seu saldo é {self._saldo}')
    def extrato(self):
        print(f'Seu extrato é {self._saldo}')

    def deposito(self, valor):
        self._saldo += valor
        print(
            f'Seu saldo é {self._saldo}'
        )

    def valida(self, conta, agencia):
        if conta == 1234 and agencia == 8448:
            return True
        else:
            return False
