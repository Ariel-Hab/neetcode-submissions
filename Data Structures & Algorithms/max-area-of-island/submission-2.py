class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        filas = len(grid)
        cols = len(grid[0])
        def hundir(r,c)->int:
            area = 1
            if r < 0 or r >= filas or c < 0 or c >= cols or grid[r][c]==0:
                return 0  
            grid[r][c] = 0
            area += hundir(r-1, c)
            area += hundir(r,c-1)
            area += hundir(r+1,c)
            area += hundir(r,c+1)
            return area
        maxArea = 0
        for r in range(filas):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = hundir(r,c)
                    maxArea = max(area, maxArea)
        return maxArea