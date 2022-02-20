"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    #  left --> right --> root
    def postorder(self, root: 'Node') -> List[int]:  
        res = []
        
        def dfsPost(root) :
            # res is a global variable that we are using
            nonlocal res
            
            # base case for null node
            if not root: return 

            # loop over the childrens and call the DFS function
            for child in root.children:
                dfsPost(child)  
                
            # add the value to the res list
            res.append(root.val)
            
            return res
        
        # driver code
        return dfsPost(root)
        
