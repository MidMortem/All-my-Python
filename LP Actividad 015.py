Tiempos = 0
PC_Tiempos_0 = 0
PC_Tiempos_1 = 0
PC_Tiempos_2 = 0

for i in range(8):
    Tiempo = float(input("Ingrese el tiempo del corredor: "))
    Tiempos = Tiempos + Tiempo
    if Tiempo < 48:
        PC_Tiempos_0 = PC_Tiempos_0 + 1
    elif Tiempo >= 48 and Tiempo <= 105:
        PC_Tiempos_1 = PC_Tiempos_1 + 1
    else:
        PC_Tiempos_2 = PC_Tiempos_2 + 1
Promedio = Tiempos / 8
PC_Tiempos_00 = PC_Tiempos_0 * 100 / 8
PC_Tiempos_11 = PC_Tiempos_1 * 100 / 8
PC_Tiempos_22 = PC_Tiempos_2 * 100 / 8
print("El promedio de los tiempos es: ", Promedio)
print("Los porcentajes de los tiempos son:")
print("Menos de 48 segundos: ", PC_Tiempos_00, "%")
print("Entre 48 y 105 segundos: ", PC_Tiempos_11, "%")
print("Más de 105 segundos: ", PC_Tiempos_22, "%")
if Promedio < 101:
    print("NUEVO RECORD")