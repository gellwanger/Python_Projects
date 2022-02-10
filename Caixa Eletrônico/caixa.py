def cria_conta(numero, titular, saldo, limite):
    conta = {'número': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor
    return conta

def extrato(conta):
    print('Saldo {}'.format(conta['saldo']))

