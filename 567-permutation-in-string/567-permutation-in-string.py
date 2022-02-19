class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        if len(s2) < len(s1): # edge case
            return False
        
        freq_s1, freq_s2 = [0]*26, [0]*26
            
        # populate freq_s1 list
        for x in s1:
            freq_s1[ord(x)-ord('a')] += 1
            
        # populate freq_s2 list
        for x in range(0,len(s2)-len(s1)+1):
            # if x is 0, then we will loop over the sliding window for the first time
            if x == 0:
                # if x == 0, then loop over the sliding window
                for y in range(x , x+len(s1)):
                        freq_s2[ord(s2[y])- ord('a')] +=  1        
            # if x != 0, increment the count for char in the end of sliding window (of s1 length)
            else: 
                freq_s2[ord(s2[x+len(s1)-1])- ord('a')] +=  1 
                
            # if both list are same then we have found the match
            if freq_s2 == freq_s1:
                return True
            
            # decrement count for char in begining of sliding window, for next iteration
            freq_s2[ord(s2[x])- ord('a')] -=  1
                
        return False
                
