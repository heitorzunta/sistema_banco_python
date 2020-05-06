from datetime import date

# Classes referentes ao módulo bancário

#classe CPF

class Cpf():
    def __init__(self):
        pass

    def validar_cpf(self, cpf):
        validar_1 = False
        validar_2 = False
        soma = 0

        #remover . e - do cpf
        if not cpf.isdigit():
            cpf = cpf.replace('.', '', len(cpf))
            cpf = cpf.replace('-', '', len(cpf))

        #verifica quantidade de digito
        if len(cpf) != 11:
            raise ValueError

        parte1 = cpf[:9]
        parte2 = cpf[:10]

        #validacao da parte 1
        for digito in parte1:
            i = len(parte1) + 1
            soma += int(digito) * i
            i -= 1

        if (soma * 10) % 11 == cpf[9]:
            validar_1 = True

        #validacao da parte 2

        for digito in parte2:
            i = len(parte1) + 1
            soma += int(digito) * i
            i -= 1

        if (soma * 10) % 11 == cpf[10]:
            validar_2 = True

        if validar_1 and validar_2:
            return cpf
        else:
            return 0
#classe de Armazenamento e Validação da Data
class Data():
    def __init__(self, data):
        self.data = date.fromisoformat(self.armazenar_data(data))

    def armazenar_data(self, data_nascimento):
        data = (data_nascimento.split('/'))
        return f'{data[2]}-{data[1]}-{data[0]}'

    def __str__(self):
        return self.data.strftime('%d/%m/%y')

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
        return f'Rua: {self.rua} - n.o: {self.numero} - Compl.: {self.complemento} - CEP: {self.cep} '

# Classe Cliente:  cliente que é representado através de seu nome, endereço, data nascimento, cpf e tipo de cliente.
class Cliente():
    def __init__(self, nome, data_nascimento, cpf, endereco, tipo_cliente = 'Normal'):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self.endereco = endereco
        self.tipo_cliente = tipo_cliente

################
endereco = ('Rua Bangu', "121", "791121-210", 'casa' )
data_nascimento = Data('26/11/1983')

cliente1 = Cliente('Heitor Batistela Zunta', data_nascimento, '996828421-15', endereco)

print(cliente1.endereco)
print('------------------------')

print(cliente1._data_nascimento)


cpf = Cpf()

valor = cpf.validar_cpf('996.828.421-15')
print(valor)

