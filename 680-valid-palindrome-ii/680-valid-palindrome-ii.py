class Solution:
    def validPalindrome(self, s: str) -> bool:
        # We will use 2 pointers, low and high where both are pointing to begin and end of list respectively
        low, high = 0, len(s)-1 
  
        # This function is used to check in any string is a palindrome or not based on the low and high index
        def isPalindrome(i,j): 
            while i < j :
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    # as chars don't match, so we return False
                    return False 
            # if we reach here it  means sting is traversed completely and all values are matching
            return True
        
        # driver code starts here
        while (low < high):
            if s[low] == s[high]:
                low += 1        # move low to right
                high -= 1       # move high pointer towards left
            # If both chars don't match, thne we will consider 2 cases
            # In first case, we will skip the low^th characher and in other we will skip high^th char
            # We will return true if either of the case is returning a valid palindrome
            else: 
                # if either of then return true, then string is a palindrome
                return isPalindrome(low+1, high) or isPalindrome(low, high-1) 
        return True
                