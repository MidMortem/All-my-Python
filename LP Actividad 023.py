CPart = 0
GPart = 0
PPart = 0
EPart = 0
ptGPart = 0
PtPart = 0
PtEPart = 0

CPart = int(input("Ingrese la cantidad de Partidos que jugaron el año pasado: "))
while CPart <4 or CPart > 20:
    CPart = int(input("Ingrese la cantidad de Partidos que jugaron el año pasado: "))
for i in range (CPart):
    Resultado = input("Ingrese el resultado del partido (GANO, PERDIO o EMPATO): ").upper()
    while Resultado != "GANO" and Resultado != "PERDIO" and Resultado != "EMPATO":
        Resultado = input("Ingrese el resultado del partido (GANO, PERDIO o EMPATO): ").upper()
    if Resultado == "GANO":
        GPart = GPart + 1
        ptGPart = ptGPart + 3
    elif Resultado == "PERDIO":
        PPart = PPart + 1
    else:
        EPart = EPart + 1
        PtEPart = PtEPart + 1
print("Porcentaje de partidos ganados: ", (GPart / CPart) * 100, "%")
print("Porcentaje de partidos empatados: ", (EPart / CPart) * 100, "%")
print("Porcentaje de partidos perdidos: ", (PPart / CPart) * 100, "%")
print("Puntos obtenidos: ", ptGPart + PtPart + PtEPart)
