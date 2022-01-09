class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        - First we can create a adjacency list (as hashmap) from the given edges list. This will take o(n) time
        - While creating the adjacency list hashmap we can calculate the degree of each vertex
        - if the degree of a vertes has length equal to length of "edges list" then break from the loop and return that vertex
        
        Time complexity: O(N) as we are iterating once in a graph
        Space complexity: O(N) for storing hashmap
        """
        def using_hashmap():
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
        
        f=edges[0][0] 
        s=edges[0][1]
        if(f in edges[1]):
            return f
        else:
            return s
        
        
        