class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)       # num of rows 
        C = len(board[0])    # num of cols
        
        # use a set to hold all the values which are visited before in the path
        visited = set()     
        
        '''
        Desc for findIfExists function
        r: represent current row index  starting from top, left as 0,0
        c: represent current column index starting from top, left as 0,0
        i: represent # of characters found so far
        '''
        def findIfExists(r,c,i):
            # Base case: if this is the last char, then return True as we have alredy found all the chars that is why the index is equal to len(word) now
            if i == len(word):  
                return True
            
            '''
            Desc: Return false for all invalid cases which are:-
            - The values of r and c are out of bounds
            - The ith character we are looking for has not been found in the board
            - This r,c (representing a cell) was already visited
            
            In any such case, return False
            '''
            if r < 0 or r >= R or c < 0 or c >= C or word[i] != board[r][c] or (r,c) in visited:  
                return False
            
            # to make sure we are not using the same element twice, add the current cell tuple to a visited set    
            visited.add((r,c)) 
            
            # if any of the four immediate neighbours (left, right,top or botton) is true then we will return True else we will backtrack
            temp = findIfExists(r-1,c,i+1) or findIfExists(r+1,c,i+1) or findIfExists(r,c+1,i+1) or findIfExists(r,c-1,i+1) 
            
            # remove the position of item from the list as we have iterated over to it's next set of chars
            visited.remove((r,c)) 
            
            return temp
        
        # Program execution starts here. We will run DFS for all the elements and return True if we found the word
        for r in range(R):
            for c in range(C):
                if findIfExists(r,c,0):
                    return True
                
        # after all the DFS is run, if the program came here it means we have not found the word, so return False
        return False    
                    
        
        
        
        
        
        