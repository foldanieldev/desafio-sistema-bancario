clientes = []
contas = []
extrato = []
saldo = 0  
num_saque = 0
num_conta = 0

AGENCIA = "0001"

def menu():
    menu = """
        \n=============================\n
        [D]\t - Depósito
        [S]\t - Sacar
        [E]\t - Extrato
        [NU]\t - Novo cliente
        [NC]\t - Nova conta
        [Q]\t - Sair

        \n=============================\n
    """
    print(menu)

def operacao_deposito(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        if valor_deposito >= 10:
            saldo += valor_deposito
            extrato_deposito = f"Depósito de R${valor_deposito:10.2f}"
            extrato.append(extrato_deposito)
        else:
            print("Valor minímo de R$ 10.")
    else:
        print("Valor inexistente, digite um valor valído.")

    return saldo, extrato

def operacao_saque(*, saldo, valor_saque, extrato):
    LIMITE_DIARIO = 3
    SAQUE_MAX = 500
    global num_saque
    if valor_saque > saldo:
        print("Saldo insuficiente.")
    else:
        if valor_saque <= SAQUE_MAX:
            num_saque += 1
            if num_saque <= LIMITE_DIARIO:
                saldo -= valor_saque
                extrato_saque = f"Saque de R${valor_saque:10.2f}"
                extrato.append(extrato_saque)
                print(f"numero de saque {num_saque}")
            else:
                print(f"Número de {LIMITE_DIARIO} saque diário atingido")   
        else:
            print(f"Limite diário é de R${SAQUE_MAX:10.2f}.")
    
       
    return saldo, extrato

def operacao_extrato(saldo,/, *, extrato_operacao):
    for indice, dado_operacao in enumerate(extrato_operacao):
        print(f"{indice +1} {dado_operacao}")

    print(f"Seu saldo é {saldo:10.2f}")
    # print(f"Seu extrato é {extrato_operacao}")

def criar_cliente(clientes):
    num_cpf = input("Insira o cpf: ")
    
    cliente = verifica_cliente(num_cpf, clientes)

    if cliente:
        print("Cliente já cadastrado.")
        return
    
    nome_cliente = input("Digite o nome: ")
    data_nasciento = input("Digite a data de nascimento: ")
    endereco = input("Rua, n - bairro, cidade/UF: ")
    clientes.append({"nome": nome_cliente, "data_nascimento": data_nasciento, "cpf": num_cpf, "endereco": endereco })

def verifica_cliente(dado_cliente, clientes):
    for lista in clientes:
       if lista["cpf"] == dado_cliente:
           cliente = lista["cpf"]
           return cliente

def criar_contas(agencia, num_conta, clientes):
    num_cpf = input("Insira o cpf: ")

    cliente = verifica_cliente(num_cpf, clientes)

    if cliente:
        print("Conta criada!")
        return {"agencia": agencia, "numero_conta": num_conta, "cliente": cliente}
    else:
        print("Conta não existe")

while True:
     
    menu()

    opcao = input("Selecione a opção desejada: ")

    if opcao.upper() == "Q":
        print("Obrigador por ser nosso cliente.")
        break

    elif opcao.upper() == "D":
        valor_deposito = float(input("Informe o valor a depositar: "))
        saldo, extrato =operacao_deposito(saldo, valor_deposito, extrato)

    elif opcao.upper() == "S":
        valor_saque = float(input("Valor a sacar: "))
        saldo, extrato = operacao_saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato)

    elif opcao.upper() == "E":
       operacao_extrato(saldo, extrato_operacao=extrato)

    elif opcao.upper() == "NU":
        criar_cliente(clientes)

    elif opcao.upper() == "NC":
        conta = criar_contas(AGENCIA, num_conta, clientes)

        if conta:
            num_conta += 1
            contas.append(conta)

    else:
        print("Opção inexistente, verifique as opções.")

