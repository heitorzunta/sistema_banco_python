
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