class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)      # num of rows 
        cols = len(board[0])   # num of cols
        
        visited = set()  # to hold all the values which are visited before in the path
        
        def findIfExists(r,c,i):
            if i == len(word):  # if this is the last char, then return True as we have alredy found all the chars that is why the index is equal to len(word) now
                return True
            
            # return false for all invalid values
            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or (r,c) in visited:  # if the element was last seen in the visited set, it became invalid so we are returning False
                return False
                
            visited.add((r,c)) # to make sure we are not using the same element twice
            temp = findIfExists(r-1,c,i+1) or findIfExists(r+1,c,i+1) or findIfExists(r,c+1,i+1) or findIfExists(r,c-1,i+1) # if any of the neighbours is true, we return true else we will backtrack
            visited.remove((r,c)) # remove the position of item from the list as we have iterated over to it's next set of chars
            return temp
        
        # Program execution starts here. We will run DFS for all the elements and return True if we found the word
        for r in range(rows):
            for c in range(cols):
                if findIfExists(r,c,0):
                    return True
        return False    # after all the DFS is run, if the program came here it means we have not found the word, so return False
                    
        
        
        
        
        
        