class Solution:
    def isPalindrome(self, x: int) -> bool:
        # All -ve values will not be a palindrome in this case
        if x < 0:
            return False
        
        # convert to a string as we will iterate over it later
        x = str(x) 
        
        # Let's handle an edge case for length == 2
        if len(x) == 2: 
            return True if x[0] == x[1] else False

            
        # use two pointer for length > 2
        # here we will use two pointers low and high. Initially low will point to the begining and high to the eld
        low = 0  
        high = len(x)-1
        
        while(low < high):
            # if the values are not same then return False
            if x[low] != x[high]:
                return False
            else:
                # else shift low pointer to the right and high pointer to the left
                low += 1
                high -= 1
        return True