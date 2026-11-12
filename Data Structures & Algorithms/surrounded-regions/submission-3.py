from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r: int, c: int) -> None:
            # Base cases: out of bounds or not an unvisited 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return

            # Mark current cell as safe
            board[r][c] = 'T'

            # Visit all 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Run DFS from all border cells
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r, c)

        # 2. Update the entire board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'  # Connected to border -> restore to 'O'
                else:
                    board[r][c] = 'X'  # Surrounded or already 'X' -> set to 'X'