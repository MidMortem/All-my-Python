import random

razas = ['elf','halfling']
subrazas = ['high-elf','drow','wood-elf','lightfoot','stout']

raza = random.choice(razas)

if raza == 'elf' :
    subraza = random.choice(subrazas[0:3])
elif raza == 'halfling' :
    subraza = random.choice(subrazas[3:5])
    
print(raza, subraza)


aprender for y while


