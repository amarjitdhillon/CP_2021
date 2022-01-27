class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        open_brace, close_brace = '(', ')'
        for i in range(len(s)):
            char = s[i]
            if char == open_brace:
                stack.append([char,i])
            elif char == close_brace :
                if len(stack) > 0 and stack[-1][0] == open_brace: # remove the open brace
                    stack.pop()  
                else:  # add the close brace
                    stack.append([char,i])
        
        extra = []
        res = []
        
        for [x,y] in stack:
            extra.append(y)
            
        for i in range(len(s)):
            if i in extra:
                continue
            res.append(s[i])
        return "".join(res)
                