def formatar_valor(valor):
    return f"R$ {valor:.2f}"

saldo = 0
depositos = []
saques = []
limite_saques = 3
limite_por_saque = 500

while True:
    print("\nEscolha uma operação:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            depositos.append(valor)
            print("Depósito realizado com sucesso!")
        
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        
        if limite_saques == 0:
            print("Limite de saques diários atingido.")
        
        else:
            valor = float(input("Valor do saque: "))
            if valor > 0 and valor <= limite_por_saque and valor <= saldo:
                saldo -= valor
                saques.append(valor)
                limite_saques -= 1
                print("Saque realizado com sucesso!")
            
            elif valor > saldo:
                print("Saldo insuficiente.")
            
            else:
                print("Valor inválido para saque ou limite excedido.")

    elif opcao == "3":
        print("\nExtrato:")
        
        if not depositos and not saques:
            print("Não foram realizadas movimentações.")
        
        else:
            
            for deposito in depositos:
                print(f"Depósito: {formatar_valor(deposito)}")
            
            for saque in saques:
                print(f"Saque: {formatar_valor(saque)}")
            print(f"Saldo: {formatar_valor(saldo)}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")