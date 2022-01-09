class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        - First we can create a adjacency list (as hashmap) from the given edges list. This will take o(n) time
        - Then we can iterate over the adjacency list hashmap and calculate the degree of each vertex
        - Output the node, which has degree as length of edges list
        
        Time complexity: O(N) as we are iterating
        Space complexity:
        """
        
        # create a adjacency list
        al = collections.defaultdict(list)
        res = 0
        for x in edges:
            al[x[0]].append(x[1]) 
            al[x[1]].append(x[0])
            
            if len(al[x[0]]) == len(edges):
                res = x[0]
                break
                
            if len(al[x[1]]) == len(edges):
                res = x[1]
                break
            
        return res
        
        
        
        