import tkinter as tk


class InterfazLaberinto:

    TAM_CELDA = 50

    def __init__(self, laberinto):
        self.laberinto = laberinto

        self.ventana = tk.Tk()
        self.ventana.title("Laberinto 10x10")

        self.canvas = tk.Canvas(
            self.ventana,
            width=laberinto.COLUMNAS * self.TAM_CELDA,
            height=laberinto.FILAS * self.TAM_CELDA
        )

        self.canvas.pack()

        self.dibujar_laberinto()

    def dibujar_laberinto(self):

        self.canvas.delete("all")

        for fila in range(self.laberinto.FILAS):

            for columna in range(self.laberinto.COLUMNAS):

                x1 = columna * self.TAM_CELDA
                y1 = fila * self.TAM_CELDA

                x2 = x1 + self.TAM_CELDA
                y2 = y1 + self.TAM_CELDA

                celda = self.laberinto.obtener_celda(
                    fila,
                    columna
                )

                # Determinar color
                if celda == self.laberinto.PARED:
                    color = "black"
                elif celda == self.laberinto.SALIDA:
                    color = "green"
                else:
                    color = "white"

                # Dibujar cuadrado
                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="gray"
                )

                # Mostrar inicio
                if (fila, columna) == self.laberinto.inicio:

                    self.canvas.create_text(
                        x1 + self.TAM_CELDA / 2,
                        y1 + self.TAM_CELDA / 2,
                        text="I",
                        fill="blue",
                        font=("Arial", 18, "bold")
                    )

                # Mostrar salida
                elif celda == self.laberinto.SALIDA:

                    self.canvas.create_text(
                        x1 + self.TAM_CELDA / 2,
                        y1 + self.TAM_CELDA / 2,
                        text="S",
                        fill="white",
                        font=("Arial", 18, "bold")
                    )

    def dibujar_camino_bfs(self, camino):
        """Dibuja el camino BFS con óvalos azules sobre el canvas."""
        for fila, columna in camino:
            if (fila, columna) != self.laberinto.inicio and (fila, columna) != self.laberinto.salida:
                x1 = columna * self.TAM_CELDA + self.TAM_CELDA * 0.25
                y1 = fila * self.TAM_CELDA + self.TAM_CELDA * 0.25
                x2 = (columna + 1) * self.TAM_CELDA - self.TAM_CELDA * 0.25
                y2 = (fila + 1) * self.TAM_CELDA - self.TAM_CELDA * 0.25
                self.canvas.create_oval(
                    x1, y1, x2, y2,
                    fill="#4FC3F7",
                    outline="#0288D1",
                    width=2
                )

    def dibujar_camino_dfs(self, camino):
        """Dibuja el camino DFS con óvalos naranjas sobre el canvas."""
        for fila, columna in camino:
            if (fila, columna) != self.laberinto.inicio and (fila, columna) != self.laberinto.salida:
                x1 = columna * self.TAM_CELDA + self.TAM_CELDA * 0.25
                y1 = fila * self.TAM_CELDA + self.TAM_CELDA * 0.25
                x2 = (columna + 1) * self.TAM_CELDA - self.TAM_CELDA * 0.25
                y2 = (fila + 1) * self.TAM_CELDA - self.TAM_CELDA * 0.25
                self.canvas.create_oval(
                    x1, y1, x2, y2,
                    fill="#FFB74D",
                    outline="#E65100",
                    width=2
                )

    def ejecutar(self):
        self.ventana.mainloop()