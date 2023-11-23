# Controle de fluxo
import funcoes

# Recebimento de valores das informações dos usuários
idade = int(input("Digite sua idade: "))
brasileiro = input("Você é brasileiro? ").upper()
status = ""
 
# Condicional de impressão de idade
print("-"*40)
funcoes.verifacaoIdade(idade, status)
funcoes.nacionalidade(brasileiro)

