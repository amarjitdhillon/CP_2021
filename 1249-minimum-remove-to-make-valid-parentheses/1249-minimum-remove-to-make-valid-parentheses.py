class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        this is a 3 pass solution with 2 pass for the string and one pass for the stack to get the index 
        if we encounter closing brace, then we will not apend it in stack and remove the opening brace tuple from stack
        if we encounter a opening brace, we will add it to stack along with it's index
        
        After the first iteration, the stack will contain all the braces which needs to be removed
        so we will iterate over the stack and get all the index which needs to be removed
        
        In the third iteration, we will loop over the string and not include the index values which are present in the stack
        Finally join the elements in stack and return the string
        '''
        stack = [] # this will hold the braces
        open_brace, close_brace = '(', ')'
		
		# first pass
        for i in range(len(s)):
            char = s[i]
            if char == open_brace:
                stack.append([char,i])
            elif char == close_brace :
                if len(stack) > 0 and stack[-1][0] == open_brace: # remove the open brace
                    stack.pop()  
                else:  # add the close brace
                    stack.append([char,i])
        
        extra = [] # contain index of elements to be removed
        res = []   # final list of chars to be returned
        
		# second pass
        for [x,y] in stack:
            extra.append(y) 
            
		# third pass	
        for i in range(len(s)):
            if i in extra: # skip this char
                continue
            res.append(s[i])
            
        return "".join(res) # return the chars as string