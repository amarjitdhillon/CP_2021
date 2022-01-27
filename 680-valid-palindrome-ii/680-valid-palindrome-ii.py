class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if len(s) == 2:
        #     return True
        
        l, h = 0, len(s)-1
  
        def isPalindrome(i,j):
            while i < j :
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        
        while (l<h):
            if s[l] == s[h]:
                l += 1
                h -= 1
            else:
                return isPalindrome(l+1, h) or isPalindrome(l, h-1)
        return True
                