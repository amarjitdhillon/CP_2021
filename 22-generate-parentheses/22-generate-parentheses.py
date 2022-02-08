class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        open_count,close_count, result, r = 0, 0, [], []
        
        def generateParanthesis(open_count,close_count,r):
            
            if open_count == close_count == n:  # base case, bottom of the tree
                result.append("".join(r))       # add it to the final result
                return
            
            if open_count < n :
                r.append("(")
                generateParanthesis(open_count+1,close_count,r)
                r.pop() # to make it to the old state as we need to add ( again
                
            if close_count < open_count:
                r.append(")")
                generateParanthesis(open_count,close_count+1,r)
                r.pop()
                
        generateParanthesis(0,0,r) # call recursive function

        return result