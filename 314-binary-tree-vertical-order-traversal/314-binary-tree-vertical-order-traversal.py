# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        # we can do any order of traversal like level order 
        For level order traversal, we can add the optional level (for horizontal) and axis (for vertical) number 
        The left child will have axis-1 and right node will have axis+1
        Each level will be incremented based on it's previous one (skipped in this answer code for simplicity)
        Then we can put the element in to the map of list. The key of map will be the axis and values will be list of items
        
        After the map is populated we can iterate over the map in order of the sorted keys and append the values to a result list. 
        
        Time: O(N) to iterate the tree node twice ( N is the number of nodes in the tree. )
        Space Complexity: O(N) where N is the number of nodes in the tree. 
        
        """
        queue = []
        axis_map = collections.defaultdict(list)
        result = []
        
        if root:
            queue.append([root,0])
        else:
            return []
        
        while len(queue)>0:
            #take the first element from front of queue
            element = queue.pop(0)
            
            node, axis = element[0], element[1]
            
            if node.left:
                queue.append([node.left,axis-1])

            if node.right:
                queue.append([node.right,  axis+1])
                
            axis_map[axis].append(node.val)
        
        for key in sorted(axis_map.keys()):
            result.append(axis_map[key])
            
        return(result)
            
            