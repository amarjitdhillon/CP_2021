class Solution:
    def longestPalindrome(self, arr: str) -> str:
        # From each number we can go outwards and check if its a valid palindrome
        palindromeString, curLen, resLen = "", 0 , 0
        
        def findPalindrome(start, end):
            # These are global variables
            nonlocal resLen, palindromeString
            
            # while the start and end strings are within bounds and are same, then keep expanding outwards 
            while(start >= 0 and end < len(arr) and (arr[start] == arr[end])): 
                # find the current length of the palindrome string
                currLen = end-start+1
                
                if currLen > resLen:
                    # update both the resLen and palindromeString as we have found a new string with more length then older one
                    palindromeString = arr[start:end+1]
                    resLen = currLen
                start   -= 1  # move `start` to right
                end     += 1  # move `end` to left
        
        # driver code 
        for i in range(len(arr)):
            findPalindrome(i,i)     # For odd length case, set start and end as the same index 
            findPalindrome(i,i+1)   # For even length case, set start and end as adjoining indexes      
        return palindromeString
            