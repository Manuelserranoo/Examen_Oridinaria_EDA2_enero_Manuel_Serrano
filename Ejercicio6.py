def encontrar_soluciones(n):
    soluciones_distintas = []
    solucion_actual = [-1] * n  # Vector de n posiciones inicializado con -1
    contar_pokemon(0, n, solucion_actual, soluciones_distintas)
    return soluciones_distintas

def contar_pokemon(i, n, solucion_actual, soluciones_distintas):
    if i == n:  # Se han ubicado todos los Pokémon
        soluciones_distintas.append(solucion_actual.copy())
        return

    for fila in range(n):
        if es_valida(i, fila, solucion_actual):
            solucion_actual[i] = fila
            contar_pokemon(i + 1, n, solucion_actual, soluciones_distintas)
            solucion_actual[i] = -1

def es_valida(i, fila, solucion_actual):
    for j in range(i):
        if solucion_actual[j] == fila or abs(solucion_actual[j] - fila) == abs(j - i):
            return False
    return True

# Ejemplo de uso
n = 4
soluciones_distintas = encontrar_soluciones(n)

print("Número de soluciones distintas para n =", n, ":", len(soluciones_distintas))
print("Soluciones distintas:")
for i, solucion in enumerate(soluciones_distintas):
    print("Solución", i + 1, ":")
    for fila in solucion:
        for columna in range(len(solucion)):
            if columna == fila:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
