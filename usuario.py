from random import randint

from twilio.rest import Client

account_sid = "ACcd01ee91dfdbf830bdc81c44d03e7c1c"
auth_token = "ed86e86b99cdf95f44a61fca0e3f1f52"
client = Client(account_sid, auth_token)

linha = "====================================================================================================================================="

login = True

registro = True

while registro == True:
    email = input("coloque seu email: ")

    usuario = input("nome do usuario(min 5 max 10): ")

    senha = input("senha: ")

    cel = input("insira seu número de celular: ")

    if ".com" in email and 5 < len(usuario) < 10 and len(senha) == 4 and "+" in cel:
        registro = False

        print(linha)
        print()
        print("cadastro finalizado")
        print("faça o login")
        print(linha)
        print()

        while login == True:
            login_usuario = input("Seu usuario: ")

            login_senha = input("Sua senha: ")
            if login_usuario == usuario and login_senha == senha:

                print("você está logado!")
                login = False

            elif login_usuario == usuario and login_senha != senha:
                nova_senha = input("Ops, sua senha está incorreta, você deseja gerar uma nova senha: ")

                if nova_senha == "sim":
                    login_email = input("coloque seu email: ")

                    if login_email == email:

                        recuperação = randint(1000, 9999)
                        
                        message = client.messages.create(
                            to = cel,
                            from_ = '+15673472474',
                            body = f'Seu codigo de recuperação é {recuperação}'
                        )
                        codigo_recuperação = int(input("insira o codigo para definir nova senha: "))
                        if codigo_recuperação == recuperação:

                            codigo = input("defina uma nova senha: ")
                            senha = codigo
                else:
                    print("tente novamente")
            
            else:
                print("Usuário Incorreto! Favor tentar novamente")
    else:
        print("Credenciais erradas! Favor envia-las novamente")
        




    
        
                     
                                            
                                          
                                            


                        

                
            
                
                    
            

