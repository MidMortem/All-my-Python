Notas = 0
Aprobados = 0
Desaprobados = 0

for i in range(20):
    while True:
        Nota = int(input("Ingrese la nota del alumno: "))
        if 0 <= Nota <= 10:
            break
        else:
            print("Nota no válida, ingrese una nota entre 0 y 10")
    
    Notas += Nota
    if Nota >= 4:
        Aprobados += 1
    else:
        Desaprobados += 1

Promedio = Notas / 20
print(f"Promedio de notas: {Promedio}")
print(f"Porcentaje de Aprobados: {Aprobados / 20 * 100:.2f}%")
print(f"Porcentaje de Desaprobados: {Desaprobados / 20 * 100:.2f}%")