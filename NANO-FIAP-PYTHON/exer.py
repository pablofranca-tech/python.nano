#Exercicio 1

nome = 'Pablo França'
empresa = 'FIAP'
qtde_funcionarios = 500
mediaMensalidade = 856.50
print(nome, "trabalha na empresa" , empresa)
print("Possui: ", qtde_funcionarios, "fucionarios.")
print("A média da mensalidade é de: ", mediaMensalidade)

#exercico 2

nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

#
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
# PRIMEIRO PROBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa!="SIM" and  doenca_infectocontagiosa!="NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")



#Tabuada
tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))


#Calculadora

