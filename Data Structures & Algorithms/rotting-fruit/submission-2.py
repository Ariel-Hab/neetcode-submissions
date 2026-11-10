class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        rows,cols = len(grid),len(grid[0])
        rotten = deque()
        rotten_list = []
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_list.append((r,c))
                elif grid[r][c]==1:
                    fresh += 1
        rotten.append(rotten_list)

        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        timer = 0
        while rotten:
            rottens = rotten.popleft()
            rotten_list = [] 
            for row_fruit, col_fruit in rottens:  
                for row_dir,col_dir in DIRECTIONS:
                    nr, nc = row_fruit + row_dir, col_fruit + col_dir 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten_list.append((nr,nc))
                        fresh -= 1
            if rotten_list:
                rotten.append(rotten_list)
                timer += 1
            elif fresh > 0:
                timer = -1
        return timer