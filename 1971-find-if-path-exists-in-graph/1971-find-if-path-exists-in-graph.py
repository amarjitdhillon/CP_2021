class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        # if the edges list is empty then return False
        if len(edges) in [0,1]:
            return True
        
        # build the adjacency list
        edgeDict = collections.defaultdict(list)
        for x,y in edges:
            edgeDict[x].append(y)
            edgeDict[y].append(x)
            
        
        # Edge case: check if either of the vertex is not in the graph
        if not start in edgeDict or not end in edgeDict:
            return False
        
        visited = [False] * (len(edgeDict)*2)
        queue = [start]
        
        found = False
        
        while queue:
            node = queue.pop(0)  # take out the node which we want to process
            
            # mark it as visited
            visited[node] = True
            
            if end in edgeDict[node]:
                found = True
                break
            
            # add all the neighbours to the queue for processing
            for val in edgeDict[node]:
                if visited[val] == False: # only add the node if it is not visited
                    queue.append(val)
                
        return found
        
        
            
        
        
        