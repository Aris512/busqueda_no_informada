from laberinto import Laberinto
from Interfaz import InterfazLaberinto


def main():

    # Crear objeto Laberinto
    laberinto = Laberinto(porcentaje_paredes=30)

    # Mostrar matriz por consola
    laberinto.mostrar()

    # Crear interfaz
    interfaz = InterfazLaberinto(laberinto)


    #pruebas del bfs, se guardan las posiciones para enviarlas a interfaz.py
    camino_bfs = []
    longitud = bfs_longitud(laberinto, camino_bfs)
    print("Longitud del camino más corto (BFS):", longitud)
    print("Camino encontrado (BFS):", camino_bfs)


    #primero crea una copia del laberinto 
    #pruebas del dfs, se guardan las posiciones para enviarlas a interfaz.py
    copia = [fila[:] for fila in laberinto.matriz]
    camino_dfs = []
    if dfs_camino(copia, 0, 0, camino_dfs, set(), laberinto.salida):
        print("Camino encontrado (DFS):", camino_dfs)
        print("Movimientos (celdas - 1):", len(camino_dfs) - 1)
    else:
        print("DFS: no hay camino disponible.")

    # Dibujar caminos en la interfaz
    if camino_bfs:
        interfaz.dibujar_camino_bfs(camino_bfs)
    if camino_dfs:
        interfaz.dibujar_camino_dfs(camino_dfs)

    # Ejecutar Tkinter
    interfaz.ejecutar()



#usamos el algoritmo de la clase, adaptado a nuestras clases
def bfs_longitud(laberinto, camino_out=None):
    from collections import deque

    lab = laberinto.matriz
    filas, cols = len(lab), len(lab[0])
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izq, arriba

    inicio = laberinto.inicio
    # Cada elemento: (fila, col, camino_acumulado)
    cola = deque([(inicio[0], inicio[1], [inicio])])       # (fila, columna, camino)
    #lista de los visitados
    visitados = {inicio}

    while cola:
        fila, col, camino = cola.popleft()

        # TODO 1: si (fila, col) es la salida, guarda el camino y devuelve distancia
        if (fila, col) == laberinto.salida:
            if camino_out is not None:
                camino_out.extend(camino)
            return len(camino) - 1

        for df, dc in direcciones:
            nf, nc = fila + df, col + dc
            # TODO 2: comprueba límites, que no sea pared y que no esté visitada.
            #         Si es válida: márcala visitada y añádela a la cola con dist+1.
            # limites
            if 0 <= nf < filas and 0 <= nc < cols:
                # que no es pared
                if lab[nf][nc] != laberinto.PARED:
                    # no esta en lista visitados
                    if (nf, nc) not in visitados:
                        visitados.add((nf, nc))
                        cola.append((nf, nc, camino + [(nf, nc)]))

    return -1   # no hay camino



def dfs_camino(lab, x, y, camino, visitados, salida):
    # ¿Llegamos a la salida?
    if (x, y) == salida:
        camino.append((x, y))
        return True

    visitados.add((x, y))
    camino.append((x, y))

    # TODO 3: recorre los 4 movimientos (abajo, derecha, arriba, izquierda).
    #         Para cada vecino válido (dentro de límites, no pared, no visitado):
    #         llama recursivamente a dfs_camino; si devuelve True, propaga True.
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        # que este dentro limites
        if 0 <= nx < len(lab) and 0 <= ny < len(lab[0]):
            # que no es pared (permite celdas 0 y la salida 'S')
            if lab[nx][ny] != 1:
                # no esta en lista visitados
                if (nx, ny) not in visitados:
                    # llamada recursiva para el backtracking
                    if dfs_camino(lab, nx, ny, camino, visitados, salida):
                        return True

    # TODO 4: backtracking — si ninguna dirección funcionó, quita esta celda del camino
    camino.pop()
    return False



if __name__ == "__main__":
    main()