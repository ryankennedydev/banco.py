print("seja bem vindo ao Banco Safra!\n")

users = []
senhas = []
transacoes = []
saldo = 0
def inicio():
    while True:
        
        menu_principal = int(input("Escolha umas das opções:\n(1)criar conta\n(2)login\n(3)sair\n"))
        
        if menu_principal == 1:
            
            registro_user = input("Digite seu nome:")
            
            if registro_user in users:
                print("Usuário ja existente ")
                continue
            
            users.append(registro_user)
            
            registro_senha = int(input("Digite sua senha:"))
            senhas.append(registro_senha)
            saldo == saldo + 1
    
        if menu_principal == 2:
            
            login_user = input("Digite seu usuário:")
        
            if login_user in users:
                login_senha = int(input("Digite sua senha: "))
                
                if login_senha in senhas and login_user in users:
                    break
                else:
                    print("senha incorreta")
                    continue
    
inicio()

while True:
    menu_banco = int(input("Escolha uma das opções: \n(1)ver saldo \n(2)depositar\n(3)sacar\n(4)transferir\n(5)ver histórico\n(6)logout\n"))
    
    if menu_banco == 1:
        print(f"Seu saldo atual é de: {saldo}")
    
    if menu_banco == 2:
        
        depositar = int(input("Digite o valor a ser depositado:"))
        saldo = saldo + depositar
        transacoes.append(f"Deposito feito de R${depositar:.2f}")
    
    if menu_banco == 3:
        sacar = int(input("Digite o valor a ser sacado: "))
        if sacar <= saldo:
            saldo = saldo - sacar
            print("Saque realizado com sucesso!")
            transacoes.append(f"Saque realizado de R$sacar:.2f}}")
        else:
            print("Saldo insuficiente!")
    
    if menu_banco == 4:
        transferencia = int(input("Digite o valor a ser transferido:"))
        if transferencia <= saldo:
            print("Transferência realizada com sucesso!")
            saldo = saldo -  transferencia
            transacoes.append(f"transferência realizada de R${transferencia:.2f}")
        else:
            print("Saldo insuficiente!")
            
    if menu_banco == 5:
        print(transacoes)
    
    if menu_banco == 6:
        break
inicio()
