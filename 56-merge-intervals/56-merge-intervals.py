class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:

        
        i.sort(key = lambda x:x[0])  # sort by the first value
        c = i[0]    # start limit
        r = []      # result array
        
        for x in i:
            if x[0] >= c[0] and x[0] <= c[1]: # this starting values lies in the range of prev tuple
                c[0] = min(c[0],x[0])
                c[1] = max(c[1],x[1])        
                continue
            else:
                r.append(c) # append the previous value
                c = x
                
        r.append(c) # add the last value
        return r
        
        