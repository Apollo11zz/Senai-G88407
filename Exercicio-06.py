# Por: VICTOR GABRIEL DE JESUS MOURA
# SENAI CAMAÇARI - CURSO TECNICO DE DESENVOLVIMENTO DE SISTEMAS
# DEZEMBRO DE 2023

import os, funcoes

# Para limpar a tela do terminal, deixar bonito
def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
        funcoes.exibirMenu()
    elif sistema == "2":
        funcoes.adicionarItem(listaProdutos)
    elif sistema == "3":
        funcoes.removerItem(listaProdutos)
    elif sistema == "4":
        funcoes.exibirPedido(listaProdutos)
    elif sistema == "5":
        funcoes.calcularTotal(listaProdutos)
    elif sistema == "6":
        break
    else:
        print("Código não identificado! Tente novamente.")
