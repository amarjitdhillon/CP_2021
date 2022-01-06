# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # edge case
            return []
        
        queue,result, level  = [root], [] , 0
        
        while len(queue) > 0:
            
            result.append([]) # add empty list of each level
            
            for _ in range(len(queue)):  # iterate over the one level
                node = queue.pop(0)      # take out first element in queue
                
                if node:
                    result[level].append(node.val)    # add the node to ith index, each corresponding to a level
            
                # add the left child to queue
                if node.left:
                    queue.append(node.left)

                # add the right child to queue
                if node.right:
                    queue.append(node.right)
                
            level += 1   # increase level as this level is processed
        return result
                
            
            
        