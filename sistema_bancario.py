menu = """____________Menu____________
Deposito [1]
Sacar    [2]
Extrato  [3]

Sair     [0]
            
=> """ 

saldo = 0 
limite = 500 
extrato = []
numeros_saques = 0 
limite_de_saque = 0
opcao = "" 
deposito = 0
saque = 0

while opcao != "0":
    print(menu,end="")
    opcao = input("")

    if opcao== "1":
        try:
            deposito = int(input("Digite o valor do deposito: "))
            if deposito > 0: # checando se o deposito é um numero inteiro positivo
                saldo = saldo + deposito 
                print(f"Operação realizada com sucesso!\nSaldo atual: {saldo}")
                extrato.append(f"R$ +{deposito}") # adicionando o deposito ao extrato
                deposito = 0
            else:
                print("So são permitidos valores positos")
        except :
            print("Valor invalido")
    
    elif opcao == "2":
        try:
            saque = int(input("Digite o valor do saque: "))
            
            if 0 > saque: # Só será permitidos números positivos no saque
                print("Só números positivos, por favor!")
            
            elif limite_de_saque >= 3: # Só seram permitidos 3 saques por dias
                print("Limite de Saque exedido")
                    
            elif saque > saldo: # Não seram permitidos valores maiores que o saldo
                print("Ops, Saldo insuficiente!")
            
            elif saque > 500: # Limite de quantida por saque
                print("Apenas valores menores que 500")
            
            elif saque <= 500: # Conferir valor do saque
                saldo = saldo - saque
                print(f"Operação realizada com sucesso!\nSaldo atual: {saldo}")
                extrato.append(f"R$ -{saque}") # adcionando o saque ao extrato
                saque = 0
                limite_de_saque +=1
            else:
                print("So são permitidos valores positos")
        except :
            print("Valor invalido")
    
    elif opcao == "3": 
        for valoresExtrato in extrato: # mostrando todo historio da conta no extrato 
            print(valoresExtrato)
        print(f"Saldo atual: {saldo}")
             
        
#Serão permitidos apenas 3 saques diarios, máximo por saque é 500 reais, não será permitido sacar uma quantia maior do que o saldo