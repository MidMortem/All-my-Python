Edades = 0
bt13a55 = 0
me13ma55 = 0
minimo = 9999
maximo = -9999
Invitados=int(input("Ingrese el número de Invitados: "))
while Invitados <1 or Invitados >7:
    Invitados=int(input("Ingrese el número de Invitados(Maximo 7): "))
for i in range (Invitados):
    Edad=int(input("Ingrese la edad del invitado: "))
    while Edad <1 or Edad > 105:
        Edad=int(input("Ingrese la edad del invitado: "))
    Edades = Edades + Edad
    if Edad < 13 or Edad > 55:
        me13ma55 = me13ma55 + 1
    else:
        bt13a55 = bt13a55 + 1
    if Edad < minimo:
        minimo = Edad
    if Edad > maximo:
        maximo = Edad
for i in range (bt13a55):
    print("Parado")
for i in range (me13ma55):
    print("Asiento")
print("Promedio de edad: ", Edades/Invitados)
print("Invitado mas joven: ", minimo)
print("Invitado mas viejo: ", maximo)