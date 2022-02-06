class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        # speacial case
        if len(strs) == 0:
            return res
        
        min_element = min(strs, key = len)
        for i in range(len(min_element)):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += s[i]
        return res
                
                    
        