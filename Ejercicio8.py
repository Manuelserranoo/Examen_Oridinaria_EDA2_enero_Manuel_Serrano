class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, other):
        return self.frecuencia < other.frecuencia


def construir_arbol_huffman(tabla_frecuencias):
    nodos = [NodoHuffman(simbolo, frecuencia) for simbolo, frecuencia in tabla_frecuencias.items()]

    while len(nodos) > 1:
        nodos = sorted(nodos, key=lambda x: x.frecuencia)
        nodo1 = nodos[0]
        nodo2 = nodos[1]
        nodos = nodos[2:]
        nodo_padre = NodoHuffman(None, nodo1.frecuencia + nodo2.frecuencia)
        nodo_padre.izquierda = nodo1
        nodo_padre.derecha = nodo2
        nodos.append(nodo_padre)

    return nodos[0]


def construir_tabla_codificacion(arbol_huffman):
    tabla_codificacion = {}

    def recorrer_arbol(nodo, codigo):
        if nodo.simbolo:
            tabla_codificacion[nodo.simbolo] = codigo
        else:
            recorrer_arbol(nodo.izquierda, codigo + "0")
            recorrer_arbol(nodo.derecha, codigo + "1")

    recorrer_arbol(arbol_huffman, "")

    return tabla_codificacion


def comprimir_mensaje(mensaje, tabla_codificacion):
    mensaje_comprimido = ""
    for caracter in mensaje:
        if caracter in tabla_codificacion:
            mensaje_comprimido += tabla_codificacion[caracter]

    return mensaje_comprimido


def descomprimir_mensaje(mensaje_comprimido, arbol_huffman):
    mensaje_descomprimido = ""
    nodo_actual = arbol_huffman

    for bit in mensaje_comprimido:
        if bit == "0":
            nodo_actual = nodo_actual.izquierda
        elif bit == "1":
            nodo_actual = nodo_actual.derecha

        if nodo_actual.simbolo:
            mensaje_descomprimido += nodo_actual.simbolo
            nodo_actual = arbol_huffman

    return mensaje_descomprimido


# Tabla de frecuencias
tabla_frecuencias = {
    "T": 0.15,
    "O": 0.15,
    "A": 0.12,
    "E": 0.10,
    "H": 0.09,
    "S": 0.07,
    "P": 0.07,
    "M": 0.07,
    "N": 0.06,
    "C": 0.06,
    "D": 0.05,
    "Z": 0.04,
    "K": 0.03,
    ",": 0.03
}

# Construir el árbol de Huffman
arbol_huffman = construir_arbol_huffman(tabla_frecuencias)

# Construir la tabla de codificación
tabla_codificacion = construir_tabla_codificacion(arbol_huffman)

# Mensaje de ejemplo para comprimir
mensaje = "HAZTE,CON,TODOS,POKEMON"

# Comprimir el mensaje
mensaje_comprimido = comprimir_mensaje(mensaje, tabla_codificacion)
print("Mensaje comprimido:", mensaje_comprimido)

# Descomprimir el mensaje
mensaje_descomprimido = descomprimir_mensaje(mensaje_comprimido, arbol_huffman)
print("Mensaje descomprimido:", mensaje_descomprimido)
