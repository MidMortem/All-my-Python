Bicicleta = 0
Moto = 0
Auto = 0
for i in range(7):
    Vehiculo = input("Ingrese el tipo de vehículo (Bicicleta, Moto, Auto): ").lower()
    if Vehiculo == "bicicleta":
        Bicicleta += 1
    elif Vehiculo == "moto":
        Moto += 1
    elif Vehiculo == "auto":
        Auto += 1
    else:
        print("Vehículo no válido")
print("Cantidad de bicicletas:", Bicicleta)
print("Cantidad de motos:", Moto)
print("Cantidad de autos:", Auto)