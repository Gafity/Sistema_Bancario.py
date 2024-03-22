# novo usúario nome, data de nascimento, cpf(somente numeros) e endereço(logradouro, nro, bairro, cidada/sigla)

clientes = {}
cpf_cadastrados = []
def cadastrar():
    global clientes 
    cpf = input("Digite seu cpf: ")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")
    saldo_conta = 0
    
    if cpf in cpf_cadastrados:
        print("Cpf já possui cadastrado")
        cadastrar()
    
    clientes[cpf]={"nome":nome, "dataNascimento":data_nascimento, "endereço":endereco, "saldo":saldo_conta}
    cpf_cadastrados.append(cpf)
    return clientes

def logar(cpf_login, data_nascimento):
    global clientes
    if cpf_login in clientes and data_nascimento == clientes.get(cpf_login).get("dataNascimento"):
        print("logado com sucesso")
    else:
        testeM = clientes.get(cpf_login,"cpf não encontrado").get("dataNascimento","dataNascimento não encontrado")
        print("login não encontrado")
        print(clientes)
        print(f"Mostrando teste: {testeM}")



def deposito_bancario(valor,saldo):
    print("")



menu = """____________Menu____________
Cadastrar   [1]
Login       [2]
Deposito    [3]
Sacar       [4]
Extrato     [5]

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
    if opcao == "1":
       clientes = cadastrar()
       print(clientes)
    
    elif opcao == "2":
        cpf = input("Digite seu cpf: ")
        data_de_nascimento = input("Digite sua data de nascimento: ")
        logar(cpf,data_de_nascimento)

    elif opcao== "3":
        try:
            deposito = int(input("Digite o valor do deposito: "))
            if deposito > 0: # checando se o deposito é um numero inteiro positivo
               deposito_bancario(deposito,)
            else:
                print("So são permitidos valores positos")
        except :
            print("Valor invalido")
    
    elif opcao == "3":
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
    
    elif opcao == "4": 
        for valoresExtrato in extrato: # mostrando todo historio da conta no extrato 
            print(valoresExtrato)
        print(f"Saldo atual: {saldo}")
             
        
#Serão permitidos apenas 3 saques diarios, máximo por saque é 500 reais, não será permitido sacar uma quantia maior do que o saldo