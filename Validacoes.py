def valida_rg(rg):
    # Verificar se é int e len == 10
    return len(rg) == 9 and int(rg)

def valida_cpf(cpf):
    return len(cpf) == 11 and int(cpf)

def valida_cep(cep):
    return len(cep) == 8 and int(cep)

def valida_telefone(telefone):
    return len(telefone) == 11 and int(telefone)

def valida_senha(senha, confirma_senha):
    return senha == confirma_senha

def valida_valor(valor):
    return int(valor)

def valida_numero_serie(numero_serie):
    return int(numero_serie)