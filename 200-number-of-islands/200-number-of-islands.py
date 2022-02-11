class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows,num_cols,num_islands = len(grid), len(grid[0]),0
        visited = set()
        
        def findIsland(r,c):
            # add this cell to the visited set
            visited.add((r,c))
            
            # add left, right, top and down respectively
            neighbours = [[0,-1], [0,1],[-1,0],[1,0]]
            
            for row_id,col_id in neighbours:
                
                # Visit a partiular neighbour if the index values are within bounds and the value at neighbour == 1 and that cell is not already visited
                if 0 <= (c+col_id) < num_cols and 0 <= (r+row_id ) < num_rows and grid[r+row_id][c+col_id] == "1" and (r+row_id,c+col_id) not in visited:
                    findIsland(r+row_id,c+col_id)
                 
        # driver code
        for row in range(num_rows):
            for col in range(num_cols):
                # call each cell element if that is not already visited
                if grid[row][col] == "1" and (row,col) not in visited:
                    findIsland(row,col)
                    
                    # increment the count if findIsland() returned it's execution as it means one set of continuous cells have been traversed
                    num_islands += 1
        return num_islands
        
            