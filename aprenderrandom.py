import random 
# # random sirve para numeros entre 0 y 1
# r1 = random.random()
# print(r1)

# #uniform para numeros al azar entre 2 numeros
# r2 = random.uniform(1,19)
# print(r2)

# #randint para integers entre 2 numeros incluyendo esos numeros
# r3 = random.randint(1,6)
# print(r3)

# #choice sirve para elegir entre opciones
# saludos = ['hola', 'como va?', 'me das asco', 'buenos días', '*mira fijamente*']
# r4 = random.choice(saludos)
# print(r4 + ', trola')

# #choices sirve para varios resultados
# #k es cuantos resultados
# #weights sirve para decidis la probavilidad de cada opcion
# colores = ['rojo', 'negro', 'verde']
# r5 = random.choices(colores, k=10)
# print(r5)
# r6 = random.choices(colores,weights=[18, 18, 2], k=10)
# print(r6)

# #shuffle sirve para mezclar listas al azar
# mazo = list(range(1, 53))
# # random.shuffle(mazo)
# # print(mazo)
# #sample agarra una cantidad denotada por k al azar de valores de una lista
# mano = random.sample(mazo, k=5)
# print(mano)

def throw_dice():
    return random.randint(1, 6)

result = throw_dice()
print(f"You rolled a {result}")