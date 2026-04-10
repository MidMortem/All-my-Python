S_Edades = 0
C_Edades_0 = 0
C_Edades_1 = 0

for i in range(30):
    Edades = int(input("Ingrese su edad:"))
    S_Edades = Edades + S_Edades
    if Edades < 18:
        C_Edades_0 = C_Edades_0 + 1
    else:
        C_Edades_1 = C_Edades_1 + 1

Promedio = S_Edades / 30
Por_0 = (C_Edades_0 * 100) / 30
Por_1 = (C_Edades_1 * 100) / 30
print("El promedio de las edades es: ", Promedio)
print("El porcentaje de personas menores de edad es: ", Por_0, "%")
print("El porcentaje de personas mayores de edad es: ", Por_1, "%")