import Validacoes as valida
import json

def cadastro():
    
    # Cadastro das informações do Usuário
    print("===== CADASTRO DO USUÁRIO ===== ")

    nome = input("Digite seu nome: ")

    while True:
        rg = input("Digite seu RG (Somente números): ")
        if valida.valida_rg(rg):
            break

    while True:
        cpf = input("Digite seu CPF (Somente números): ")
        if valida.valida_cpf(cpf):
            break

    while True:
        cep = input("Digite seu CEP (Somente números): ")
        if valida.valida_cep(cep):
            break

    while True:
        telefone = input("Digite seu telefone (Com DDD e sem espaços): ")
        if valida.valida_cep(cep):
            break

    endereco = input("Digite seu endereço: ")
    email = input("Digite seu e-mail: ")

    while True:
        senha = input("Digite sua senha: ")
        confirma_senha = input("Confirme a sua senha: ")
        if valida.valida_senha(senha, confirma_senha):
            break
        print("As senhas não coincidem ")

    usuario = {'cpf': cpf, 'nome': nome, 'rg': rg, 'cep': cep, 'endereco': endereco, 'telefone': telefone, 'email': email, 'senha': senha}

    adicionar_usuario(usuario)

    print("Senha confirmada!\nCadastro do usuário finalizado!")
    
def carregar_usuarios():
    try:    
        with open("./tabela_cadastro.json", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip(): 
                usuarios = json.loads(conteudo)
            else:
                usuarios = []
    except FileNotFoundError:
        usuarios = []
    return usuarios

def adicionar_usuario(usuario):
    usuarios = carregar_usuarios()
    novo_usuario = usuario
    usuarios.append(novo_usuario)
    with open("./tabela_cadastro.json", 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent = 4)


# cadastro()