# Por: VICTOR GABRIEL DE JESUS MOURA
# SENAI CAMAÇARI - CURSO TECNICO DE DESENVOLVIMENTO DE SISTEMAS
# DEZEMBRO DE 2023

import funcoes
usuarioLista = {
"user1": "12345",
"user2": "54321",
}

status = False
while status == False:
    menu = input("""
    Digite o numero referente a opção que deseja acessar

    ----------------------------------------------
    |  [1] LOGIN      [2] REGISTRO     [3] SAIR  |
    ----------------------------------------------
    """)
    if menu == "1":
        status = funcoes.validacaoLogin(usuarioLista)
    elif menu == "2":
        status = funcoes.registroLogin(usuarioLista)
    elif menu == "3":
        print("Obrigado por utilizar o sistema!")
        status = True
    else:
        print("Comando não reconhecido")