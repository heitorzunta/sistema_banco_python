class Agencia():

    def __init__(self, endereco, numero):
        self.endereco = endereco
        self.numero = numero

    def __str__(self):
        return f'Agencia: {self.numero}'


