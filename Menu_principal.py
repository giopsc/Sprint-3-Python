import CadastroBike
import Cadastro
import Login
import Vistoria

def menu_principal():
    print("<------------- CycleSecure ------------->")
    print("1 - Realizar cadastro.")
    print("2 - Login.")
    print("3 - Realizar vistoria.")
    print("4 - Cadastrar bike.")
    print("5 - Contatos.")
    # print("6 - Conhecer planos de serviço.")
    # print("7 - Contratar plano de serviço.")
    # print("8 - Apólice.")
    escolha = input("Escolha uma opção para iniciar o processo: ")

    match escolha:
        case "1":
            Cadastro.cadastro()
        case "2":
            Login.login()
        case "3":
            Vistoria.realizar_vistoria_bicicleta()
        case "4":
            CadastroBike.cadastrar_bike()
        case "5":
            print("===== CENTRAL DE ATENDIMENTO ===== \n\nTel Fixo São Paulo ou Capital -> (11)4122-5599\nDemais Localidades -> 3355-6988\nWhatsApp -> (11) 3355-9999\nSAC - Sugestões e Reclamações -> 0800-526.356.77\nEm caso de Roubo e Furto disque Emergência -> 0800-526.888.88\n\n")
        case _:
            print("Opção inválida")
            menu_principal()

menu_principal()