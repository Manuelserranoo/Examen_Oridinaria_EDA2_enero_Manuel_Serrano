import random


class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel}"


class TablaHashEncadenada:
    def __init__(self):
        self.tabla = {}

    def agregar_pokemon(self, pokemon):
        key = self.generar_clave(pokemon)
        if key in self.tabla:
            self.tabla[key].append(pokemon)
        else:
            self.tabla[key] = [pokemon]

    def generar_clave(self, pokemon):
        raise NotImplementedError("Debe implementar este método en una subclase.")


class TablaHashPorNivel(TablaHashEncadenada):
    def generar_clave(self, pokemon):
        return pokemon.nivel % 1000


class TablaHashPorTipo(TablaHashEncadenada):
    def generar_clave(self, pokemon):
        return pokemon.tipo[0]


def generar_pokemon():
    tipos = ["Agua", "Fuego", "Tierra", "Eléctrico", "Normal", "Fantasma"]
    pokemons = []
    for _ in range(800):
        nombre = f"Pokemon-{_+1}"
        tipo = random.choice(tipos)
        nivel = random.randint(1, 100)
        pokemons.append(Pokemon(nombre, tipo, nivel))
    return pokemons


def cargar_pokemons_en_tablas(pokemons, tabla_nivel, tabla_tipo):
    for pokemon in pokemons:
        tabla_nivel.agregar_pokemon(pokemon)
        tabla_tipo.agregar_pokemon(pokemon)


def buscar_pokemon_desertor(tabla_nivel):
    pokemons_nivel = tabla_nivel.tabla.get(187 % 1000, [])
    for pokemon in pokemons_nivel:
        if pokemon.tipo == "Fantasma" and pokemon.nivel == 187:
            return pokemon
    return None


def obtener_pokemons_por_terminacion(tabla_nivel, terminacion):
    pokemons_terminacion = []
    for nivel, lista_pokemons in tabla_nivel.tabla.items():
        for pokemon in lista_pokemons:
            if str(pokemon.nivel)[-2:] == terminacion:
                pokemons_terminacion.append(pokemon)
    return pokemons_terminacion


def obtener_pokemons_por_tipo(tabla_tipo, tipo):
    return tabla_tipo.tabla.get(tipo[0], [])


# Generar los 800 Pokémon
pokemons = generar_pokemon()

# Crear las tablas hash
tabla_nivel = TablaHashPorNivel()
tabla_tipo = TablaHashPorTipo()

# Cargar los Pokémon en las tablas
cargar_pokemons_en_tablas(pokemons, tabla_nivel, tabla_tipo)

# Buscar al Pokémon Fantasma de nivel 187 y quitarlo
pokemon_desertor = buscar_pokemon_desertor(tabla_nivel)
if pokemon_desertor:
    tabla_nivel.tabla[187 % 1000].remove(pokemon_desertor)

# Obtener los Pokémon terminados en 78 para la misión de asalto
pokemons_asalto = obtener_pokemons_por_terminacion(tabla_nivel, "78")

# Obtener los Pokémon terminados en 37 para la misión de exploración
pokemons_exploracion = obtener_pokemons_por_terminacion(tabla_nivel, "37")

# Obtener los Pokémon de tipo Tierra para la misión de exploración al Bosque Verdanturf
pokemons_tierra = obtener_pokemons_por_tipo(tabla_tipo, "Tierra")

# Obtener los Pokémon de tipo Fuego para la misión de exterminación en Cueva Lava
pokemons_fuego = obtener_pokemons_por_tipo(tabla_tipo, "Fuego")

# Imprimir los resultados
print(f"Pokémon desertor: {pokemon_desertor}")
print(f"Pokémon para la misión de asalto: {pokemons_asalto}")
print(f"Pokémon para la misión de exploración: {pokemons_exploracion}")
print(f"Pokémon de tipo Tierra para la misión al Bosque Verdanturf: {pokemons_tierra}")
print(f"Pokémon de tipo Fuego para la misión en Cueva Lava: {pokemons_fuego}")
