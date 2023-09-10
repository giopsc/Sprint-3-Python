import json
import Validacoes


def cadastrar_bike():

    print("===== CADASTRO DA BICICLETA =====")
    bike = {}
    bike['nome'] = input("Escolha um nome de identificação da bike: ")
    bike['marca'] = input("Digite a marca da bike: ")
    bike['modelo'] = input("Digite o modelo da bike: ")
    bike['cor'] = input("Digite a cor da bike: ")
    bike['categoria'] = input("Informe a categoria da bike(mountain, road, urbana, etc): ")
    
    while True:
        bike['valor'] = input("Digite o valor da bike: ")
        if Validacoes.valida_valor(bike['valor']):
            break

    while True:
        bike['numero_serie'] = input("Digite o número de série: ")
        if Validacoes.valida_numero_serie(bike['numero_serie']):
            break

    modificacao = input("A bike sofreu alguma modificação? \n 1- Sim.\n 2- Não. \n")

    match modificacao:
        case "1":
            bike['modificacao'] = input("Quais modificações? ")
        case _:
            bike['modificacao'] = "Nenhuma"        

    acidentes = input("A bike já sofreu algum tipo de acidente? \n 1- Sim.\n 2- Não. \n")

    match acidentes:
        case "1":
            bike['acidentes'] = input("Quais acidentes? ")
        case _:
            bike['acidentes'] = "Nenhum"

    adicionar_bike(bike)


def carregar_bikes():
    try:    
        with open("./tabela_cadastro_bikes.json", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip(): 
                bikes = json.loads(conteudo)
            else:
                bikes = []
    except FileNotFoundError:
        bikes = []
    return bikes

def adicionar_bike(bike):
    bikes = carregar_bikes()
    nova_bike = bike
    bikes.append(bike)
    with open("./tabela_cadastro_bikes.json", 'w', encoding='utf-8') as arquivo:
        json.dump(bikes, arquivo, indent = 4)
    print("Bike adicionada com sucesso!")
