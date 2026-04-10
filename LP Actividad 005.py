for i in range(3):
   print("Verificacion para ingreso a muntaña rusa")
   edad = int(input("ingrese su edad: " ))
   peso = float(input("ingrese su peso: "))
   altura = float(input("ingrese su altura: "))

   if edad >= 16 and peso < 120.5 and altura > 1.40 and altura < 2.15 :
       print("Pase usted es apto para la montaña rusa")
   else :
       print("Lo siento usted no es apto para la montaña rusa")