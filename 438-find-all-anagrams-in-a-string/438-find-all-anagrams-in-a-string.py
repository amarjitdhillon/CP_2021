class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        1. len(P) >= len(S). if not return [] as there is no anagram
        2. Take sliding  window of len(P) and slide over the S array. Update the frequecy list for each window
            if both lists are same then add the index to result list.append
        3. At then end return res list
        '''
        
        res, charP, charS = [], [0]*26, [0]*26
        
        if len(p) > len(s): # edge case
            return res
        
        for c in p: # freq count of second word
            charP[ord(c)-ord('a')] += 1
        
        for i in range(0, len(s)-len(p)+1): # iterate over the first word with sliding window of len(p)
            if i == 0: # begining of the word
                for j in range(i, i+len(p)):
                    charS[ord(s[j])-ord('a')] += 1       
            else: # increment the end of sliding window count in charS
                charS[ord(s[i+len(p)-1])-ord('a')] += 1
                
            if charS == charP:
                res.append(i)
            
            # decrement the starting of sliding window count in charS
            charS[ord(s[i])-ord('a')] -= 1
            
        return res