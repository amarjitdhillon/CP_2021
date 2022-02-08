class Solution:
    def uniqueLetterString(self, s: str) -> int:
        record = [[] for _ in range(26)]
        # record all the index
        for i,letter in enumerate(s):
            record[ord(letter) - 65].append(i)

        ans = 0
        # avoid searching the letters that don not appear in the string, and adding the boundary index.
        check_list = [[-1]+index+[len(s)] for index in record if index]
        for index in check_list:
            for i in range(1,len(index)-1):
                ans+=(index[i] - index[i-1])*(index[i+1] - index[i])

        return ans