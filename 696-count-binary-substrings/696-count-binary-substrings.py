class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        Intution: We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string. For example, if s = "110001111000000", then groups lenghts will be [2, 3, 4, 6]
        Then, we can make min(groups[i], groups[i+1]) valid binary strings within this string. Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.
        
        Let's understand this with example
                For 00011 we have 2 groups of length 3 and 2, yet here we can make 2 valid substrings whch is min(4,2). 
                    These strings are 0011 and 01. So clearly min group is the limiting factor
                 For 000011, we have 2 groups of length 4 and 2, yet here we can make 2 valid substrings whch is min(4,2). 
                    These strings are 0011 and 01. I hope the logic is clear
        '''
        # Initial count of next group will be starting from 1, that is why currentGroupCounter is 1
        previousGroupCounter, currentGroupCounter, result = 0, 1 , 0
        
         # iterate from the second char onwards as we need to compare it with the previous element(fist)
        for i in range(1, len(s)):
            
             # if the consecutive values are same, it means we should increase the current group counter and keep expanding the current group 
            if s[i-1] == s[i]: 
                currentGroupCounter += 1
            else:
                '''
                Otherwise, we need to take the minimum from the 2 consecutive groups that we have found. 
                 '''
                result += min(previousGroupCounter,currentGroupCounter)
                
                # save the result of the currentGroupCounter as we need to move on to next group
                previousGroupCounter = currentGroupCounter   
                
                # the initial count of next group will be starting from 1
                currentGroupCounter = 1
                
        #  After loop is over, we need to compare the last 2 groups
        result += min(previousGroupCounter,currentGroupCounter) 
        
        return result
            
                