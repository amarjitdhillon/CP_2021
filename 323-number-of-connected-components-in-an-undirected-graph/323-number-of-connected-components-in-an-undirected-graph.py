from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create an adjacency list
        al = collections.defaultdict(list)
        
        for x,y in edges:
            al[x].append(y)
            al[y].append(x)
            
        count = 0
        visited = set()
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
            else:
                return
            
            for x in al[node]:
                dfs(x)
            
            
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
                
        return count
                
                
        

            