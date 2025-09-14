

usuarios = {}

opcao = input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar os usuários\n" +
              "<S> - Para Sair: ").upper()

while opcao in ["I", "P", "E", "L"]:
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a última data de acesso: ")
        estacao = input("Qual a última estação acessada: ").upper()
        usuarios[chave] = [nome, data, estacao]

    elif opcao == "P":
        chave = input("Digite o login para pesquisar: ").upper()
        if chave in usuarios:
            print(f"Nome: {usuarios[chave][0]}")
            print(f"Último acesso: {usuarios[chave][1]}")
            print(f"Estação: {usuarios[chave][2]}")
        else:
            print("Usuário não encontrado.")

    elif opcao == "E":
        chave = input("Digite o login para excluir: ").upper()
        if chave in usuarios:
            del usuarios[chave]
            print("Usuário excluído com sucesso.")
        else:
            print("Usuário não encontrado.")

    elif opcao == "L":
        for chave, dados in usuarios.items():
            print(f"Login: {chave}")
            print(f"Nome: {dados[0]}")
            print(f"Último acesso: {dados[1]}")
            print(f"Estação: {dados[2]}")
            print("-" * 20)

    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar os usuários\n" +
                  "<S> - Para Sair: ").upper()
