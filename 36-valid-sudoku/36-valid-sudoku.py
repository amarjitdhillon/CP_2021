from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. We can create 3 hashmaps; one for rows, one for cols and another for a square matrix
        2. The key, value pair for row and col hashmap will be row_id: set() and col_id: set()
        3. The key, value pair for matrix hashmap will be row_id//3, col_id//3: set()
        3. Return True if each of them is valid and False if any of them is invalid
        """
        
        rows_hashmap    = defaultdict(set)
        cols_hashmap    = defaultdict(set)
        square_hashmap  = defaultdict(set)
        
        # iterate over the board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    # skip it as its an empty value
                    continue
                
                # return false if the value exists
                if board[r][c] in rows_hashmap[r] or  board[r][c] in cols_hashmap[c] or  board[r][c] in square_hashmap[(r//3,c//3)]:
                    return False
                
                # else update the matrics
                rows_hashmap[r].add(board[r][c])
                cols_hashmap[c].add(board[r][c])
                square_hashmap[(r//3,c//3)].add(board[r][c])
                
        return True
       