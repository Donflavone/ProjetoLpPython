# Cadastro da senha
senha = input("Digite uma senha para o celular: ")

# Tentativas de acesso
tentativas = 3

for _ in range(tentativas):
    senha_inserida = input("Digite a senha para acessar o celular: ")
    
    if senha_inserida == senha:
        print("Bem-vindo!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você tem {tentativas} tentativas até o bloqueio.")
        
if tentativas == 0:
    print("O celular foi bloqueado.")
