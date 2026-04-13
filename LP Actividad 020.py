# minimo = 9999
# for i in range (4):
#     num = int(input("Ingrese: "))
#     if num<minimo:
#         minimo = num
# print(minimo)

#"MAXIMOS Y MINIMOS"
# maximo = -9999
# minimo = 9999
# for i in range (3):
#     num = int(input("ingrese un nro:"))
#     if num>maximo:
#         maximo = num
#     if num<minimo:
#         minimo = num
# print(f"El numero maximo es: {maximo}")
# print(f"El numero minimo es: {minimo}")

maximo = -9999
minimo = 9999

for i in range (5):
    num = float(input("Ingrese su altura: "))
    while num <1.4 or num >2.25:
        print("Altura no válida. Ingrese una altura entre 1.4 y 2.25.")
        num = float(input("Ingrese su altura: "))
    if num>maximo:
        maximo = num
    if num<minimo:
        minimo = num

print("La altura máxima es: " , maximo)
print("La altura mínima es: " , minimo)