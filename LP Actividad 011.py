#"""porcentaje"""
#total = 2.5
#sumador = 0
#for i in range(3):
#    tomo = float(input("ingrese cuanto bebió: "))
#    sumador = sumador + tomo
#porcentaje_bebio = sumador*100 / total
#print("se bebió:", porcentaje_bebio, "%")

contador = 0
for i in range(4):
    altura = float(input("ingrese cuanto mide: "))
    if altura > 1.65:
        contador = contador + 1
porcentaje = contador*100 / 4
print("El porcentaje de personas que miden más de 1.65 es de:", porcentaje)