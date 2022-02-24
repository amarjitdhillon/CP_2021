class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        # edge case
        if len(mat) == 0:
            return 0
        
        visited = set()
        numberOfProvinces = 0
        
        # depth first search recursive formula
        def dfs(r):
            nonlocal visited
            visited.add(r)
            
            for c in range(len(mat[r])):
                # call dfs if city is not visited and connection is there
                if c not in visited and mat[r][c] == 1:
                    dfs(c)
            
        # driver code
        for x in range(len(mat)):            
            if x not in visited:
                dfs(x)
                numberOfProvinces += 1
        
        return numberOfProvinces
            
        
        
        
        
        