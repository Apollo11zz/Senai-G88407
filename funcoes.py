# Exercício 01
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

# Exercicio 02

def verifacaoIdade(idade):
    if idade < 13:
        print("Você é uma criança")
    elif idade < 19:
        print("Você é um adolescente")
    else:
        print("Você é um adulto")
