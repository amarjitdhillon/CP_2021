class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = []
        result  = []
        for i, log in enumerate(logs):
            lg = log.split(" ")
            if lg[1].isalpha(): #is a word
                res.append((0,lg[1:], lg[0],i))   # tuple with 3 keys
            else:
                res.append((1,None, None,i))
                
        res = sorted(res)
        for x in res:
            index = x[3]
            result.append(logs[index])
        return result