"""Promedio"""
sumador = 0
for i in range(3):
    nota = int(input("ingrese su nota: "))
    sumador = sumador + nota
promedio = sumador / 3
print("El promedio es de:", promedio)