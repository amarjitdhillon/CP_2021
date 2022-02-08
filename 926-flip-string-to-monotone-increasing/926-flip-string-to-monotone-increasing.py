class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oneCount, changes = 0,0
        for c in s:
            if c == "1":
                oneCount += 1
            else: # it's a zero
                if oneCount >= 1:
                    changes += 1
            changes = min(changes, oneCount)
        return changes
    
        