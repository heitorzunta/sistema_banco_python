from modules.cliente import Cliente
from modules.data import Data
from modules.endereco import Endereco
from modules.cpf import Cpf
from modules.agencia import Agencia
from modules.conta import Conta, ContaCorrente, ContaFacil, Poupanca

################ TESTE ###################################################
# Criar endereco
endereco = Endereco('Rua Bangu', "121", "791121-210", 'casa' )
#print(endereco)

# Criar Data
data_nascimento = Data('26/11/1983')
#print(data_nascimento)

# Verificar CPF
cpf = Cpf.validar_cpf('996.828.421.15')


# Criar cliente
nome1 = 'Heitor Batistela Zunta'.upper()
nome2 = 'Ana Lucia Souza'.upper()

cliente1 = Cliente(nome1, data_nascimento, cpf, endereco)
cliente2 = Cliente(nome2, data_nascimento, cpf, endereco, 'Especial')


## Teste Clientes

agencia1 = Agencia(endereco, '0001')
conta1 = ContaCorrente(agencia1, cliente1)
conta2 = Conta(agencia1, cliente2)
#print(conta1)
#print('novoooooo')
#print(conta2)

#conta1.deposita(100.0)
#print(conta1)
#conta1.desconto_taxa_anual()
#print(conta1)

print('TESTE CONTA FACIL')

conta_facil = ContaFacil(cliente1)
print(conta_facil.deposita(5000))
print(conta_facil.deposita(1))
print(conta_facil.taxa_anual_conta())
print(conta_facil)

print('TESTE CONTA POUPANCA')
conta_poupanca = Poupanca(agencia1, cliente1)
conta_poupanca.deposita(100)
conta_poupanca.taxa_anual_conta()
print(conta_poupanca)

