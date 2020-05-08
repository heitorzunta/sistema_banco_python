# Classe Cliente:  cliente que é representado através de seu nome, endereço, data nascimento, cpf e tipo de cliente.

class Cliente():
    def __init__(self, nome, data_nascimento, cpf, endereco, tipo_cliente = 'Normal'):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self.endereco = endereco
        self.tipo_cliente = tipo_cliente

    def __str__(self):
         saida = 'Cliente: ' + self._nome + '\n' + 'CPF: ' + self._cpf + '\n' + 'Tipo: ' + self.tipo_cliente
         return saida






