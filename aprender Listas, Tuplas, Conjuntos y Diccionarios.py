# #listas, datos ordenatos heteogeneos y mutables

# lista = [20, True, 3.232,'el numero de tu vieja']

# lista[2] = 'su madre'
# lista[1] = [3,5,'aaaa']
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[-4])
# print(lista[-3])
# print(lista[-2])
# print(lista[-1])
##append agrega algo al final
##count dice cuantas veces se repite un elemento
##index dice la pocision donde aparece por primera vez un elemento
##remove elimina la primera aparicion de un elemento
# lista2 = [1, 2, 3, 4, 5, 3, 2, 5, 2, 3, 2, 2]
# lista2.append(6)
# print(lista2)
# print(lista2.count(2))
# print(lista2.index(4))
# lista2.remove(1)
# print(lista2)
# print(lista2.index(4))


# #tuplas, datos ordenatos heteogeneos pero no mutables

# tupla = ('ejemplo1', 3, 3.23, True, False, 'elfo')

# print(tupla)
# print(tupla[2])
# print(tupla.count(True))
# print(tupla.index(False))

# #conjuntos, no ordenados, heterogeneo pero solo con elementos inmutables, mutable y sin repeticion

# #{} o set
# print(set([5, 2, 3, 4, 75, 1.5]))
# print(set((5, 2, 3, 4, 75, 1.5)))
# print(set("52511.5"))

# conjunto = set([2, 3, 3, 4])
# print(conjunto)

# conjunto.add(1)
# print(conjunto)

# conjunto.remove(1)
# print(conjunto)

# conjunto2 = set([5, 3, 7, 8])
# conjunto3 = set([9, 10, 11, 12])
# conjunto4 = set([2, 3])
# print(conjunto, conjunto2, conjunto3)
# print(conjunto.intersection(conjunto2))
# print(conjunto2.issubset(conjunto))
# print(conjunto4.issubset(conjunto))
# print(conjunto & conjunto2)
#### A|B union, A-B diferencia, A>=B superconjunto, 
#### A&B interseccion, A^B diferencia simetrica, A<=B subconjunto



##diccionarios, relacionar pares de elementos {clave : valor} clave = key nos sirve para 
## identificar y buscar el elemento con el que tiene relacion al que llamaremos valor = value
## no tiene orden, heterogeneo con clave inmutable y mutable

diccionario = {1: 'uno', 2: 'dos'}
diccionario[3] = 'tres'
print(diccionario)

dict_lista_tuplas = dict([(1, 'uno'), (2, 'dos'), (3, 'tres')])
print(dict_lista_tuplas)

dict_lista_string = dict(uno = 1, dos = 2, tres = 3)
print(dict_lista_string)