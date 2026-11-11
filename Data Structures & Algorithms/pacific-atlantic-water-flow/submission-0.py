from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r: int, c: int, ocean_set: set):
            ocean_set.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Water flows downhill to the ocean, so going backwards means moving uphill:
                    # heights[nr][nc] >= heights[r][c]
                    if (nr, nc) not in ocean_set and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, ocean_set)

        # 1. Start DFS from Pacific borders (top row and left column)
        for c in range(cols):
            dfs(0, c, pacific)              # Top row
        for r in range(rows):
            dfs(r, 0, pacific)              # Left column

        # 2. Start DFS from Atlantic borders (bottom row and right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)       # Bottom row
        for r in range(rows):
            dfs(r, cols - 1, atlantic)       # Right column

        # 3. Find intersection of cells reachable by both oceans
        return list(pacific & atlantic)