# by Victor Gabriel Moura, from SENAI Camaçari

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))
# estudante = input("Você é estudante? ").upper()

# if estudante == "SIM":
#    estudanteStatus = True
# elif estudante == "NAO":
#    estudanteStatus = False
# else:
#   estudanteStatus = False

# print("""
# Nome: {}
# Idade: {}
# Altura: {}
# Estudante: {}
# """.format(nome, idade, altura, estudante))

# print(type(nome))
# print(type(idade))
# print(type(altura))
# print(type(estudanteStatus))

# OPERADORADORES MATEMÁTICOS

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


opMatematicos(5, 3)
opComparacao(5, 3)
opLogico()
