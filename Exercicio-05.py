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

# ----------------------------------------------------------------------------
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
        status = validacaoLogin(usuarioLista)
    elif menu == "2":
        status = registroLogin(usuarioLista)
    elif menu == "3":
        print("Obrigado por utilizar o sistema!")
        status = True
    else:
        print("Comando não reconhecido")