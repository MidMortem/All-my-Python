Notas = 0
Notas_Fallo = 0

for i in range(4):
    Nota = float(input("Ingrese la nota del alumno: "))
    Notas = Notas + Nota
    if Nota <= 4:
        Notas_Fallo = Notas_Fallo + 1
Promedio = Notas / 4
print("El promedio de las notas es: ", Promedio)
print("La cantidad de notas reprobadas es: ", Notas_Fallo)