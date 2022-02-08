class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Time complexity: O(N) as we are iterating the matrix twice where N is the number of cells in the grid.
        Space complexity: O(1) as  we are doing the in place transaction
        """
        C = len(mat[0])
        R = len(mat)
        
        # first transformation is for all the rows and half of the element lying to right hand side of diagonal
        for r in range(R):
            for c in range(r,C):
                mat[r][c], mat[c][r] = mat[c][r], mat[r][c]

                
        # second transformation is for all the rows and all elements lying to left of the middle column.
        for r in range(R):
            for c in range(0,C//2):
                mat[r][c], mat[r][C-c-1] = mat[r][C-c-1], mat[r][c]
                
        return mat
        
            
            