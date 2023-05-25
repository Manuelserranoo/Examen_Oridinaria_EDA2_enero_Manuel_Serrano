import unittest

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


# Pruebas utilizando el módulo unittest
class PokemonTests(unittest.TestCase):
    def test_creacion_pokemon(self):
        pokemon = Pokemon("Pikachu", "Eléctrico", 35, 55, 40, 50, 50, 90)
        self.assertEqual(pokemon.nombre, "Pikachu")
        self.assertEqual(pokemon.tipo, "Eléctrico")
        self.assertEqual(pokemon.ps, 35)
        self.assertEqual(pokemon.ataque, 55)
        self.assertEqual(pokemon.defensa, 40)
        self.assertEqual(pokemon.ataque_especial, 50)
        self.assertEqual(pokemon.defensa_especial, 50)
        self.assertEqual(pokemon.velocidad, 90)

    def test_str_repr(self):
        pokemon = Pokemon("Charizard", "Fuego", 78, 84, 78, 109, 85, 100)
        self.assertEqual(str(pokemon), "Nombre: Charizard\nTipo: Fuego\nPS: 78\nAtaque: 84\nDefensa: 78\nAtaque Especial: 109\nDefensa Especial: 85\nVelocidad: 100")


if __name__ == "__main__":
    unittest.main()
