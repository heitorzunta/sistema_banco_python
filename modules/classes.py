# Classes referentes ao módulo bancário

# Classe Endereco
class Endereco():
    def __init__(self, rua, numero, cep, complemento = 'casa'):
        self.rua = rua
        self.cep = cep
        self.__numero = self.add_numero(numero)
        self.complemento = complemento

    def add_numero(self, numero):
        if(numero.isnumeric()):
            self.numero = numero
        else:
            self.numero = 0

    def __str__(self):
        return f'Rua: {self.rua} - n.o: {self.numero} - Cpl: {self.complemento} - CEP: {self.cep} '

# Classe Cliente:  cliente que é representado através de seu nome, endereço, data nascimento, cpf e tipo de cliente.
class Cliente():
    def __init__(self, nome, data_nascimento, cpf, tipo_cliente = 'Normal'):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self.tipo_cliente = tipo_cliente
        self.endereco = []

    def addEndereco(self, rua, cep, numero, complemento):
        self.endereco.append(Endereco(rua, cep, numero, complemento))

##################

cliente1 = Cliente('Heitor Batistela Zunta', '26/11/1983', '996828421-15')
cliente1.addEndereco('Rua Bangu', "121", "791121-210", 'casa' )

for endereco in cliente1.endereco:
    print(endereco)
