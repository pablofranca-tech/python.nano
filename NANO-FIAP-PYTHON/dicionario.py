

import getpass

print('Perfil do usuário')

login = input("Digite seu login: ")
senha = getpass.getpass("Digite sua senha: ")
print(f"\n✅ Login realizado com sucesso!\nBem-vindo, {login}!")

