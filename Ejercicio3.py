
class Pokemon:
    def __init__(self, nombre, tipo, ps, ataque, defensa, ataque_especial, defensa_especial, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.ps = ps
        self.ataque = ataque
        self.defensa = defensa
        self.ataque_especial = ataque_especial
        self.defensa_especial = defensa_especial
        self.velocidad = velocidad
        print(f"¡Se ha creado el Pokémon {self.nombre} de tipo {self.tipo} con éxito!")

    def clasificacion(self):
        print(f"Clasificación del Pokémon {self.nombre}:")
        print("PS:", self.ps)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)
        print("Ataque Especial:", self.ataque_especial)
        print("Defensa Especial:", self.defensa_especial)
        print("Velocidad:", self.velocidad)


    def __str__(self):
        return f"Nombre: {self.nombre}\nTipo: {self.tipo}\nPS: {self.ps}\nAtaque: {self.ataque}\nDefensa: {self.defensa}\nAtaque Especial: {self.ataque_especial}\nDefensa Especial: {self.defensa_especial}\nVelocidad: {self.velocidad}"

# Ejemplo de uso
pokemon1 = Pokemon("Pikachu", "Eléctrico", 35, 55, 40, 50, 50, 90)
pokemon2 = Pokemon("Charizard", "Fuego", 78, 84, 78, 109, 85, 100)
pokemon3 = Pokemon("Blastoise", "Agua", 79, 83, 100, 85, 105, 78)

pokemons = [pokemon1, pokemon2, pokemon3]

for pokemon in pokemons:
    print(pokemon)
    print()