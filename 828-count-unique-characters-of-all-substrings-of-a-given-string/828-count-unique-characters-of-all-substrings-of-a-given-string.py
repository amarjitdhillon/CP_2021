class Solution:
    def uniqueLetterString(self, s: str) -> int:
        record = [[] for _ in range(26)]    # for all english characters
        
        # record all the index
        for index,character in enumerate(s):
            record[ord(character) - 65].append(index)
            
        result = 0
        # avoid searching the letters that do not appear in the string, and adding the boundary index.
        check_list = [[-1]+index+[len(s)] for index in record if index]
        
        for index in check_list:
            for i in range(1,len(index)-1):
                left = index[i] - index[i-1]
                right = index[i+1] - index[i]
                result += left* right

        return result