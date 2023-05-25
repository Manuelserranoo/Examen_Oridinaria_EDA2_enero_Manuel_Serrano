def calcular_posibles_teletransportes(cantidad_movimientos):
    memo = {}  # Diccionario para memoización

    def contar_teletransportes(ruta_actual, movimientos_restantes):
        if movimientos_restantes == 0:
            return 1

        # Verificar si el resultado ya está en la memoización
        if (ruta_actual, movimientos_restantes) in memo:
            return memo[(ruta_actual, movimientos_restantes)]

        total_teletransportes = 0

        if ruta_actual == 0:
            total_teletransportes += contar_teletransportes(4, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(6, movimientos_restantes - 1)
        elif ruta_actual == 1:
            total_teletransportes += contar_teletransportes(6, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(8, movimientos_restantes - 1)
        elif ruta_actual == 2:
            total_teletransportes += contar_teletransportes(7, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(9, movimientos_restantes - 1)
        elif ruta_actual == 3:
            total_teletransportes += contar_teletransportes(4, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(8, movimientos_restantes - 1)
        elif ruta_actual == 4:
            total_teletransportes += contar_teletransportes(3, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(9, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(0, movimientos_restantes - 1)
        elif ruta_actual == 5:
            return 0
        elif ruta_actual == 6:
            total_teletransportes += contar_teletransportes(1, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(7, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(0, movimientos_restantes - 1)
        elif ruta_actual == 7:
            total_teletransportes += contar_teletransportes(2, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(6, movimientos_restantes - 1)
        elif ruta_actual == 8:
            total_teletransportes += contar_teletransportes(1, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(3, movimientos_restantes - 1)
        elif ruta_actual == 9:
            total_teletransportes += contar_teletransportes(2, movimientos_restantes - 1)
            total_teletransportes += contar_teletransportes(4, movimientos_restantes - 1)

        # Guardar el resultado en la memoización
        memo[(ruta_actual, movimientos_restantes)] = total_teletransportes

        return total_teletransportes

    # Llamar a la función recursiva para cada ruta inicial
    posibilidades_validas = sum(contar_teletransportes(ruta, cantidad_movimientos) for ruta in range(10))

    return posibilidades_validas


# Ejemplo de uso
cantidad_movimientos3 = 3
cantidad_movimientos5 = 5
posibilidades_validas5 = calcular_posibles_teletransportes(cantidad_movimientos5)
posibilidades_validas3 = calcular_posibles_teletransportes(cantidad_movimientos3)
print("Posibilidades válidas para", cantidad_movimientos5, "movimientos:", posibilidades_validas5)
print("Posibilidades válidas para", cantidad_movimientos3, "movimientos:", posibilidades_validas3)
