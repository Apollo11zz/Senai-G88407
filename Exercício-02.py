# Controle de fluxo
import funcoes

# Recebimento de valores das informações dos usuários
idade = int(input("Digite sua idade: "))
brasileiro = input("Você é brasileiro? ").upper()

# Passando o valor da variavel brasileiro para booleano
if brasileiro == "SIM":
    brasileiro = True
else:
    brasileiro = False

# Condicional de impressão de nacionalidade
if brasileiro:
    print("Você é brasileiro")
else:
    print("Você não é brasileiro")
    
# Condicional de impressão de idade
funcoes.verifacaoIdade(idade)

