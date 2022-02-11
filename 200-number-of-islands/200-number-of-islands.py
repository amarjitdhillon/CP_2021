class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows,num_cols,num_islands = len(grid), len(grid[0]),0
        visited = set()
        
        def findIsland(r,c):
            visited.add((r,c))
                
            # find right neighbour value
            if c+1 < num_cols and grid[r][c+1] == "1" and (r,c+1) not in visited:
                findIsland(r,c+1)
            
            # find left neighbour value
            if c-1 >= 0 and grid[r][c-1] == "1" and (r,c-1) not in visited:
                findIsland(r,c-1)
                
            # find top neighbour value
            if r-1 >= 0 and grid[r-1][c] == "1" and  (r-1,c) not in visited:
                findIsland(r-1, c)
            
            #  find bottom neighbour value
            if r+1 < num_rows and grid[r+1][c] == "1" and (r+1,c) not in visited:
                findIsland(r+1, c)
                

                 
        # driver code
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    findIsland(row,col)
                    num_islands += 1
        return num_islands
        
            