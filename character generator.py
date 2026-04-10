import random

razas = ['Elf', 'dwarf', 'human', 'orc', 'halfling', 'gnome', 'half-elf', 'tiefling', 'dragonborn',  'half-orc']
clases = ['Bard', 'Fighter', 'Wizard', 'cleric', 'artificer', 'barbarian', 'druid', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', ]
generos = ['masculino', 'femenino']
edades = ['young', 'adult', 'old']

raza= random.choice(razas)
genero= random.choice(generos)
clase= random.choice(clases)
edad= random.choice(edades)
pj = f'{raza} {clase} {genero} {edad}'
print(pj)