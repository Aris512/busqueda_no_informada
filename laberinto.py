import random


class Laberinto:
    FILAS = 10
    COLUMNAS = 10

    VACIO = 0
    PARED = 1
    SALIDA = "S"

    def __init__(self, porcentaje_paredes=30):
        self.porcentaje_paredes = porcentaje_paredes

        # Posición inicial
        self.inicio = (0, 0)

        # Crear la matriz
        self.matriz = []

        # Generar laberinto
        self.generar()

    def generar(self):
        """Genera las paredes y la salida aleatoriamente."""

        # Crear matriz vacía
        self.matriz = [
            [self.VACIO for _ in range(self.COLUMNAS)]
            for _ in range(self.FILAS)
        ]

        # Colocar paredes
        for fila in range(self.FILAS):
            for columna in range(self.COLUMNAS):

                # Nunca colocar pared en el inicio
                if (fila, columna) == self.inicio:
                    continue

                numero = random.randint(1, 100)

                if numero <= self.porcentaje_paredes:
                    self.matriz[fila][columna] = self.PARED

        # Buscar posiciones vacías
        posiciones_disponibles = []

        for fila in range(self.FILAS):
            for columna in range(self.COLUMNAS):

                if (fila, columna) == self.inicio:
                    continue

                if self.matriz[fila][columna] == self.VACIO:
                    posiciones_disponibles.append((fila, columna))

        # Elegir salida aleatoriamente
        salida = random.choice(posiciones_disponibles)

        self.matriz[salida[0]][salida[1]] = self.SALIDA

        # Guardar posición de la salida
        self.salida = salida

    def obtener_celda(self, fila, columna):
        """Devuelve el contenido de una celda."""
        return self.matriz[fila][columna]

    def es_valida(self, fila, columna):
        """Comprueba que la posición esté dentro de la matriz."""
        return (
            0 <= fila < self.FILAS
            and 0 <= columna < self.COLUMNAS
        )

    def es_transitable(self, fila, columna):
        """Indica si una celda puede ser recorrida."""
        if not self.es_valida(fila, columna):
            return False

        return self.matriz[fila][columna] != self.PARED

    def mostrar(self):
        """Muestra el laberinto por consola."""
        for fila in self.matriz:
            print(" ".join(map(str, fila)))