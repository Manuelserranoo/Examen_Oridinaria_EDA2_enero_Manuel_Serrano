import unittest

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print(f"¡Se ha creado la Pokeball {self.nombre} con éxito!")

    def __str__(self):
        return f"Pokeball: {self.nombre}\nPeso: {self.peso}\nPrecio: {self.precio}\nFecha de fabricación: {self.fecha_fabricacion}"


class PokeballTests(unittest.TestCase):
    def setUp(self):
        self.pokeball1 = Pokeball(50, "Ultra Ball", 1000, "2023-05-20")
        self.pokeball2 = Pokeball(30, "Great Ball", 500, "2023-05-22")
        self.pokeball3 = Pokeball(20, "Poke Ball", 200, "2023-05-21")

    def test_pokeball_creation(self):
        self.assertEqual(self.pokeball1.nombre, "Ultra Ball")
        self.assertEqual(self.pokeball2.peso, 30)
        self.assertEqual(self.pokeball3.precio, 200)
        self.assertEqual(self.pokeball1.fecha_fabricacion, "2023-05-20")

    def test_pokeball_str(self):
        expected_output = "Pokeball: Ultra Ball\nPeso: 50\nPrecio: 1000\nFecha de fabricación: 2023-05-20"
        self.assertEqual(str(self.pokeball1), expected_output)

    def test_pokeball_sorting(self):
        pokeballs = [self.pokeball1, self.pokeball2, self.pokeball3]
        sorted_pokeballs = sorted(pokeballs, key=lambda x: x.fecha_fabricacion)
        self.assertEqual(sorted_pokeballs, [self.pokeball1, self.pokeball3, self.pokeball2])

    def test_pokeball_price_update(self):
        self.assertEqual(self.pokeball1.precio, 1000)
        self.pokeball1.precio = 1200
        self.assertEqual(self.pokeball1.precio, 1200)


if __name__ == "__main__":
    unittest.main()
