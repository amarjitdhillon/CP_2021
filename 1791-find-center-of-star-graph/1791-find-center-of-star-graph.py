class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        def using_hashmap():
            '''
            - First we can create a adjacency list (as hashmap) from the given edges list. This will take o(n) time
            - While creating the adjacency list hashmap we can calculate the degree of each vertex
            - if the degree of a vertes has length equal to length of "edges list" then break from the loop and return that vertex

            Time complexity: O(N) as we are iterating once in a graph
            Space complexity: O(N) for storing hashmap
            '''
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
        
        def simpler_approach():
            '''
            This approach uses the fact that the center node should be present in all the pairs. So it simply means that if we pick any one node from the from the first pair, then either one of these nodes should be present in the second pair too. Once we found that node, that is our answer
            '''
            x=edges[0][0] 
            y=edges[0][1]
            if(x in edges[1]):
                return x
            else:
                return y
            
        return simpler_approach()
        
        
        