class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while(n>0):
            if n == 1:
                return True
            if n%3 != 0:
                return False
            n = n/3    
                
        