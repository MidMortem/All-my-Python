A = 4500
P = 5000
T = 2500
CA = 0
CP = 0
CT = 0

while True:
    opcion = input(f"""Que quiere comprar? Tenemos :
      -Bolsa de Arena 100kg a ${A}
      -Bolsa de Piedras 100kg a ${P}
      -Tejas a ${T} c/u 
""").upper()
    if opcion == "ARENA":
        cantidad = int(input("Cuántas bolsas de arena quiere? "))
        CA += cantidad
    elif opcion == "PIEDRAS":
        cantidad = int(input("Cuántas bolsas de piedras quiere? "))
        CP += cantidad
    elif opcion == "TEJAS":
        cantidad = int(input("Cuántas tejas quiere? "))
        CT += cantidad
    else:
        print("Opción no válida, intenta de nuevo.")
        continue
    opcion2 = input("Desea comprar algo mas? (Si/No)").upper()
    if opcion2 != "SI":
        break
Total = (CA * A) + (CP * P) + (CT * T)
print(f"El total a pagar es: ${Total}")