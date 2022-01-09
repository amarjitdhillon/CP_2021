class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # if len(edges) == 0:
        #     return None
        
        # create a adjacency list
        al = collections.defaultdict(list)
        for x in edges:
            al[x[0]].append(x[1]) 
            al[x[1]].append(x[0])
        
        res = 0
        for y in al:
            if len(al[y]) == len(edges):
                res = y
                break
            
        return res
        
        
        
        