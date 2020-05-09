# classe da Conta

class Conta():

    numeros_gerados = 0

    def __init__(self, agencia, cliente):
        Conta.numeros_gerados += 1
        self._agencia = agencia
        self._cliente = cliente
        self._numero_conta = Conta.numeros_gerados
        self._saldo = 0.0

    def __str__(self):
        return f'{self._agencia}\n{self._cliente}\nNumero da Conta: {self._numero_conta}\nSaldo: R$ {self._saldo}'

    def taxa_anual_conta(self):
        pass

    def deposita(self, valor):
        self._saldo += valor
        return True

    def sacar(self, valor):

        if self._saldo > 0 and self._saldo >= valor:
            self._saldo -= valor
            return True

        return False

    def tranferencia(self, conta, valor):

        if isinstance(conta, Conta):
            if self.sacar(valor):
                conta.deposita(valor)
                return True
        return False

class ContaCorrente(Conta):

    def __init__(self, agencia, cliente):
        super().__init__(agencia, cliente)

    def taxa_anual_conta(self):
        valor_desconto_anual = 5.0
        self._saldo -= valor_desconto_anual
        return True

class ContaFacil(Conta):


    def __init__(self, cliente, agencia = 22222):
        super().__init__(agencia, cliente)
        self.__saque_no_mes = 1
        self.__transferencia_no_mes = 1
        self.__limite_saldo = 5000.0

    def taxa_anual_conta(self):
        valor_desconto_anual = 10.00
        self._saldo -= valor_desconto_anual
        return True

    def deposita(self, valor):
        if self._saldo < 5000 and self.__limite_saldo >= valor:
            self._saldo += valor
            return True
        return False

    def sacar(self, valor):
        if ContaFacil.self.__saque_no_mes > 0 :
            ContaFacil.self.__saque_no_mes -= 1
            return super().sacar(valor)
        return False

    def tranferencia(self, conta, valor):
        if ContaFacil.self.__transferencia_no_mes > 0 :
            ContaFacil.self.__transferencia_no_mes -= 1
            return super().tranferencia(conta, valor)
        return False

class Poupanca(Conta):
    def __init__(self, agencia, cliente):
        super().__init__(agencia, cliente)

    def taxa_anual_conta(self):
        self._saldo *= (1 + 0.014)
        return True

    def sacar(self, valor):
        return False
