class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        limit = math.pow(2,31)
        
        negative = False
        if x < 0: 
            negative = True
            x = -x      # removing -ve for now and will add -ve to result
            
        r = 0
        
        while(x != 0):
            l = x%10      # remainder is the last digit
            x = x//10     # quotient is the pending digit
            r = (r*10) + l
            
            if r >= limit-1 or r < -limit: # check limits
                return 0
            
        return r if not negative else -r

        