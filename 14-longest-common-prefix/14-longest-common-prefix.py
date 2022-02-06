class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''   # final output
        
        if len(strs) == 0: # special case
            return res
        
        min_element = min(strs, key = len) # find the min length word in strs
        
        for i in range(len(min_element)):
            for s in strs:
                if s[i] != strs[0][i]: # return if chars dont match with the first word
                    return res
            res += s[i]  # if all the chars match, then add it to the result
        return res