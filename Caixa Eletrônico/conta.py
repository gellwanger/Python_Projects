from pyrsistent import v


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Imprimindo objeto...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo R${} do titular {}'.format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, origem, destino):
        origem.saque(valor)
        destino.deposito(valor)
        