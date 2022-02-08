class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oneCount, changes = 0,0                 # intially both are 0
        for c in s:
            if c == "1":
                oneCount += 1
            else:                               # if not 1 then it's a zero
                if oneCount >= 1:       
                    changes += 1                # in case we have already seen a zero, we will increase the changes count
            changes = min(changes, oneCount)    # we will do changes if it's count is less then # of 1's seen so far
        return changes
    
        