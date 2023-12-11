# Por: VICTOR GABRIEL DE JESUS MOURA
# SENAI CAMAÇARI - CURSO TECNICO DE DESENVOLVIMENTO DE SISTEMAS
# DEZEMBRO DE 2023

import funcoes

# Recebimento de valores das informações dos usuários
idade = int(input("Digite sua idade: "))
brasileiro = input("Você é brasileiro? ").upper()
status = ""
# Condicional de impressão de idade
print("-"*40)
funcoes.verifacaoMaiorIdade(idade, status)
funcoes.nacionalidade(brasileiro)

