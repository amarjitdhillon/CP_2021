class Solution:
    def longestPalindrome(self, arr: str) -> str:
        # From each number we can go outwards and check if its a valid palindrome
        res, curLen, resLen = "",0 ,0
        
        def findPalindrome(s, e): # s and e are starting and end indexes
            nonlocal resLen, res
            while(s >= 0 and e < len(arr) and (arr[s] == arr[e])): # string is a palindrome
                currLen = e-s+1
                if currLen > resLen:
                    # update both the resLen and res as currLen > resLen
                    res = arr[s:e+1]
                    resLen = currLen
                s -= 1  # move `s` to left
                e += 1  # move `e` to right
        
        for i in range(len(arr)):
            findPalindrome(i,i)   # odd length case
            findPalindrome(i,i+1) # even length case      
        return res
            