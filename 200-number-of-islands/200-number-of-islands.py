class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows,num_cols = len(grid), len(grid[0])
        
        x = 0
        def findIsland(r,c):
            
            grid[r][c] = "x"
                
            # find right 
            if c+1 > -1 and c+1 < num_cols and grid[r][c+1] == "1":
                findIsland(r,c+1)
            
            # call left
            if c-1 > -1 and c-1 < num_cols and grid[r][c-1] == "1":
                findIsland(r,c-1)
                
            # call top
            if r-1 > -1 and r-1 < num_rows and grid[r-1][c] == "1":
                findIsland(r-1, c)
            
            # call bottom
            if r+1 < num_rows and r+1 > 0 and grid[r+1][c] == "1":
                findIsland(r+1, c)
                        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    findIsland(row,col)
                    x += 1
        return x
        
            