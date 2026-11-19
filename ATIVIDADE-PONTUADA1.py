import os

saldo_disponivel = 0
extrato = []

def logo_banco():
    print("=== BANCO DO CONFRINHO DO CAIXA ===")

def saldo():
    print(f"Saldo disponível: R$ {saldo_disponivel}")

def ver_extrato():
    if not extrato:
        print("NENHUMA MOVIMENTAÇÃO REALIZADA!")
    else:
        for item in extrato:
            print(item)

def deposito(saldo_disponivel):
    valor = float(input("Digite o valor do depósito: "))
    if valor <= 0:
        print("Depósito inválido.")
    else:
        saldo_disponivel += valor
        extrato.append(f"Depósito: + R$ {valor}")
        print("Depósito realizado com sucesso!")
    return saldo_disponivel

def saque(saldo_disponivel):
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("Valor de saque inválido.")
    elif valor > saldo_disponivel:
        print("Saldo indisponível para realizar o saque.")
    else:
        saldo_disponivel -= valor
        extrato.append(f"Saque: - R$ {valor}")
        print("Saque aprovado!")
        return saldo_disponivel

while True:
    logo_banco()

    print("""
    1 - Ver Saldo.
    2 - Depositar.
    3 - Sacar.
    4 - Ver extrato.
    0 - Sair.
    """)

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            logo_banco()
            print("=== SALDO ===")
            saldo()

        case "2":
            logo_banco()
            print("=== DEPOSITAR ===")
            saldo_disponivel = deposito(saldo_disponivel)
        case "3":
            logo_banco()
            print("=== SACAR ===")
            saldo_disponivel = saque(saldo_disponivel)
        case "4":
            logo_banco()
            print("=== EXTRATO ===")
            ver_extrato()
        case "0":
            logo_banco()
            print("Obrigado por utilizar nosso banco!")
            break
        case _:
            print("Opção inválida!")

    input("\nPressione ENTER para continuar...")
    os.system("cls")