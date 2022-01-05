class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        '''
        1. First step is to find if the conversion is legal and that can be done by equating the row*col of existing and new matrix
        2. if conversion is possible then there can be 3 cases
            - # rows and cols are same
            - no of new rows > old rows in mat, so we need to copy the column values as rows
            - no of new rows < old rows in mat, so we need to copy the rows as a col
        '''
        
        if len(mat) == 0:
            return mat
        
        rows = len(mat)
        cols = len(mat[0])
        
        
        def is_valid_conversion():
            return rows*cols == r*c
        
        
        def perform_coversion():
            result = [[0 for x in range(c)] for y in range(r)]
            
            c_index , r_index = 0,0
            for row in range(rows):
                for col in range(cols):
                    if c_index == c:
                        r_index += 1
                        c_index = 0
                    result[r_index][c_index] = mat[row][col]
                    c_index += 1
            return result
                    
                    
        # return the original array if the conversion is not valid
        if not is_valid_conversion():
            return mat
        
        return perform_coversion()