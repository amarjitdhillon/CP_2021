class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        C = len(mat[0])
        R = len(mat)
        
        # first transformation
        for r in range(R):
            for c in range(r,C):
                temp = mat[r][c]
                mat[r][c] = mat[c][r]
                mat[c][r] = temp
                
        # second transformation
        for r in range(R):
            for c in range(0,C//2):
                temp = mat[r][c] 
                mat[r][c] = mat[r][C-c-1]
                mat[r][C-c-1] = temp
                
        return mat
        
            
            