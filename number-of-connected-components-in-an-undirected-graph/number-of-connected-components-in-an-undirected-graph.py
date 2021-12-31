from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # create a adjacency list called al
        al = defaultdict(list)
        
        for edge in edges:
            al[edge[0]].append(edge[1])
            al[edge[1]].append(edge[0])
         
        visited = set()
        count = 0
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
            else:
                return
            
            for edge in al[node]:
                dfs(edge)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
             
            