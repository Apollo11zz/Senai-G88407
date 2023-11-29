usuarioLista = ["user1", "user2"]
senhaLista = ["1234", "12345"]

#menu = input("""
#Digite o numero referente a opção que deseja acessar
#
#----------------------------------------------
#|  [1] LOGIN      [2] REGISTRO     [3] SAIR  |
#----------------------------------------------
#""")


usuarioLogin = input("Digite seu usuário: ")
if usuarioLogin in usuarioLista:
    senhaLogin = input("Digite sua senha: ")
    if senhaLogin in senhaLista:
            print("Login efetuado com sucesso\n\nSeja bem vindo!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário inválido!")



