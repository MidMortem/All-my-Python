print ("""PRECIOS:
Soda $2500
Jugo $3200
""")
sumador = 0
contador_soda = 0
contador_jugo = 0
for i in range(8):
    bebida = input("Ingrese soda o jugo: ").lower()
    if bebida == "soda":
        sumador = sumador + 2500
        contador_soda = contador_soda + 1
    elif bebida == "jugo":
        sumador = sumador + 3200
        contador_jugo = contador_jugo + 1
    else:
        print("Bebida no válida")
print("TOTAL RECAUDADO: $", sumador)
print("Total de sodas vendidas:", contador_soda)
print("Total de jugos vendidos:", contador_jugo)