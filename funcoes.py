# Exercício 01 ------------------------------------------------------------
def opMatematicos(a, b):
    print("-"*30)
    print("OPERADORES MATEMÁTICOS")
    print("-"*30)
    print("Soma: ", a+b)
    print("Diferença:", a-b)
    print("Produto:", a*b)
    print("Divisão: ", a/b)
    print("\n")


def opComparacao(a, b):
    print("-"*30)
    print("OPERADORES DE COMPARAÇÃO")
    print("-"*30)
    print("Igual: ", a == b)
    print("Diferente: ", a != b)
    print("A é maior que B: ", a > b)
    print("A é menor que B: ", a < b)                                                  
    print("\n")


def opLogico():
    e = True and False
    ou = True or False
    nao = not True
    print("-"*30)
    print("OPERADORES LÓGICOS")
    print("-"*30)
    print("""
E = TRUE AND FALSE
OU = TRUE OR FALSE
NÃO = NOT TRUE
""")

# Exercicio 02 ------------------------------------------------------------

def verifacaoMaiorIdade(idade, maiorIdade):
    if idade < 13:
        print("Você é uma criança")
        maiorIdade = False
    elif idade < 19:
        print("Você é um adolescente")
        maiorIdade = True
    else:
        print("Você é um adulto")
        maiorIdade = True

    if maiorIdade:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")


def nacionalidade(nacio):
    # Passando o valor da variavel brasileiro para booleano
    if nacio == "SIM":
        nacio = True
    else:
        nacio = False

    # Condicional de impressão de nacionalidade
    if nacio:
        print("Você é brasileiro")
    else:
        print("Você não é brasileiro")
    
# Exercicio 03 ------------------------------------------------------------
def verificacaoFaixaEtaria(idade):
    if idade <= 13:
        print("Você é uma criança")
    elif idade <= 18:
        print("Você é um adolescente")
    elif idade <= 60:
        print("Você é um adulto")
    else:
        print("Você é um idoso")
# Exercicio 04 ------------------------------------------------------------
def calcularCustoViagem(distancia, tipoVeiculo):
    if tipoVeiculo == "CARRO":
        custoPorKm = 0.5
    elif tipoVeiculo == "MOTO":
        custoPorKm = 0.2
    elif tipoVeiculo == "BICICLETA":
        custoPorKm = 0.1
    else:
        return None
    
    custoTotal = distancia * custoPorKm
    return custoTotal

# Exercicio 05 ------------------------------------------------------------
def validacaoLogin(lista):
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in lista and lista[usuario] == senha:
        print("Login bem-sucedido!")
        return True
    else:   
        print("Usuário ou senha INCORRETA!!")
        return False

def registroLogin(lista):
    usuario = input("Digite o usuário que deseja registrar: ")
    senha = input("Digite a senha que deseja cadastrar: ")
    lista[usuario] = senha
    return False

# Exercicio 06 ------------------------------------------------------------
# Para exibir o menu sem o while
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

# Para ser utilizado no menu do programa
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

# Adiciona o produto a lista
def adicionarItem(lista):
    menu()
    while True:
        produto = input("Digite o número do produto que deseja adicionar (ou 's' para sair): ")
        if produto.lower() == 's':
            break
        elif produto.isdigit() and int(produto) in range(1, 11):
            # Se o produto for um inteiro e estiver dentro dos numeros da lista
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

# Remove os itens que já estão na lista
def removerItem(lista):
    while True:
        if lista:
            print("Produtos no pedido:")
            for i, produto in enumerate(lista, start=1): # Numera em ordem os pedidos da lista 
                print("{}. {}".format(i, produto))

            escolha = input("Digite o número do produto que deseja remover (ou 's' para voltar ao menu): ")
            if escolha.lower() == 's':
                break
            elif escolha.isdigit() and int(escolha) in range(1, len(lista) + 1): 
                # Se o produto for um inteiro e estiver dentro dos numeros da lista
                itemRemovido = list(lista.keys())[int(escolha) - 1]
                del lista[itemRemovido]
                print("{} removido do pedido.".format(itemRemovido))
            else:
                print("Opção inválida ou fora de alcance.")
        else:
            print("Não há produtos no pedido para remover.")
            break

# Exibe formatada a lista
def exibirPedido(lista):
    while True:
        if lista:
            print(""" 
|-------------------------------|-----------|
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

# Calcula o preço total dos produtos que estão na lista
def calcularTotal(lista):
    while True:
        if lista:
            total = sum(lista.values()) # Soma os preços da lista
            print("O total do pedido é: R${:.2f}".format(total))
            escolha = input("Pressione 's' para voltar ao menu: ")
            if escolha.lower() == 's':
                break
            else:
                print("Opção inválida.")
        else:
            print("Não há produtos no pedido.")
            break