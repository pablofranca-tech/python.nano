inventario = []
resposta = 'S'

while resposta == 'S':
    equipamento = input('Equipamento: ')
    valor = float(input('Valor: '))
    numero_serial = int(input('Número Serial: '))
    departamento = input('Departamento: ')
    
    inventario.append([equipamento, valor, numero_serial, departamento])
    
    resposta = input("Digite 'S' para continuar: ").upper()


for elemento in inventario:
    print(elemento)
                    


                    