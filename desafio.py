import os

menu = """

    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair


Digite a op desejada: 

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            print(f"Depósito realizado com sucesso. Saldo atual: R$ {saldo:.2f}")
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print(f"Operação falhou, não foi possível depositar o valor de R$ {valor:.2f} na sua conta, verifique se esta correto")
    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou por falta de saldo em conta. Saldo atual: R$ {saldo:.2f}")
        elif excedeu_limite:
            print(f"Operação falhou pois o valor de R$ {valor:.2f} excede o limite de R$ 500,00. Saldo atual: R$ {saldo:.2f}")
        elif excedeu_saques:
            print(f"Operação falhou pois o número de saques que podem ser realizados no dia chegou ao limite de {LIMITE_SAQUES}")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            print(f"Saque realizado com sucesso. Saldo atual: R$ {saldo:.2f}. Quantidade de saques restantes no dia: {(LIMITE_SAQUES - numero_saques)}")
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
        else:
            print(f"Operação falhou pois o valor a ser sacado é inválido!")
    
    elif opcao == "e":
        print(" Extrato ".center(23,"#"))
        print("")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("")
        print("#"*23)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, tente novamente")