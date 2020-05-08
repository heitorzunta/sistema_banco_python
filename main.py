from modules.cliente import Cliente
from modules.data import Data
from modules.endereco import Endereco
from modules.cpf import Cpf


################ TESTE ###################################################
# Criar endereco
endereco = Endereco('Rua Bangu', "121", "791121-210", 'casa' )
print(endereco)

# Criar Data
data_nascimento = Data('26/11/1983')
print(data_nascimento)

# Verificar CPF
cpf = Cpf.validar_cpf('996.828.421.15')


# Criar cliente
nome = 'Heitor Batistela Zunta'.upper()
cliente1 = Cliente(nome, data_nascimento, cpf, endereco)

print(cliente1)

