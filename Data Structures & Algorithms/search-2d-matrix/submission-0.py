import math

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # Mapeo de índice 1D a coordenadas 2D (fila, col)
            mid_row = mid // n
            mid_col = mid % n
            val = matrix[mid_row][mid_col]
            if (val == target):
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid -1
            
        return False

