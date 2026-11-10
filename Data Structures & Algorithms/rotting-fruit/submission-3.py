from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        
        # 1. Guardar podridas DIRECTAMENTE como tuplas y contar frescas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        timer = 0

        # 2. BFS por niveles
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr, nc))
            
            timer += 1

        # 3. Si quedaron frescas inalcanzables se retorna -1
        return timer if fresh == 0 else -1