import os

def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
        print(""" 
|-------------------------------------------|
|                   MENU                    |
|-------------------------------------------|
|     NOME            |   PREÇO (R$)        |
|-------------------------------------------|
|   1. PASTA          |      20.00          |
|   2. SUSHI          |      30.00          |
|   3. BURGUER        |      18.00          |
|   4. SALADA         |      15.00          |
|   5. PIZZA          |      25.00          |
|   6. TACO           |      12.00          |
|   7. SOPA           |      10.00          |
|   8. WRAP           |      22.00          |
|   9. SOBÁ           |      28.00          |
|  10. CHURRASCO      |      35.00          |
|-------------------------------------------|
        """)

def exibirMenu():
    while True:
        print(""" 
|-------------------------------------------|
|                   MENU                    |
|-------------------------------------------|
|     NOME            |   PREÇO (R$)        |
|-------------------------------------------|
|   1. PASTA          |      20.00          |
|   2. SUSHI          |      30.00          |
|   3. BURGUER        |      18.00          |
|   4. SALADA         |      15.00          |
|   5. PIZZA          |      25.00          |
|   6. TACO           |      12.00          |
|   7. SOPA           |      10.00          |
|   8. WRAP           |      22.00          |
|   9. SOBÁ           |      28.00          |
|  10. CHURRASCO      |      35.00          |
|-------------------------------------------|
        """)
        voltarMenu = input("Pressione 's' para voltar ao menu principal: ")
        if voltarMenu.lower() == 's':
            break


def adicionarItem(lista):
    menu()
    while True:
        produto = input("Digite o número do produto que deseja adicionar (ou 's' para sair): ")
        if produto.lower() == 's':
            break
        elif produto.isdigit() and int(produto) in range(1, 11):
            produto = int(produto)
            nomeProduto = {
                1: "PASTA", 2: "SUSHI", 3: "BURGUER", 4: "SALADA", 5: "PIZZA",
                6: "TACO", 7: "SOPA", 8: "WRAP", 9: "SOBÁ", 10: "CHURRASCO"
            }[produto]
            precoProduto = {
                1: 20.00, 2: 30.00, 3: 18.00, 4: 15.00, 5: 25.00,
                6: 12.00, 7: 10.00, 8: 22.00, 9: 28.00, 10: 35.00
            }[produto]
            lista[nomeProduto] = precoProduto
            print("{} adicionado com sucesso por R${:.2f}.".format(nomeProduto, precoProduto))
        else:
            print("Opção inválida.")

def removerItem(lista):
    while True:
        if lista:
            print("Produtos no pedido:")
            for i, produto in enumerate(lista, start=1):
                print("{}. {}".format(i, produto))

            escolha = input("Digite o número do produto que deseja remover (ou 's' para voltar ao menu): ")
            if escolha.lower() == 's':
                break
            elif escolha.isdigit() and int(escolha) in range(1, len(lista) + 1):
                itemRemovido = list(lista.keys())[int(escolha) - 1]
                del lista[itemRemovido]
                print("{} removido do pedido.".format(itemRemovido))
            else:
                print("Opção inválida ou fora de alcance.")
        else:
            print("Não há produtos no pedido para remover.")
            break

def exibirPedido(lista):
    while True:
        if lista:
            print(""" 
|-------------------------------------------|
|           NOME                |   PREÇO   |
|-------------------------------|-----------|""")
            for produto, preco in lista.items():
                print("|           {}               |   R${:.2f} |".format(produto, preco))

            escolha = input("Pressione 's' para voltar ao menu: ")
            if escolha.lower() == 's':
                break
            else:
                print("Opção inválida.")
        else:
            print("Não há produtos no pedido.")
            break


def calcularTotal(lista):
    while True:
        if lista:
            total = sum(lista.values())
            print("O total do pedido é: R${:.2f}".format(total))
            escolha = input("Pressione 's' para voltar ao menu: ")
            if escolha.lower() == 's':
                break
            else:
                print("Opção inválida.")
        else:
            print("Não há produtos no pedido.")
            break

listaProdutos = {}
run = True
while run:
    limparTerminal()
    sistema = input(""" 
|-------------------------------------------------------------------|
|           BEM VINDO AO SISTEMA DE REALIZAÇÃO DE PEDIDO            |
|         DIGITE O NÚMERO REFERENTE AO QUE DESEJA UTILIZAR          |
|-------------------------------------------------------------------|
|   [1] EXIBIR MENU     [2] ADICIONAR ITEM      [3] REMOVER ITEM    |     
|-------------------------------------------------------------------|
|   [4] EXIBIR PEDIDO   [5] CALCULAR TOTAL      [6] SAIR DO SISTEMA |
|-------------------------------------------------------------------|
""")
    if sistema == "1":
        exibirMenu()
    elif sistema == "2":
        adicionarItem(listaProdutos)
    elif sistema == "3":
        removerItem(listaProdutos)
    elif sistema == "4":
        exibirPedido(listaProdutos)
    elif sistema == "5":
        calcularTotal(listaProdutos)
    elif sistema == "6":
        break
    else:
        print("Código não identificado! Tente novamente.")
