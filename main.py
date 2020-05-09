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
agencia1 = Agencia(endereco, '0001')

## Teste Contas
conta_corrente = ContaCorrente(agencia1, cliente1)
conta = Conta(agencia1, cliente2)
conta_facil = ContaFacil(cliente1)
conta_poupanca = Poupanca(agencia1, cliente1)

# Teste conta corrente
conta_corrente.deposita(1000)
#conta_corrente.tranferencia(conta_facil, 100)
#print(conta_corrente)
# Teste conta facil
#conta_facil.deposita(1000)
#conta_facil.tranferencia(conta_corrente, 100)
#conta_facil.tranferencia(conta_corrente, 500)
#conta_facil.sacar(10)
#print(conta_facil)

# Teste  Conta Poupanca
conta_poupanca.deposita(100)



############ metodo de saque para a classe main ######################

#def saque(conta, valor):
#    if isinstance(conta, Conta) and conta.sacar(valor):
#        print('saque efetuado com sucesso!')
#    else:
#        print('Ocorreu um erro em seu saque!')
# saque(conta_corrente, 100)




