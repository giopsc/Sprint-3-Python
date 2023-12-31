def realizar_vistoria_bicicleta():
    print("===== Iniciaremos o processo da vistoria. =====\n")
    print("1- Tire uma foto da bicicleta inteira em um ângulo frontal e lateral: Isso ajudará a avaliar a condição geral da bicicleta, incluindo qualquer dano visível ou arranhões na pintura.")
    print("2- Tire uma foto do número de série (Chassis): O número de série é um identificador único que pode ajudar a verificar a propriedade da bicicleta e sua autenticidade.")
    print("3- Tire uma foto das rodas: Isso verifica a condição dos pneus, raios e aros.")
    print("4- Tire uma foto do guidão: Isso verifica a condição dos manetes, freios e outras peças importantes.")
    print("5- Tire uma foto da corrente: Isso ajuda a verificar a condição da corrente, engrenagens e pedais.")
    print("6- Tire uma foto do quadro: Isso verifica a condição geral do quadro e quaisquer sinais de dano.\n")
    while True:
        continuar = input("Escolha uma opção:\n 1- Reiniciar o programa.\n 2- Realizar a vistoria depois.\n 3- Finalizar o processo de vistoria.\n ")
        if continuar == "1":
            realizar_vistoria_bicicleta()
        elif continuar == "2":
            print("\nOk, volte quando você quiser realizar a vistoria.")
            break
        else:
            print("\nPrograma finalizado!")
            break