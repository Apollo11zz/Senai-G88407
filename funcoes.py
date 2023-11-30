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

def verifacaoIdade(idade, maiorIdade):
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