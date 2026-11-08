class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        filas = len(grid)
        cols = len(grid[0])
        def hundir(r, c):
            # Caso base: fuera de la grilla o agua → no hay nada que hundir
            if r < 0 or r >= filas or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"        # la hundo (= la marco como visitada)
            hundir(r + 1, c)        # abajo
            hundir(r - 1, c)        # arriba
            hundir(r, c + 1)        # derecha
            hundir(r, c - 1)        # izquierda
        islas = 0
        for r in range(filas):
            for c in range(cols):
                if grid[r][c] == "1":
                    islas += 1
                    hundir(r,c)
        return islas