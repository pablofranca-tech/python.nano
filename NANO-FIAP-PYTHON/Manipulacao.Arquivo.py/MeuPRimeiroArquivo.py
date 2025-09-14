
with open("primeiro_arquivo.txt", "r+") as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo:
        conteudo += linha
    print(conteudo)