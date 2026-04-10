import random

# Character data structure - maps race to age range and subraces
races = {
    'elf': {'age': (100, 750), 'subraces': ['drow', 'high', 'wood']},
    'dwarf': {'age': (50, 350), 'subraces': ['mountain', 'hill', 'duergar']},
    'human': {'age': (18, 100), 'subraces': ['variant']},
    'orc': {'age': (12, 50), 'subraces': []},
    'halfling': {'age': (20, 200), 'subraces': ['lightfoot', 'stout']},
    'gnome': {'age': (40, 500), 'subraces': ['forest', 'rock']},
    'half-elf': {'age': (20, 180), 'subraces': []},
    'tiefling': {'age': (18, 100), 'subraces': ['Asmodeus', 'Mephistopheles', 'Zariel', 'Dispater', 'Fierna', 'Belial', 'Baalzebul', 'Glasya']},
    'dragonborn': {'age': (15, 80), 'subraces': ['black', 'blue', 'brass', 'bronze', 'copper', 'gold', 'green', 'red', 'silver', 'white', 'amethyst', 'crystal', 'emerald', 'sapphire', 'topaz']},
    'half-orc': {'age': (14, 80), 'subraces': []},
    'genasi': {'age': (18, 120), 'subraces': ['air', 'earth', 'fire', 'water']},
    'kenku': {'age': (12, 60), 'subraces': []},
    'tortle': {'age': (15, 50), 'subraces': []},
    'bugbear': {'age': (16, 80), 'subraces': []},
    'goblin': {'age': (8, 60), 'subraces': []},
    'hobgoblin': {'age': (18, 100), 'subraces': []},
    'kobold': {'age': (6, 120), 'subraces': []},
    'lizardfolk': {'age': (14, 60), 'subraces': []},
}

clases = ['Bard', 'Fighter', 'Wizard', 'Cleric', 'Artificer', 'Barbarian', 'Druid', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock']
generos = ['Male', 'Female']


def choose_option(prompt: str, options: list[str]) -> str | None:
    """Let the user choose an option (number or name).

    - Press Enter: random choice
    - Type "r" or "random": skip all remaining prompts and randomize the rest
    """
    print(f"\n{prompt} (press Enter for random, or type 'r' to randomize rest)")
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")

    choice = input("Choose number or name: ").strip()
    if not choice:
        return random.choice(options)

    if choice.lower() in {"r", "random"}:
        return None

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(options):
            return options[idx]

    for opt in options:
        if opt.lower() == choice.lower():
            return opt

    print("Invalid choice; picking randomly.")
    return random.choice(options)


# Generate character (mix random and user choice)
raza = choose_option("Pick a race", list(races.keys()))
if raza is None:
    # User chose to randomize everything
    raza = random.choice(list(races.keys()))
    raza_datos = races[raza]
    subraza = (
        random.choice(raza_datos["subraces"])
        if raza_datos["subraces"]
        else "No subrace"
    )
    edad = random.randint(*raza_datos["age"])
    genero = random.choice(generos)
    clase = random.choice(clases)
else:
    raza_datos = races[raza]
    subraza_choice = (
        choose_option(f"Pick a subrace for {raza}", raza_datos["subraces"])
        if raza_datos["subraces"]
        else "No subrace"
    )
    if subraza_choice is None:
        # Randomize remaining 12
        subraza = (
            random.choice(raza_datos["subraces"])
            if raza_datos["subraces"]
            else "No subrace"
        )
        edad = random.randint(*raza_datos["age"])
        genero = random.choice(generos)
        clase = random.choice(clases)
    else:
        subraza = subraza_choice
        edad = random.randint(*raza_datos["age"])
        genero = choose_option("Pick a gender", generos)
        if genero is None:
            genero = random.choice(generos)
            clase = random.choice(clases)
        else:
            clase_choice = choose_option("Pick a class", clases)
            clase = random.choice(clases) if clase_choice is None else clase_choice

# Display character
if raza == 'tiefling':
    pj = f"bloodline of {subraza} {raza} {clase} {genero} Age: {edad}"
else:
    pj = f"{subraza} {raza} {clase} {genero} Age: {edad}"
print(pj)