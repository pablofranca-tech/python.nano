inventario = []
resposta = "S"

while resposta == "S":
    equipamento = input("Equipamento: ")
    valor = float(input("Valor: "))
    numero_serial = int(input("Número Serial: "))
    departamento = input("Departamento: ")

    inventario.append({
        "Equipamento": equipamento,
        "Valor": valor,
        "Número Serial": numero_serial,
        "Departamento": departamento
    })

    resposta = input("Digite 'S' para continuar: ").upper()

for item in inventario:
    print(f"Equipamento: {item['Equipamento']}")
