import json
import Cadastro

usuarios = Cadastro.carregar_usuarios()

def login():
    cpf = input("CPF: ")
    senha = input("Senha: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            return True
        else:
            print("CPF ou senha incorretos!")
            return False