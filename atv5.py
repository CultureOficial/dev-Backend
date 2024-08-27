while True:
    user = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if user == senha:
        print("A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Login bem-sucedido!")
        break  
