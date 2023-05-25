from datetime import datetime

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = datetime.strptime(fecha_fabricacion, "%Y-%m-%d")
        print(f"¡Se ha creado la Pokeball {self.nombre} con éxito!")

    def __str__(self):
        return f"Información de la Pokeball:\nNombre: {self.nombre}\nPeso: {self.peso} g\nPrecio: {self.precio} $\
                \nFecha de fabricación: {self.fecha_fabricacion.strftime('%Y-%m-%d')}"

    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"El precio de la Pokeball {self.nombre} ha sido modificado. Nuevo precio: {self.precio} $")


# Crear algunas Pokeballs
pokeball1 = Pokeball(50, "Great Ball", 200, "2023-05-25")
pokeball2 = Pokeball(100, "Ultra Ball", 500, "2023-05-26")
pokeball3 = Pokeball(80, "Master Ball", 1000, "2023-05-24")

# Mostrar los datos de las Pokeballs ordenadas por fecha de fabricación
pokeballs = [pokeball1, pokeball2, pokeball3]
pokeballs_ordenadas = sorted(pokeballs, key=lambda x: x.fecha_fabricacion)

print("Pokeballs ordenadas por fecha de fabricación:")
for pokeball in pokeballs_ordenadas:
    print(pokeball)
    print()

# Modificar el precio de una Pokeball
pokeball2.modificar_precio(600)
