#sumador = 0
#for i in range (5):
#    numero = int(input("Ingrese un número: "))
#    sumador += numero
#print("La suma de los números ingresados es:", sumador)

#contador = 0
#for i in range(5):
#    numero = int(input("Ingrese un número: "))
#    if numero > 10:
#        contador += 1
#print("La cantidad de números mayores a 10 es:", contador)


Toalla = 0
Sabana = 0
Acolchado = 0

Toalla_Precio = 17500
Sabana_Precio = 32000
Acolchado_Precio = 55000

print ("""Bienvenido a la tienda de ropa de cama: 
       Toallas: $17,500 
       Sabanas: $32,000 
       Acolchados: $55,000""")
for i in range(5):
    Producto = input("Ingrese el producto que desea comprar (Toalla, Sabana, Acolchado): ").lower()
    if Producto == "toalla":
        Toalla += 1
    elif Producto == "sabana":
        Sabana += 1
    elif Producto == "acolchado":
        Acolchado += 1
    else:
        print("Producto no válido")
Total = (Toalla * Toalla_Precio) + (Sabana * Sabana_Precio) + (Acolchado * Acolchado_Precio)
print("El total a pagar es: $", Total)