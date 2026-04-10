#for x in range (2,21,2):
#inicio limite incremento
#                    print(x)
#contador_felino = 0
#contador_canino = 0
#for i in range(10):
#animal = input("Ingrese el nombre de un animal: ").lower()
#if animal == "gato" or animal == "tigre" or animal == "leon":
#print("felino")
#contador_felino = contador_felino + 1
#elif animal == "perro" or animal == "lobo" or animal == "zorro":
#print("canino")
#contador_canino = contador_canino + 1
#else:
#print("desconocido")
#print("Cantidad de felinos:", contador_felino)
#print("Cantidad de caninos:", contador_canino)
for i in range(4):
    Puntaje = int(input("Ingrese una Puntuación: "))
    if Puntaje < 15:
        print("VUELVA A INTENTARLO")
    elif Puntaje >= 15 and Puntaje < 30:
        print("BUEN PUNTAJE")
    elif Puntaje >= 30 and Puntaje < 55:
        print("EXCELENTE PUNTAJE")
    elif Puntaje >= 55:
        print("PERFECTO")