# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        
        """
        
        queue = []
        axis_map = collections.defaultdict(list)
        result = []
        
        if root:
            queue.append([root,0,0])
        else:
            return []
        
        while len(queue)>0:
            #take the first element from front of queue
            element = queue.pop(0)
            
            node,level, axis = element[0], element[1], element[2]
            
            if node.left:
                queue.append([node.left, level+1, axis-1])

            if node.right:
                queue.append([node.right, level+1, axis+1])
                
            axis_map[axis].append(node.val)
        
        for key in sorted(axis_map.keys()):
            result.append(axis_map[key])
            
        return(result)
            
            