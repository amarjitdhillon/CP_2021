class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []     
        keypad = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        # edge case
        if len(digits) == 0:
            return []
        
        def dfsKeypad(index,path):
            # Here base condition is when len(path) is equal to the len(digits)
            if len(path) == len(digits): #          # If the path is the same length as digits, we have a complete path  
                result.append("".join(path))        # convert list to string and then add the result
                return                              # backtrack 
            
            for val in keypad[int(digits[index])]:  # loop through various letters that the current digit maps to, 
                path.append(val)                    # Add the letter to our current path
                dfsKeypad(index+1, path)            # Move on to the next digit down the tree
                path.pop()                          # Backtrack by removing the letter before moving onto the next
                
        dfsKeypad(0,[])
        return result
            
        
        
