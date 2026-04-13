LowerR = 0
MiddleR = 0
UpperR = 0
Maximo = -9999
Gasto = 0
while Gasto >= 0:
    Gasto = float(input("Ingrese el gasto de expensas: "))
    if Gasto < 150000:
        LowerR = LowerR + 1
    if Gasto >= 150000 and Gasto <= 450000:
        MiddleR = MiddleR + 1
    if Gasto > 450000:
        UpperR = UpperR + 1
    if Gasto > Maximo:
        Maximo = Gasto
print("Cantidad de departamentos con gasto menor a $150.000: ", LowerR)
print("Cantidad de departamentos con gasto entre $150.000 y $450.000: ", MiddleR)
print("Cantidad de departamentos con gasto mayor a $450.000: ", UpperR)
print("Gasto máximo registrado: $", Maximo)