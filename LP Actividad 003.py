edad = input("Ingrese su edad: ")
peso = input("Ingrese su peso: ")
altura = input("Ingrese su altura: ")
edad = int(edad)
peso = float(peso)
altura = float(altura)

if edad > 15 and peso < 110.5 and altura > 1.48 and altura < 2.15 :
    print("Puede ingresar, que se divierta!")
else:
    print("No puede ingresar")