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

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel_saque)  

    def saque(self, valor):
        if(self.pode_sacar):
            self.__saldo -= valor
        else:
            print('O valor {} passou do limite'.format(valor))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'
