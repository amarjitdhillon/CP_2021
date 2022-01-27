class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, h = 0, len(s)-1 # use 2 pointers
  
        def isPalindrome(i,j): # used to check in any string is a palindrome
            while i < j :
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False # as chars don't match, so we return False
            return True
        
        while (l<h):
            if s[l] == s[h]:
                l += 1
                h -= 1
            else: # we will consider 2 cases, in first we will skip the l^th characher and in other we will skip h^th char
                return isPalindrome(l+1, h) or isPalindrome(l, h-1) # if either of then return true, then string is a palindrome
        return True
                