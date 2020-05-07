#classe CPF

def validar_digito(stringTeste, stringDigito):
    soma = 0
    i = len(stringTeste) + 1
    for digito in stringTeste:
        soma += int(digito) * i
        i -= 1
    if (soma * 10) % 11 == int(stringDigito):
        return True
    else:
        return False

def validar_cpf(cpf):
    validar_1 = False
    validar_2 = False

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
    validar_1 = validar_digito(parte1, cpf[9])

    #validacao da parte 2
    validar_2 = validar_digito(parte2, cpf[10])

    if validar_1 and validar_2:
        return cpf
    else:
        raise ValueError

