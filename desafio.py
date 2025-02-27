
saldo = 0
extrato_deposito = []
extrato_saque = []
numero_deposito = 1
numero_saque = 1
LIMITE_DIARIO = 3

# Funõa para realizar depósito
def fazer_deposito(valor):
    global saldo
    global extrato_deposito
    global numero_deposito

    print("########## Seu Depósito ##########\n")

    if valor > 0:
        if valor < 10:
            print(f"Valor de R${valor:10.2f} insuficente, depósito minímo de 10,00 reais.")
        else:
            saldo += valor
            extrato = f"Depósito de número {numero_deposito}: R${valor:10.2f}"
            extrato_deposito.append(extrato)
            numero_deposito = numero_deposito + 1
            print(f"Depósito de R${valor:10.2f} efetuado com sucesso!")
    else:
        print("Valor inválido. ")
    

# Função para realizar o saque 
def realiza_saque(valor):
    global saldo
    global extrato_saque
    global numero_saque 
    limite = 500
    extrato = ""
    LIMITE_DIARIO

    print("########## Seu Saque ##########\n")

    if numero_saque <= LIMITE_DIARIO:
        print(f"Número de saques {numero_saque}")
        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            if valor <= limite:
                saldo -= valor
                extrato = f"Saque de número {numero_saque}: R${valor:10.2f}"
                numero_saque += 1
                extrato_saque.append(extrato)
            else:
                print(f"Não é possível realizar o saque devido ao limite diário R${limite:10.2f}")
    else:
        print("Você atingiu o número de saque diario!")


# Função para realizar apresentação do extrato.
def mostrar_extrato(mostra_deposito, mostra_saque):
    mostra_deposito_na_tela = mostra_deposito
    mostra_saque_na_tela = mostra_saque

    print("########## Seu Extrato ##########\n")

    for lista in mostra_deposito_na_tela:
        print(lista)

    for lista in mostra_saque_na_tela:
        print(lista)

    print(f"Saldo atual: R${saldo:10.2f}")
    

menu = '''
Banco do Estudante\n
    [1] Depositar
    [2] Saque
    [3] Extrato
    [0] Sair
'''

while True:
    print(menu)

    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        print("########## Seu Depósito ##########\n")
        valor_a_depositar = float(input("Valor a depositar: "))
        fazer_deposito(valor_a_depositar)
    elif opcao == 2:
        print("########## Seu Saque ##########\n")
        valor_sacar = float(input("Valor a ser sacado: "))
        realiza_saque(valor_sacar)
    elif opcao == 3:
        print("########## Seu Extrato ##########\n")
        mostrar_extrato(extrato_deposito, extrato_saque)
    elif opcao == 0:
        print("Obrigado por usar o nosso sistema bancário!")
        break
    else:
        print("Informe uma opção válida, tente novamente!")

