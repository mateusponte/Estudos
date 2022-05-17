from pessoa import Pessoa
from contas.cc import ContaCorrente
from contas.cp import ContaPoupanca

a = Pessoa('Mateus', 23)
b = ContaCorrente(1234, 8448, 100)
c = ContaPoupanca(1234,8448,500)

b.deposito(300)
b.sacar(250)