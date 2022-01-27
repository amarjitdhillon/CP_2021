class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x) # convert to a string
        
        if len(x) == 2: # edge case for length 2
            if x[0] == x[1]:
                return True
            else:
                return False
            
        # use two pointer for length > 2 
        l = 0  
        h = len(x)-1
        
        while(l<h):
            if x[l] != x[h]:
                return False
            else:
                l += 1
                h -= 1
        return True