contas = {"12345": 99.00}

def autenticar(lista):
    senha = input("Digite sua senha: ")
    if senha in lista:
        print("A senha foi encontrada!\nConta Autenticada.")
        return senha
    else:   
        print("A senha não foi encontrada!")
        return False

def verficarSaldo(lista, conta):
    saldo = lista[conta]
    print("O saldo da sua conta é: R${}".format(saldo)) #É o mesmo que o 'f' antes da string

def depositar(lista, conta):
    saldo = lista[conta]
    deposito = float(input("Digite quantos R$ deseja retirar: R$"))
    saldo += deposito
    lista[conta] = saldo

def retirar(lista, conta):
    saldo = lista[conta]
    retirada = float(input("Digite quantos R$ deseja depositar: R$"))
    saldo -= retirada
    lista[conta] = saldo

def operacoesBancarias(lista, usuario):
    run = True
    while run:
            sistema = input(""" 
        |---------------------------------------------------|
        |            CAIXA ELETRÔNICO SENAI                 |
        |                MENU PRINCIPAL                     |
        |---------------------------------------------------|
        |   [1] VERIFICAR SALDO     [2] DEPOSITAR DINHEIRO  |     
        |---------------------------------------------------|
        |   [3] RETIRAR DINHEIRO    [4] SAIR                |
        |---------------------------------------------------|
        """)
            if sistema == "1":
                verficarSaldo(lista, usuario)
            elif sistema == "2":
                depositar(lista, usuario)
            elif sistema == "3":
                retirar(lista, usuario)
            elif sistema == "4":
                break
            else:
                print("Comando invalido! Tente novamente")

print("\n\nBem vindo ao Banco Senai!\nPor favor insira sua senha para acessar sua conta bancária")
usuario = autenticar(contas)
if usuario != False:
    operacoesBancarias(contas, usuario)
else:
    print("Sistema encerrando...")