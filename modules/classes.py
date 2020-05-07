from datetime import date

# Classes referentes ao módulo bancário

#classe CPF

class Cpf():
    def __init__(self):
        pass

    @classmethod
    def validar_digito(self, stringTeste, stringDigito):
        soma = 0
        i = len(stringTeste) + 1
        for digito in stringTeste:
            soma += int(digito) * i
            i -= 1
        if (soma * 10) % 11 == int(stringDigito):
            return True
        else:
            return False
    @classmethod
    def validar_cpf(self, cpf):
        validar_1 = False
        validar_2 = False

        # remover . e - do cpf
        if not cpf.isdigit():
            cpf = cpf.replace('.', '', len(cpf))
            cpf = cpf.replace('-', '', len(cpf))

        # verifica quantidade de digito
        if len(cpf) != 11:
            raise ValueError

        parte1 = cpf[:9]
        parte2 = cpf[:10]

        # validacao da parte 1
        validar_1 = self.validar_digito(parte1, cpf[9])

        # validacao da parte 2
        validar_2 = self.validar_digito(parte2, cpf[10])

        if validar_1 and validar_2:
            return cpf
        else:
            raise ValueError



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
        self._cpf = Cpf.validar_cpf(cpf)
        self.endereco = endereco
        self.tipo_cliente = tipo_cliente

################ TESTE ###################################################
endereco = ('Rua Bangu', "121", "791121-210", 'casa' )
data_nascimento = Data('26/11/1983')

cliente1 = Cliente('Heitor Batistela Zunta', data_nascimento, '996828421-15', endereco)

print(cliente1.endereco)
print('------------------------')

print(cliente1._cpf)


