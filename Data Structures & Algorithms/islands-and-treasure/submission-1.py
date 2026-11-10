from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Modifica grid in-place.
        """
        if not grid or not grid[0]:
            return

        filas, cols = len(grid), len(grid[0])
        cola = deque()

        # 1. Agregamos todos los cofres (0) a la cola inicial
        for r in range(filas):
            for c in range(cols):
                if grid[r][c] == 0:
                    cola.append((r, c))

        DIRECCIONES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. Expandir nivel por nivel (la primera vez que llegas a una celda es la distancia mínima)
        while cola:
            r, c = cola.popleft()

            for dr, dc in DIRECCIONES:
                nr, nc = r + dr, c + dc

                # Solo avanzamos si está en rango y es una celda vacía (2147483647)
                if 0 <= nr < filas and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    cola.append((nr, nc))