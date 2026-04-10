import random

valores = [1, 2, 3, 4, 5, 6]

for num in range (10):
    tirada = random.choices(valores, k=5)
    print(tirada)