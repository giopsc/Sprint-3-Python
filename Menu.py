import Cadastro
import Login
import re as regex

def menu():
    
    print("<------------- CycleSecure ------------->")
    print("1 - Realizar cadastro.")
    print("2 - Login.")
    print("3 - Realizar vistoria.")
    print("4 - Perguntas frequentes.")
    print("5 - Termos e condições.")
    print("6 - Contatos.")
    # print("7 - Conhecer planos de serviço.")
    # print("8 - Contratar plano de serviço.")
    # print("9 - Apólice.")
    escolha = input("Escolha uma opção para iniciar o processo: ")

    match escolha:
        case "1":
            Cadastro.cadastro()
        case "2":
            Login.login()
        case "3":
            print("Vistoria")
        case _:
            print("Opção inválida")
            menu()

menu()