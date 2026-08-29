class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        for row in range(9):
            for column in range(9):
                #check requirements
                val = board[row][column]
                if val == ".":
                    continue
                if not val.isdigit() or not (1 <= int(val) <= 9):
                    return False
                int_val = int(val)

                #assign values
                row_value = (int_val, "row", row)
                column_value = (int_val, "column", column)
                square_value = (int_val, "square", row//3, column//3)

                if row_value in hashset or column_value in hashset or square_value in hashset:
                    return False
                hashset.add(row_value)
                hashset.add(column_value)
                hashset.add(square_value)
        return True


            

                
