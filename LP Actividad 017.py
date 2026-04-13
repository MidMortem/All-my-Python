Suma = 0
for dia in range(1, 32):
    TPUH = float(input(f"Ingrese la temperatura de Ushuaia el {dia} de Julio del 2025: "))
    while TPUH >= 6 or TPUH <= -6:
        TPUH = float(input(f"Ingrese la temperatura de Ushuaia el {dia} de Julio del 2025: "))
    Suma += TPUH

print(f"El promedio de temperatura de Ushuaia en Julio del 2025 fue: {Suma / 31}°C")